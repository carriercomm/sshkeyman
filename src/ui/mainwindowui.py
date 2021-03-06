# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtcreator/sshkeyman/mainwindow.ui'
#
# Created: Fri Jul  5 12:06:08 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        self.main_widget = QtGui.QWidget(main)
        self.main_widget.setObjectName(_fromUtf8("main_widget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.main_widget)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.main_splitter = QtGui.QSplitter(self.main_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_splitter.sizePolicy().hasHeightForWidth())
        self.main_splitter.setSizePolicy(sizePolicy)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setObjectName(_fromUtf8("main_splitter"))
        self.left_widget = QtGui.QWidget(self.main_splitter)
        self.left_widget.setObjectName(_fromUtf8("left_widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.left_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_2 = QtGui.QWidget(self.left_widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_key_button = QtGui.QToolButton(self.widget_2)
        self.add_key_button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("media/icon/16x16/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_key_button.setIcon(icon1)
        self.add_key_button.setAutoRaise(True)
        self.add_key_button.setObjectName(_fromUtf8("add_key_button"))
        self.horizontalLayout_3.addWidget(self.add_key_button)
        self.remove_key_button = QtGui.QToolButton(self.widget_2)
        self.remove_key_button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("media/icon/16x16/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_key_button.setIcon(icon2)
        self.remove_key_button.setAutoRaise(True)
        self.remove_key_button.setObjectName(_fromUtf8("remove_key_button"))
        self.horizontalLayout_3.addWidget(self.remove_key_button)
        self.verticalLayout.addWidget(self.widget_2)
        self.key_list = QtGui.QListWidget(self.left_widget)
        self.key_list.setObjectName(_fromUtf8("key_list"))
        self.verticalLayout.addWidget(self.key_list)
        self.right_widget = QtGui.QWidget(self.main_splitter)
        self.right_widget.setObjectName(_fromUtf8("right_widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.right_widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.right_widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.key_edit = QtGui.QTextEdit(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_edit.sizePolicy().hasHeightForWidth())
        self.key_edit.setSizePolicy(sizePolicy)
        self.key_edit.setReadOnly(True)
        self.key_edit.setAcceptRichText(False)
        self.key_edit.setObjectName(_fromUtf8("key_edit"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.server_tree = QtGui.QTreeWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.server_tree.sizePolicy().hasHeightForWidth())
        self.server_tree.setSizePolicy(sizePolicy)
        self.server_tree.setHeaderHidden(True)
        self.server_tree.setObjectName(_fromUtf8("server_tree"))
        self.horizontalLayout.addWidget(self.server_tree)
        self.verticalLayout_2.addWidget(self.splitter)
        self.button_widget = QtGui.QWidget(self.right_widget)
        self.button_widget.setObjectName(_fromUtf8("button_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.button_widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.rollback_button = QtGui.QPushButton(self.button_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("media/icon/16x16/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rollback_button.setIcon(icon3)
        self.rollback_button.setObjectName(_fromUtf8("rollback_button"))
        self.horizontalLayout_2.addWidget(self.rollback_button)
        self.commit_button = QtGui.QPushButton(self.button_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("media/icon/16x16/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commit_button.setIcon(icon4)
        self.commit_button.setObjectName(_fromUtf8("commit_button"))
        self.horizontalLayout_2.addWidget(self.commit_button)
        self.verticalLayout_2.addWidget(self.button_widget)
        self.vboxlayout.addWidget(self.main_splitter)
        main.setCentralWidget(self.main_widget)
        self.menuBar = QtGui.QMenuBar(main)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        main.setMenuBar(self.menuBar)
        self.action_import_key = QtGui.QAction(main)
        self.action_import_key.setIcon(icon1)
        self.action_import_key.setObjectName(_fromUtf8("action_import_key"))
        self.action_exit = QtGui.QAction(main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("media/icon/16x16/door.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit.setIcon(icon5)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_profiles = QtGui.QAction(main)
        self.action_profiles.setObjectName(_fromUtf8("action_profiles"))
        self.action_about = QtGui.QAction(main)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.menuFile.addAction(self.action_import_key)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_profiles)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_about)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "SSH key manager", None))
        self.add_key_button.setText(_translate("main", "...", None))
        self.remove_key_button.setText(_translate("main", "...", None))
        self.server_tree.headerItem().setText(0, _translate("main", "Server", None))
        self.rollback_button.setText(_translate("main", "Rollback", None))
        self.commit_button.setText(_translate("main", "Commit", None))
        self.menuFile.setTitle(_translate("main", "File", None))
        self.menuHelp.setTitle(_translate("main", "Help", None))
        self.action_import_key.setText(_translate("main", "Import &Key...", None))
        self.action_exit.setText(_translate("main", "E&xit", None))
        self.action_profiles.setText(_translate("main", "&Profiles...", None))
        self.action_about.setText(_translate("main", "About SSH key manager...", None))

