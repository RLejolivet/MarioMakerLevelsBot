from PySide import QtCore, QtGui
from ui.window import Ui_MainWindow

import LevelListModel

class LevelsBotWindow(Ui_MainWindow, QtGui.QMainWindow):
    """The QMainWindow class for the Mario Maker Levels Bot, 
    containing all the UI logic."""

    
    def __init__(self):
        super().__init__(None)
        self.setupUi(self)

        self.level_list_model = LevelListModel.LevelListModel()
        
        # Testing items, TODO: delete
        self.level_list_model.add_level("ABCD-0000-0069-A5D9", "SomeGuyInChat")
        self.level_list_model.add_level("ABCD-0000-0012-A5D9", "Laraeph", {"subscriber": True, "user-level": 0})
        self.level_list_model.add_level("1234-0000-00AB-CDEF", "ARandomMod", {"subscriber": False, "user-level": 1})
        self.level_list_model.add_level("78CD-0000-AD95-FFFF", "ASubbedMod", {"subscriber": True, "user-level": 1})

        self.levels_tableView.setModel(self.level_list_model)
        self.levels_tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)