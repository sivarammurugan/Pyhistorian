# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PYHistorian.ui'
#
# Created: Sat Feb 08 00:41:18 2014
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_PHistorianUI(object):
    def setupUi(self, PHistorianUI):
        PHistorianUI.setObjectName(_fromUtf8("PHistorianUI"))
        PHistorianUI.resize(646, 575)
        self.centralwidget = QtGui.QWidget(PHistorianUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 624, 483))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scrollArea_2 = QtGui.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 602, 461))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.listWidgetTagList = QtGui.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidgetTagList.setGeometry(QtCore.QRect(10, 90, 181, 351))
        self.listWidgetTagList.setObjectName(_fromUtf8("listWidgetTagList"))
        self.listWidgetTagList_2 = QtGui.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidgetTagList_2.setGeometry(QtCore.QRect(400, 100, 181, 351))
        self.listWidgetTagList_2.setObjectName(_fromUtf8("listWidgetTagList_2"))
        self.spinBoxSampleTime = QtGui.QSpinBox(self.scrollAreaWidgetContents_2)
        self.spinBoxSampleTime.setGeometry(QtCore.QRect(210, 160, 46, 22))
        self.spinBoxSampleTime.setObjectName(_fromUtf8("spinBoxSampleTime"))
        self.labelOPCServersList = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.labelOPCServersList.setGeometry(QtCore.QRect(200, 130, 61, 20))
        self.labelOPCServersList.setObjectName(_fromUtf8("labelOPCServersList"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setGeometry(QtCore.QRect(280, 160, 91, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 210, 91, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(400, 70, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea_3 = QtGui.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 0, 606, 465))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 602, 461))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.listWidgetOPCTags = QtGui.QListWidget(self.scrollAreaWidgetContents_3)
        self.listWidgetOPCTags.setGeometry(QtCore.QRect(10, 90, 181, 351))
        self.listWidgetOPCTags.setObjectName(_fromUtf8("listWidgetOPCTags"))
        self.listWidgetPYTags = QtGui.QListWidget(self.scrollAreaWidgetContents_3)
        self.listWidgetPYTags.setGeometry(QtCore.QRect(400, 100, 181, 351))
        self.listWidgetPYTags.setObjectName(_fromUtf8("listWidgetPYTags"))
        self.spinBoxSampleTime_2 = QtGui.QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBoxSampleTime_2.setGeometry(QtCore.QRect(210, 160, 46, 22))
        self.spinBoxSampleTime_2.setObjectName(_fromUtf8("spinBoxSampleTime_2"))
        self.labelOPCServersList_2 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.labelOPCServersList_2.setGeometry(QtCore.QRect(200, 130, 61, 20))
        self.labelOPCServersList_2.setObjectName(_fromUtf8("labelOPCServersList_2"))
        self.labelOPCServer = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.labelOPCServer.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.labelOPCServer.setObjectName(_fromUtf8("labelOPCServer"))
        self.pushButtonAddTags = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButtonAddTags.setGeometry(QtCore.QRect(280, 160, 91, 21))
        self.pushButtonAddTags.setObjectName(_fromUtf8("pushButtonAddTags"))
        self.pushButtonRemoveTags = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButtonRemoveTags.setGeometry(QtCore.QRect(280, 210, 91, 21))
        self.pushButtonRemoveTags.setObjectName(_fromUtf8("pushButtonRemoveTags"))
        self.labelPYHistorian = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.labelPYHistorian.setGeometry(QtCore.QRect(410, 80, 81, 16))
        self.labelPYHistorian.setObjectName(_fromUtf8("labelPYHistorian"))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        PHistorianUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PHistorianUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        PHistorianUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PHistorianUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PHistorianUI.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(PHistorianUI)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        PHistorianUI.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionStartCollect = QtGui.QAction(PHistorianUI)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Start-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStartCollect.setIcon(icon)
        self.actionStartCollect.setObjectName(_fromUtf8("actionStartCollect"))
        self.actionStopCollect = QtGui.QAction(PHistorianUI)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Stop-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStopCollect.setIcon(icon1)
        self.actionStopCollect.setObjectName(_fromUtf8("actionStopCollect"))
        self.actionOPC_Servers = QtGui.QAction(PHistorianUI)
        self.actionOPC_Servers.setObjectName(_fromUtf8("actionOPC_Servers"))
        self.actionConnect = QtGui.QAction(PHistorianUI)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("//tsclient/C/Users/40003845/Downloads/Actions-network-connect-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon2)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionOPC_Server_Settings = QtGui.QAction(PHistorianUI)
        self.actionOPC_Server_Settings.setObjectName(_fromUtf8("actionOPC_Server_Settings"))
        self.menuFile.addAction(self.actionStartCollect)
        self.menuView.addAction(self.actionOPC_Servers)
        self.menuSettings.addAction(self.actionOPC_Server_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionStartCollect)
        self.toolBar.addAction(self.actionStopCollect)

        self.retranslateUi(PHistorianUI)
        QtCore.QMetaObject.connectSlotsByName(PHistorianUI)

    def retranslateUi(self, PHistorianUI):
        PHistorianUI.setWindowTitle(_translate("PHistorianUI", "PYHistoiran", None))
        PHistorianUI.setStatusTip(_translate("PHistorianUI", "Not Connected", None))
        self.labelOPCServersList.setText(_translate("PHistorianUI", "sample Time", None))
        self.label.setText(_translate("PHistorianUI", "OPC Server Tags", None))
        self.pushButton.setText(_translate("PHistorianUI", "Add tags ->", None))
        self.pushButton_2.setText(_translate("PHistorianUI", "<--Remove Tags ", None))
        self.label_2.setText(_translate("PHistorianUI", "OPC Server Tags", None))
        self.labelOPCServersList_2.setText(_translate("PHistorianUI", "sample Time", None))
        self.labelOPCServer.setText(_translate("PHistorianUI", "OPC Server Tags", None))
        self.pushButtonAddTags.setText(_translate("PHistorianUI", "Add tags ->", None))
        self.pushButtonRemoveTags.setText(_translate("PHistorianUI", "<--Remove Tags ", None))
        self.labelPYHistorian.setText(_translate("PHistorianUI", "PYHistorian Tags", None))
        self.menuFile.setTitle(_translate("PHistorianUI", "File", None))
        self.menuView.setTitle(_translate("PHistorianUI", "View", None))
        self.menuHelp.setTitle(_translate("PHistorianUI", "Help", None))
        self.menuSettings.setTitle(_translate("PHistorianUI", "Settings", None))
        self.toolBar.setWindowTitle(_translate("PHistorianUI", "toolBar", None))
        self.actionStartCollect.setText(_translate("PHistorianUI", "startCollect", None))
        self.actionStartCollect.setToolTip(_translate("PHistorianUI", "start Dat Collection", None))
        self.actionStopCollect.setText(_translate("PHistorianUI", "actionStopCollect", None))
        self.actionOPC_Servers.setText(_translate("PHistorianUI", "OPC Servers", None))
        self.actionConnect.setText(_translate("PHistorianUI", "connect OPC", None))
        self.actionOPC_Server_Settings.setText(_translate("PHistorianUI", "OPC Server Settings", None))
