import datetime
import threading

from PySide import QtCore
from PySide.QtCore import QModelIndex
from PySide.QtCore import Qt

class Level(object):
    """The class representing a Mario Maker Level for the following model."""

    def __init__(self, date, code, name, tags):
        self.date = date
        self.code = code
        self.name = name
        self.tags = tags

class LevelListModel(QtCore.QAbstractTableModel):
    """The Qt model for the levels list"""

    def __init__(self, parent=None):
        """Initialize the model.
        Loading the levels from a file?"""
        super().__init__(parent)
        self.levels_list = []
        self.list_lock = threading.Lock()

    ###########################################################################
    # Qt methods.
    # Those will be used by the Qt View Widget to display the data
    ###########################################################################

    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns in the current model."""
        return 4 #Date added, level code, request name, tags

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in the model."""
        return len(self.levels_list)

    def data(self, index, role=Qt.DisplayRole):
        """Return the data for the index, given the corresponding role."""
        if(not self._is_valid_index(index)):
            return None

        if(role == Qt.DisplayRole):
            row = index.row()
            col = index.column()
            if(col == 0):
                return "" # self.levels_list[row].date
            elif(col == 1):
                return self.levels_list[row].code
            elif(col == 2):
                return self.levels_list[row].name
            elif(col == 3):
                tags = self.levels_list[row].tags
                if(tags is None):
                    return ""
                elif(tags['subscriber'] and tags['user-level']): # tags['user-level'] > 0
                    return "Sub and Mod"
                elif(tags['subscriber']):
                    return "Sub"
                elif(tags['user-level']): # tags['user-level'] > 0
                    return "Mod"
                else:
                    return ""


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

    #def sort(column, order=Qt.AscendingOrder):
    #    """Sort the indexes by column, in order."""
        #TODO: implement

    ###########################################################################
    # User methods.
    # Those are used by the rest of the program to interact with the data
    ###########################################################################

    def add_level(self, code, name, tags=None):
        """Add a new level to the list if it isn't already in."""

        self.list_lock.acquire()

        self.beginInsertRows(QModelIndex(), len(self.levels_list), len(self.levels_list))
        self.levels_list.append(Level(datetime.datetime.now(), code, name, tags))
        self.endInsertRows()

        self.list_lock.release()

    ###########################################################################
    # Private methods
    # Used by the model for the model
    ###########################################################################

    def _is_valid_index(self, index):
        row = index.row()
        column = index.column()
        return not (row < 0 or column < 0 or
                    row >= len(self.levels_list) or column > 4 or
                    index == QModelIndex())
