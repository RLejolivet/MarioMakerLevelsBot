import enum
import datetime
import threading

from PySide import QtCore
from PySide.QtCore import QModelIndex
from PySide.QtCore import Qt

class Filters(enum.IntEnum):
    NoFilter = 0
    Fake = 1
    PotentiallyFake = 2
    Subs = 4
    Mods = 8

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

    def check_filters(self):
        """Check which filters may apply to this Level.
        """
        # TODO: call check if the level is in the fakes
        # TODO: call check if the level may be fake
        # TODO: call check if tags contain sub and/or mod

class LevelListModel(QtCore.QAbstractTableModel):
    """The Qt model for the levels list"""

    def __init__(self, parent=None):
        """Initialize the model.
        Loading the levels from a file?"""
        super().__init__(parent)

        # Contains all the submitted levels.
        # Key: level code
        # Value: Level instance
        self.levels_dict = {}
        self.dict_lock = threading.Lock() # Prevent access racing on levels dict

        # Contains all the levels that should be shown to the view
        # The index in this list is the row for the view.
        self.view_list = []
        self.list_lock = threading.Lock() # Prevent access racing on view list

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
            if(col == 0): # Number requested
                return "{}".format(row) # self.view_list[row].date
            elif(col == 1): # Code
                return self.view_list[row].code
            elif(col == 2): # Name the level was requested by
                return self.view_list[row].name
            elif(col == 3): # Tags (sub and/or mod)
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
            elif(col == 4): # Number of times requested
                return self.view_list[row].times_requested


    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return the data for the row and column headers."""
        if(orientation == Qt.Horizontal and role == Qt.DisplayRole):
            if(section == 0):
                return "#"
            elif(section == 1):
                return "Code"
            elif(section == 2):
                return "User"
            elif(section == 3):
                return "Privileges"
            elif(section == 4):
                return "Times requested"

    #def sort(column, order=Qt.AscendingOrder):
    #    """Sort the indexes by column, in order."""
        #TODO: implement

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

        self.list_lock.acquire()

        self.beginInsertRows(QModelIndex(), len(self.view_list), len(self.view_list))
        self.view_list.append(Level(datetime.datetime.now(), code, name, tags))
        self.endInsertRows()

        self.list_lock.release()

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
