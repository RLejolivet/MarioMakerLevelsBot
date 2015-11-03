import os
import sys

def main():
    
    from PySide import QtGui
    from LevelsBotWindow import LevelsBotWindow

    app = QtGui.QApplication(sys.argv)
    win = LevelsBotWindow()
    win.show()
    app.exec_()

if(__name__ == "__main__"):

    if getattr(sys,'frozen',False):
        # if trap for frozen script wrapping
        sys.path.append(os.path.join(os.path.dirname(sys.executable),'bin'))
        sys.path.append(os.path.join(os.path.dirname(sys.executable),'bin/library.zip'))

    main()