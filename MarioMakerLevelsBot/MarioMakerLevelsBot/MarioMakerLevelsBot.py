import sys

def main():
    
    from PySide import QtGui
    from LevelsBotWindow import LevelsBotWindow

    app = QtGui.QApplication(sys.argv)
    win = LevelsBotWindow()
    win.show()
    app.exec_()

if(__name__ == "__main__"):
    main()