import re

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

        # Settings
        self.settings = QtCore.QSettings("user/settings.ini", QtCore.QSettings.IniFormat, self)
        self.channel_lineedit.setText(self.settings.value("irc_info/channel", ""))
        self.twitch_name_lineedit.setText(self.settings.value("irc_info/nick", ""))
        self.twitch_oauth_lineedit.setText(self.settings.value("irc_info/oauth", ""))

        # Menu bar
        self.actionAbout.triggered.connect(self.about)

        # IRC info tab

        self.chat_listener = None
        self.oauth_help_button.clicked.connect(self.oauth_help)
        self.connect_button.clicked.connect(self.connect)

        # Levels list tab

        self.level_list_model = LevelListModel.LevelListModel()
        self.levels_tableView.setModel(self.level_list_model)
        self.levels_tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.find_codes_checkbox.stateChanged.connect(self.toggle_check_codes)


    ###########################################################################
    # Menu bar
    ###########################################################################

    def about(self):
        """Display a messagebox with some information about the program.
        """
        QtGui.QMessageBox.about(
            self,
            "Simple IRC bot for Twitch created by Laraeph",
            "Simple IRC bot for Twitch created by Laraeph\n"
            "Pull Mario Maker Level Codes from chat easily!\n"
            "Howto use: http://mentor2.dyndns.org/Laraeph/MarioMakerBot\n"
            "Or: https://github.com/RLejolivet/MarioMakerLevelsBot\n"
            "\n"
            "Contact me for questions, evolution requests:\n"
            "twitch.tv/laraeph\n"
            "twitter.com/LaraephFR\n"
            "laraephddo@gmail.com\n")


    ###########################################################################
    # IRC info tab
    ###########################################################################

    def oauth_help(self):
        """Display a messagebox with some information about the required OAuth.
        """
        QtGui.QMessageBox.about(
            self,
            "OAuth help",
            "This is the OAuth of your bot account, to connect to Twitch\n"
            "To obtain it:\n"
            "    - Log on the bot account on Twitch\n"
            "    - Go to http://twitchapps.com/tmi/\n"
            "    - Connect with Twitch\n"
            "    - Accept\n"
            "    - Copy and paste the OAuth given in the box\n"
            "\n"
            "More information can be found at http://help.twitch.tv/customer/portal/articles/1302780-twitch-irc\n"
        )

    def connect(self):
        if(self.chat_listener is None):
            self.chat_listener = ChatListener.ChatListener(
                self.twitch_name_lineedit.text(),
                self.twitch_oauth_lineedit.text(),
                self.channel_lineedit.text(),
                self)

            self.chat_listener.wrong_password.connect(self.wrong_password_slot)
            self.chat_listener.connection_failed.connect(self.connection_failed_slot)
            self.chat_listener.connection_successful.connect(self.connection_successful_slot)

            self.chat_listener.start()

    def wrong_password_slot(self):
        QtGui.QMessageBox.information(
            self,
            "Unable to connect to Twitch chat",
            "Unable to connect to Twitch chat\n"
            "Invalid Name/Password (OAuth) combination."""
            )

    def connection_failed_slot(self):
        QtGui.QMessageBox.information(
            self,
            "Unable to connect to Twitch chat",
            "Unable to connect to Twitch chat\n"
            "Make sure your internet connection doesn't restrict IRC."
            )

    def connection_successful_slot(self, channel):
        self.statusbar.showMessage("Successfully connected to channel {}".format(channel))
        self.settings.setValue("irc_info/channel", self.channel_lineedit.text())
        self.settings.setValue("irc_info/nick", self.twitch_name_lineedit.text())
        self.settings.setValue("irc_info/oauth", self.twitch_oauth_lineedit.text())

    ###########################################################################
    # Levels list tab
    ###########################################################################

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
