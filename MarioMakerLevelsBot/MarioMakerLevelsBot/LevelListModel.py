from PySide import QtCore
from PySide.QtCore import QModelIndex
from PySide.QtCore import Qt

class Level(object):
    """The class representing a Mario Maker Level for the following model."""

class LevelListModel(QtCore.QAbstractItemModel):
    """The Qt model for the levels list"""

    def __init__(self, parent=None):
        """Initialize the model.
        Loading the levels from a file?"""
        #TODO: implement

    ###########################################################################
    # Qt methods.
    # Those will be used by the Qt View Widget to display the data
    ###########################################################################

    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns in the current model."""
        #TODO: implement

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in the model."""
        #TODO: implement

    def index(self, row, column, parent=QModelIndex()):
        """Return an index for the item in the position designed by row and column.
        If the item does not exist, return QModelIndex()."""
        #TODO: implement

    def data(self, index, role=Qt.DisplayRole):
        """Return the data for the index, given the corresponding role."""
        #TODO: implement

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return the data for the row and column headers."""
        #TODO: implement

    def flags(self, index):
        """Return the Qt flags for the index."""
        #TODO: implement

    def sort(column, order=Qt.AscendingOrder):
        """Sort the indexes by column, in order."""
        #TODO: implement

    ###########################################################################
    # User methods.
    # Those are used by the rest of the program to interact with the data
    ###########################################################################

    def add_level(self, code, tags=None):
        """Add a new level to the list if it isn't already in."""
        #TODO: implement

