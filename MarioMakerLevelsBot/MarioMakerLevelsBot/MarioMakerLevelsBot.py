import os
import sys

def main():
    
    from PySide import QtGui
    from LevelsBotWindow import LevelsBotWindow

    logfile = open("log.txt", "w")
    sys.stdout = logfile
    sys.stderr = logfile

    app = QtGui.QApplication(sys.argv)
    win = LevelsBotWindow()
    win.show()
    app.exec_()

    logfile.close()

if(__name__ == "__main__"):

    if getattr(sys,'frozen',False):
        # if trap for frozen script wrapping
        sys.path.append(os.path.join(os.path.dirname(sys.executable),'bin'))
        sys.path.append(os.path.join(os.path.dirname(sys.executable),'bin/library.zip'))

    main()