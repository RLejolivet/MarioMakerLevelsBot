# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue Dec 22 17:18:58 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.irc_info_tab = QtGui.QWidget()
        self.irc_info_tab.setObjectName("irc_info_tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.irc_info_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtGui.QWidget(self.irc_info_tab)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.channel_lineedit = QtGui.QLineEdit(self.widget)
        self.channel_lineedit.setObjectName("channel_lineedit")
        self.horizontalLayout.addWidget(self.channel_lineedit)
        self.verticalLayout_2.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(self.irc_info_tab)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.twitch_name_lineedit = QtGui.QLineEdit(self.groupBox)
        self.twitch_name_lineedit.setObjectName("twitch_name_lineedit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.twitch_name_lineedit)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.oauth_help_button = QtGui.QToolButton(self.widget_2)
        self.oauth_help_button.setObjectName("oauth_help_button")
        self.horizontalLayout_2.addWidget(self.oauth_help_button)
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.widget_2)
        self.twitch_oauth_lineedit = QtGui.QLineEdit(self.groupBox)
        self.twitch_oauth_lineedit.setEchoMode(QtGui.QLineEdit.Password)
        self.twitch_oauth_lineedit.setObjectName("twitch_oauth_lineedit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.twitch_oauth_lineedit)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.widget_6 = QtGui.QWidget(self.irc_info_tab)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.connect_button = QtGui.QPushButton(self.widget_6)
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout_6.addWidget(self.connect_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_6)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.irc_info_tab, "")
        self.levels_tab = QtGui.QWidget()
        self.levels_tab.setObjectName("levels_tab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.levels_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtGui.QWidget(self.levels_tab)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtGui.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.find_codes_checkbox = QtGui.QCheckBox(self.widget_3)
        self.find_codes_checkbox.setObjectName("find_codes_checkbox")
        self.verticalLayout_3.addWidget(self.find_codes_checkbox)
        self.hide_likely_fakes_checkbox = QtGui.QCheckBox(self.widget_3)
        self.hide_likely_fakes_checkbox.setObjectName("hide_likely_fakes_checkbox")
        self.verticalLayout_3.addWidget(self.hide_likely_fakes_checkbox)
        self.hide_potentially_checkbox = QtGui.QCheckBox(self.widget_3)
        self.hide_potentially_checkbox.setObjectName("hide_potentially_checkbox")
        self.verticalLayout_3.addWidget(self.hide_potentially_checkbox)
        self.subs_only_checkbox = QtGui.QCheckBox(self.widget_3)
        self.subs_only_checkbox.setObjectName("subs_only_checkbox")
        self.verticalLayout_3.addWidget(self.subs_only_checkbox)
        self.mods_only_checkbox = QtGui.QCheckBox(self.widget_3)
        self.mods_only_checkbox.setObjectName("mods_only_checkbox")
        self.verticalLayout_3.addWidget(self.mods_only_checkbox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.select_random_button = QtGui.QPushButton(self.widget_3)
        self.select_random_button.setObjectName("select_random_button")
        self.verticalLayout_3.addWidget(self.select_random_button)
        self.open_in_brower_button = QtGui.QPushButton(self.widget_3)
        self.open_in_brower_button.setObjectName("open_in_brower_button")
        self.verticalLayout_3.addWidget(self.open_in_brower_button)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.save_level_button = QtGui.QPushButton(self.widget_3)
        self.save_level_button.setObjectName("save_level_button")
        self.verticalLayout_3.addWidget(self.save_level_button)
        self.fake_level_button = QtGui.QPushButton(self.widget_3)
        self.fake_level_button.setObjectName("fake_level_button")
        self.verticalLayout_3.addWidget(self.fake_level_button)
        self.delete_level_button = QtGui.QPushButton(self.widget_3)
        self.delete_level_button.setObjectName("delete_level_button")
        self.verticalLayout_3.addWidget(self.delete_level_button)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.reset_levels_button = QtGui.QPushButton(self.widget_3)
        self.reset_levels_button.setObjectName("reset_levels_button")
        self.verticalLayout_3.addWidget(self.reset_levels_button)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.levels_tableView = QtGui.QTableView(self.levels_tab)
        self.levels_tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.levels_tableView.setAlternatingRowColors(True)
        self.levels_tableView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.levels_tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.levels_tableView.setSortingEnabled(True)
        self.levels_tableView.setObjectName("levels_tableView")
        self.levels_tableView.verticalHeader().setVisible(False)
        self.levels_tableView.verticalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_3.addWidget(self.levels_tableView)
        self.tabWidget.addTab(self.levels_tab, "")
        self.saved_tab = QtGui.QWidget()
        self.saved_tab.setObjectName("saved_tab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.saved_tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_4 = QtGui.QWidget(self.saved_tab)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtGui.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.delete_saved_button = QtGui.QPushButton(self.widget_4)
        self.delete_saved_button.setObjectName("delete_saved_button")
        self.verticalLayout_4.addWidget(self.delete_saved_button)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.reset_saved_button = QtGui.QPushButton(self.widget_4)
        self.reset_saved_button.setObjectName("reset_saved_button")
        self.verticalLayout_4.addWidget(self.reset_saved_button)
        self.horizontalLayout_4.addWidget(self.widget_4)
        self.saved_tableView = QtGui.QTableView(self.saved_tab)
        self.saved_tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.saved_tableView.setAlternatingRowColors(True)
        self.saved_tableView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.saved_tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.saved_tableView.setSortingEnabled(True)
        self.saved_tableView.setObjectName("saved_tableView")
        self.saved_tableView.verticalHeader().setVisible(False)
        self.saved_tableView.verticalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_4.addWidget(self.saved_tableView)
        self.tabWidget.addTab(self.saved_tab, "")
        self.fake_tab = QtGui.QWidget()
        self.fake_tab.setObjectName("fake_tab")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.fake_tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_5 = QtGui.QWidget(self.fake_tab)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtGui.QLabel(self.widget_5)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.delete_fake_button = QtGui.QPushButton(self.widget_5)
        self.delete_fake_button.setObjectName("delete_fake_button")
        self.verticalLayout_5.addWidget(self.delete_fake_button)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.reset_fakes_button = QtGui.QPushButton(self.widget_5)
        self.reset_fakes_button.setObjectName("reset_fakes_button")
        self.verticalLayout_5.addWidget(self.reset_fakes_button)
        self.horizontalLayout_5.addWidget(self.widget_5)
        self.fakes_tableView = QtGui.QTableView(self.fake_tab)
        self.fakes_tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.fakes_tableView.setAlternatingRowColors(True)
        self.fakes_tableView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.fakes_tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.fakes_tableView.setSortingEnabled(True)
        self.fakes_tableView.setObjectName("fakes_tableView")
        self.fakes_tableView.verticalHeader().setVisible(False)
        self.fakes_tableView.verticalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_5.addWidget(self.fakes_tableView)
        self.tabWidget.addTab(self.fake_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mario Maker Levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.channel_lineedit.setToolTip(QtGui.QApplication.translate("MainWindow", "The name of the channel to pull Mario Maker levels from", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Twitch account to connect to chat", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Oauth", None, QtGui.QApplication.UnicodeUTF8))
        self.oauth_help_button.setText(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.connect_button.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.irc_info_tab), QtGui.QApplication.translate("MainWindow", "Twich chat info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.find_codes_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Find codes from chat", None, QtGui.QApplication.UnicodeUTF8))
        self.hide_likely_fakes_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Hide levels on fakes list", None, QtGui.QApplication.UnicodeUTF8))
        self.hide_potentially_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Hide potentially fakes", None, QtGui.QApplication.UnicodeUTF8))
        self.subs_only_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Show levels from subs only", None, QtGui.QApplication.UnicodeUTF8))
        self.mods_only_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Show levels from mods only", None, QtGui.QApplication.UnicodeUTF8))
        self.select_random_button.setText(QtGui.QApplication.translate("MainWindow", "Select random", None, QtGui.QApplication.UnicodeUTF8))
        self.open_in_brower_button.setText(QtGui.QApplication.translate("MainWindow", "Open level in browser", None, QtGui.QApplication.UnicodeUTF8))
        self.save_level_button.setText(QtGui.QApplication.translate("MainWindow", "Add selected level(s) to saved list", None, QtGui.QApplication.UnicodeUTF8))
        self.fake_level_button.setText(QtGui.QApplication.translate("MainWindow", "Add selected level(s) to fakes list", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_level_button.setText(QtGui.QApplication.translate("MainWindow", "Delete selected level(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_levels_button.setText(QtGui.QApplication.translate("MainWindow", "Reset levels list", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.levels_tab), QtGui.QApplication.translate("MainWindow", "Levels List", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_saved_button.setText(QtGui.QApplication.translate("MainWindow", "Delete selected saved level(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_saved_button.setText(QtGui.QApplication.translate("MainWindow", "Reset saved list", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.saved_tab), QtGui.QApplication.translate("MainWindow", "Saved levels list", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_fake_button.setText(QtGui.QApplication.translate("MainWindow", "Delete selected fake level(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_fakes_button.setText(QtGui.QApplication.translate("MainWindow", "Reset fakes list", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fake_tab), QtGui.QApplication.translate("MainWindow", "Fake levels list", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

