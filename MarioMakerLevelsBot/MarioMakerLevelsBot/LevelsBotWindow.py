from PySide import QtGui
from ui.window import Ui_MainWindow

class LevelsBotWindow(Ui_MainWindow, QtGui.QMainWindow):
    """The QMainWindow class for the Mario Maker Levels Bot, 
    containing all the UI logic."""

    
    def __init__(self):
        super().__init__(None)
        self.setupUi(self)