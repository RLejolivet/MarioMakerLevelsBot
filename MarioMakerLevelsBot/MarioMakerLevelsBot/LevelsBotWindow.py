import re
import functools

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
        self.hide_likely_fakes_checkbox.stateChanged.connect(self.level_list_model.hide_fake_levels)
        self.hide_potentially_checkbox.stateChanged.connect(self.level_list_model.hide_potentially_fake_levels)
        self.subs_only_checkbox.stateChanged.connect(self.level_list_model.show_subs_levels_only)
        self.mods_only_checkbox.stateChanged.connect(self.level_list_model.show_mods_levels_only)

        self.delete_level_button.clicked.connect(functools.partial(self.delete_selected_slot, self.levels_tableView, self.level_list_model))
        self.reset_levels_button.clicked.connect(self.level_list_model.reset)

        # Saved list tab

        self.save_list_model = LevelListModel.LevelListModel()
        self.saved_tableView.setModel(self.save_list_model)
        self.saved_tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.delete_saved_button.clicked.connect(functools.partial(self.delete_selected_slot, self.saved_tableView, self.save_list_model))

        # Fake list tab
        self.fake_list_model = LevelListModel.LevelListModel()
        self.fakes_tableView.setModel(self.fake_list_model)
        self.fakes_tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.delete_fake_button.clicked.connect(functools.partial(self.delete_selected_slot, self.fakes_tableView, self.fake_list_model))

        # Back to levels list tab with the new models
        
        self.save_level_button.clicked.connect(functools.partial(self.move_selected_slot, self.save_list_model))
        self.fake_level_button.clicked.connect(functools.partial(self.move_selected_slot, self.fake_list_model))


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
        """Create a ChatListener and connect it to Twitch chat to start receiving messages.
        """
        if(self.chat_listener is None):
            self.chat_listener = ChatListener.ChatListener(
                self.twitch_name_lineedit.text(),
                self.twitch_oauth_lineedit.text(),
                map(lambda x: x.strip(), self.channel_lineedit.text().split(",")),
                self)

            self.chat_listener.wrong_password.connect(self.wrong_password_slot)
            self.chat_listener.connection_failed.connect(self.connection_failed_slot)
            self.chat_listener.connection_successful.connect(self.connection_successful_slot)

            self.chat_listener.start()

    def wrong_password_slot(self):
        """Slot connected to the "wrong password" signal that may be emitted by the ChatListener.
        """
        QtGui.QMessageBox.information(
            self,
            "Unable to connect to Twitch chat",
            "Unable to connect to Twitch chat\n"
            "Invalid Name/Password (OAuth) combination."""
            )

    def connection_failed_slot(self):
        """Slot connected to the "connection failed signal that may be emitted by the ChatListener."
        """
        QtGui.QMessageBox.information(
            self,
            "Unable to connect to Twitch chat",
            "Unable to connect to Twitch chat\n"
            "Make sure your internet connection doesn't restrict IRC."
            )

    def connection_successful_slot(self, channel):
        """Slot connected to the "connection successful that may be emitted by the ChatListener.
        
        Display a message confirming the connection as status bar not to force an extra click,
        and save the information for later.
        """
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

    # RegExp used to find codes. Pre-compiled to go faster when receiving messages.
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

    def move_selected_slot(self, target_model):
        """Transfer the selected levels in levels model to the target_model
        """
        selected_indexes = self.levels_tableView.selectionModel().selectedRows()

        for index in selected_indexes:
            row = index.row()
            level = self.level_list_model.data(index, LevelListModel.Level)
            target_model.add_level(level.code, level.name, level.tags)

        self.level_list_model.remove_indexes(selected_indexes)

    def delete_selected_slot(self, target_view, target_model):
        """Delete the selected levels in the target model.
        """
        selected_indexes = target_view.selectionModel().selectedRows()
        target_model.remove_indexes(selected_indexes)
