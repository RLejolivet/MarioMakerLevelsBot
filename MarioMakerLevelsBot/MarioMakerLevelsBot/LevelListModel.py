import enum
import bisect
import datetime
import threading

from PySide import QtCore, QtGui
from PySide.QtCore import QModelIndex
from PySide.QtCore import Qt

class Filters(enum.IntEnum):
    """Enumerates all the filters.
    The numbers are powers of two to enable bitwise operations to select filters.
    AllFilters should be the number of all filters enabled bitwise.
    """
    NoFilter = 0
    AllFilters = 0x0F
    Fake = 1
    PotentiallyFake = 2
    NonSubs = 4
    NonMods = 8

class Sorting(enum.IntEnum):
    """Enumerates all the sorting options.
    Like Filters, the numbers are powers of two,
    in case multiple sorting options can be selected at the same time.
    """
    NoSorting = 0 # Unlikely but to keep boolean logic
    AllSorting = 0x3F # Even more unlikely but may be used in bitwise operations maybe
    Reversed = 1 # This flag means the sorting is reversed, or in descending order.
    Date = 2
    Code = 4
    User = 8
    Priviledges = 16
    TimesRequested = 32


class Level(object):
    """The class representing a Mario Maker Level for the following model."""

    def __init__(self, date, code, name, tags):
        super().__init__()
        self.date = date
        self.code = code
        self.name = name
        self.tags = tags
        self.times_requested = 1
        self.filters = Filters.NoFilter

        self.check_filters()

    def check_filters(self):
        """Check which filters may apply to this Level.
        """
        # TODO: call check if the level is in the fakes
        self.check_potentially_fake()
        self.check_tags()

    def check_potentially_fake(self):
        """Check if the code is potentially fake due to its form.
        """
        # Check if the second group of numbers is different than 0000
        if(self.code[5:9] != "0000"):
            self.filters |= Filters.PotentiallyFake

    def check_tags(self):
        """Check the tags to see if any filters should be applied to this level.
        """
        if(self.tags is None or not self.tags.get('subscriber', False)):
            self.filters |= Filters.NonSubs

        if(self.tags is None or not self.tags.get('user-type', 0) > 0):
            self.filters |= Filters.NonMods

    @classmethod
    def key(self, sorting):
        """Return a key function to sort a Level according to the sorting parameter.
        """
        if(sorting & Sorting.NoSorting):
            return (lambda x: 1) # All elements get the same key

        if(sorting & Sorting.Date):
            return (lambda x: x.date)

        if(sorting & Sorting.Code):
            return (lambda x: x.code)

        if(sorting & Sorting.User):
            return (lambda x: x.name)

        if(sorting & Sorting.Priviledges):
            # Not having priviledges grants "points": the more points the higher in the sort
            return (lambda x: (x.filters & Filters.NonSubs) + (x.filters & Filters.NonMods))

        if(sorting & Sorting.TimesRequested):
            return (lambda x: x.times_requested)

class Columns(enum.IntEnum):
    """Names the columns in the model
    """
    Date = 0
    Code = 1
    User = 2
    Tags = 3
    TimesRequested = 4



class LevelListModel(QtCore.QAbstractTableModel):
    """The Qt model for the levels list"""

    def __init__(self, parent=None):
        """Initialize the model.
        Loading the levels from a file?"""
        super().__init__(parent)

        # Filters on the model
        self.filters = Filters.NoFilter
        self.sorting = Sorting.Date

        # Contains all the submitted levels.
        # Key: level code
        # Value: Level instance
        self.levels_dict = {}
        self.dict_lock = threading.RLock() # Prevent access racing on levels dict

        # Contains all the levels that should be shown to the view
        # The index in this list is the row for the view.
        self.view_list = []
        self.view_keys = [] # keys for sorting the view
        self.list_lock = threading.RLock() # Prevent access racing on view list

    ###########################################################################
    # Qt methods.
    # Those will be used by the Qt View Widget to display the data
    ###########################################################################

    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns in the current model."""
        return 5 #Date added, level code, request name, tags, times requested

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in the model."""
        return len(self.view_list)

    def data(self, index, role=Qt.DisplayRole):
        """Return the data for the index, given the corresponding role."""
        if(not self._is_valid_index(index)):
            return None

        if(role == Qt.DisplayRole):
            row = index.row()
            col = index.column()
            if(col == Columns.Date): # Number requested
                return "{}".format(row+1) # self.view_list[row].date
            elif(col == Columns.Code): # Code
                return self.view_list[row].code
            elif(col == Columns.User): # Name the level was requested by
                return self.view_list[row].name
            elif(col == Columns.Tags): # Tags (sub and/or mod)
                tags = self.view_list[row].tags
                if(tags is None):
                    return ""
                elif(tags.get('subscriber', False) and tags.get('user-type', 0)): # tags['user-type'] > 0
                    return "Sub and Mod"
                elif(tags.get('subscriber', False)):
                    return "Sub"
                elif(tags.get('user-type')): # tags['user-type'] > 0
                    return "Mod"
                else:
                    return ""
            elif(col == Columns.TimesRequested): # Number of times requested
                return self.view_list[row].times_requested

        elif(role == Qt.TextColorRole):
            row = index.row()
            if(self.view_list[row].filters & Filters.Fake): # Fake flag is on
                return QtGui.QColor("red")
            elif(self.view_list[row].filters & Filters.PotentiallyFake): # Potentially fake flag is on
                return QtGui.QColor("orange")


    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return the data for the row and column headers."""
        if(orientation == Qt.Horizontal and role == Qt.DisplayRole):
            if(section == Columns.Date):
                return "#"
            elif(section == Columns.Code):
                return "Code"
            elif(section == Columns.User):
                return "User"
            elif(section == Columns.Tags):
                return "Privileges"
            elif(section == Columns.TimesRequested):
                return "Times requested"

    def sort(self, column, order=Qt.AscendingOrder):
        """Sort the indexes by column, in order."""
        if(column == Columns.Date):
            self.sorting = Sorting.Date
        elif(column == Columns.Code):
            self.sorting = Sorting.Code
        elif(column == Columns.User):
            self.sorting = Sorting.User
        elif(column == Columns.Tags):
            self.sorting = Sorting.Priviledges
        elif(column == Columns.TimesRequested):
            self.sorting = Sorting.TimesRequested

        if(order == Qt.DescendingOrder):
            self.sorting |= Sorting.Reversed

        self._reset_view()

    def removeRows(self, row, count, parent=QModelIndex()):
        """Removes count rows starting with the given row under parent parent from the model.

        Return True if the rows were successfully removed; otherwise return False.
        """
        self.dict_lock.acquire()
        self.list_lock.acquire()

        self.beginRemoveRows(parent, row, row + count -1)

        for offset in range(count):
            level = self.view_list[row + offset]
            del self.levels_dict[level.code]

        del self.view_list[row:row+count]
        if(not self.sorting & Sorting.Reversed):
            del self.view_keys[row:row+count]
        else:
            del self.view_keys[len(self.view_keys) - (row + count): len(self.view_keys) - row]

        self.endRemoveRows()

        self.list_lock.release()
        self.dict_lock.release()

        return True

    def removeRow(self, row, parent=QModelIndex()):
        """Remove a single row.

        Return True if the row was successfully removed; otherwise return False.
        """
        return self.removeRows(row, 1, parent)

    def reset(self):
        """Reset the model. Removes all levels from it.
        """
        self.dict_lock.acquire()
        self.list_lock.acquire()

        self.beginResetModel()
        self.levels_dict = {}
        self.view_list = []
        self.endResetModel()
        
        self.list_lock.release()
        self.dict_lock.release()

    ###########################################################################
    # User methods.
    # Those are used by the rest of the program to interact with the data
    ###########################################################################

    def add_level(self, code, name, tags=None):
        """Add a new level to the list if it isn't already in."""

        if(tags is not None):
            display_name = tags.get("display-name", "")
            if(display_name != ""):
                name = display_name

        self.dict_lock.acquire()

        level = self.levels_dict.get(code, None)

        if(level is not None):
            level.times_requested += 1

            # Check if the level is (probably) in the list using filters
            if(self._check_filters(level)): # Filters are comaptible
                try:
                    index = self.createIndex(self.view_list.index(level), 4)
                    self.dataChanged.emit(index, index)
                except ValueError: # It wasn't actually in the list, why?
                    self._add_level_to_view(level)


        else:
            level = Level(datetime.datetime.now(), code, name, tags)
            self.levels_dict[code] = level

            if(self._check_filters(level)):
                self._add_level_to_view(level)

        self.dict_lock.release()

    def hide_fake_levels(self, hide):
        """Show or hide the levels that are labeled as fake.
        """
        return self._toggle_filter(Filters.Fake, hide)

    def hide_potentially_fake_levels(self, hide):
        """Show or hide the levels that are labeled as potentially fake.
        """
        return self._toggle_filter(Filters.PotentiallyFake, hide)

    def show_subs_levels_only(self, show):
        """Show or hide the levels that are labeled as non submitted by subs.
        """
        return self._toggle_filter(Filters.NonSubs, show)

    def show_mods_levels_only(self, show):
        """Show or hide the levels that are labeled as non submitted by mods.
        """
        return self._toggle_filter(Filters.NonMods, show)

    def remove_indexes(self, indexes):
        """Remove all the rows in the indexes list.
        """
        # Create a set of the rows (as int) to delete
        selected_rows = set()
        for index in indexes:
            selected_rows.add(index.row())

        # Delete all of them one by one (easy but maybe not the best performance-wise)
        for index, row in enumerate(sorted(selected_rows)):
            self.removeRow(row - index) # The actual target row to be removed decreases by one when a previous is removed

    ###########################################################################
    # Private methods
    # Used by the model for the model
    ###########################################################################

    def _is_valid_index(self, index):
        """Check if the provided index is valid in the model.
        """
        row = index.row()
        column = index.column()
        return not (row < 0 or column < 0 or
                    row >= len(self.view_list) or column > 4 or
                    index == QModelIndex())

    def _check_filters(self, level):
        """Check if the filters on the model and the ones on a level are
        compatible.

        Return True if they are, False if they are not.
        Compatible if any of the filters in the model are not True in the level.
        Because of the values chosen for the filters, this means the bit by bit
        logical AND has to be zero.
        """
        if(self.filters == Filters.NoFilter):
            return True
        else:
            return (self.filters & level.filters == 0)

    def _add_level_to_view(self, level):
        """Adds the level to the view, at the correct position.
        """
        key = Level.key(self.sorting)(level)
        index = bisect.bisect(self.view_keys, key)
        self.view_keys[index:index] = [key]

        # If sorting is reversed, the key list and view are in different orders
        if(self.sorting & Sorting.Reversed):
            index = len(self.view_list) - index


        self.list_lock.acquire()

        self.beginInsertRows(QModelIndex(), index, index)
        self.view_list[index:index] = [level]

        self.endInsertRows()

        self.list_lock.release()

    def _toggle_filter(self, filter, toggle):
        """Toggle the filter on/off according to toggle and rebuild the view
        If it already is on/off, do nothing.
        """
        
        if(bool(self.filters & filter) == bool(toggle)): # Filter already correctly set
            return
        else:
            if(toggle): # Adding the filter
                self.filters |= filter # Add the filter bit
            else:
                self.filters &= Filters.AllFilters ^ filter # Remove the filter bit

            self._reset_view()

    def _reset_view(self):
        """Rebuilds the entire view list according to the filters and sorting.
        """
        self.dict_lock.acquire()
        self.list_lock.acquire()

        self.beginResetModel()

        # Rebuild view with only items that should show
        self.view_list = [ level for level in self.levels_dict.values() if self._check_filters(level) ]

        # Sorting the view, creating the list of keys, and reversing if needed
        self.view_list.sort(key=Level.key(self.sorting))
        self.view_keys = [Level.key(self.sorting)(x) for x in self.view_list]
        if(self.sorting & Sorting.Reversed):
            self.view_list.reverse()

        self.endResetModel()

        self.list_lock.release()
        self.dict_lock.release()
