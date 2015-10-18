﻿import re

from PySide import QtCore, QtGui
from ui.window import Ui_MainWindow

import ChatListener
import LevelListModel

class LevelsBotWindow(Ui_MainWindow, QtGui.QMainWindow):
    """The QMainWindow class for the Mario Maker Levels Bot, 
    containing all the UI logic."""

    
    def __init__(self):
        super().__init__(None)
        self.setupUi(self)

        self.level_list_model = LevelListModel.LevelListModel()
        self.levels_tableView.setModel(self.level_list_model)
        self.levels_tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.chat_listener = None
        self.connect_button.clicked.connect(self.connect)
        self.find_codes_checkbox.stateChanged.connect(self.toggle_check_codes)

    def connect(self):
        if(self.chat_listener is None):
            self.chat_listener = ChatListener.ChatListener(
                self.twitch_name_lineedit.text(),
                self.twitch_oauth_lineedit.text(),
                self.channel_lineedit.text(),
                self)
            self.chat_listener.start()

    def toggle_check_codes(self, checked):
        """Slot receiving information about if chat should be parsed or not.
        """
        if(checked):
            if(self.chat_listener is not None):
                self.chat_listener.add_callback(self.parse_message)
            else:
                box = QtGui.QMessageBox.information(
                    self,
                    "Not connected to Twitch chat",
                    "The bot is currently not connected to Twitch chat.\n"
                    "Head to the Twitch chat info tab to connect."
                    )
                self.find_codes_checkbox.setCheckState(QtCore.Qt.Unchecked)

        else:
            if(self.chat_listener is not None):
                self.chat_listener.remove_callback(self.parse_message)

    code_re = re.compile("[0-9A-F]{4}[ \-_][0-9A-F]{4}[ \-_][0-9A-F]{4}[ \-_][0-9A-F]{4}")

    def parse_message(self, channel, name, tags, message):
        """Parse a message read from chat. This is the callback for the ChatListener.
        """
        s = self.code_re.search(message.upper())

        if(s is None):
            return
        else:
            code = message[s.start(): s.end()].upper().replace(" ", "-").replace("_", "-")
            self.level_list_model.add_level(code, name, tags)
