# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PHistorian.ui'
#
# Created: Fri Feb 07 03:20:08 2014
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
        self.dockWidget = QtGui.QDockWidget(self.scrollAreaWidgetContents)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.pushButtonConnectOPC = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButtonConnectOPC.setGeometry(QtCore.QRect(20, 190, 75, 23))
        self.pushButtonConnectOPC.setObjectName(_fromUtf8("pushButtonConnectOPC"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidgetServers = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidgetServers.setGeometry(QtCore.QRect(20, 30, 201, 111))
        self.listWidgetServers.setObjectName(_fromUtf8("listWidgetServers"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout_2.addWidget(self.dockWidget)
        self.scrollArea_2 = QtGui.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 296, 461))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.listWidgetTagList = QtGui.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidgetTagList.setGeometry(QtCore.QRect(10, 110, 361, 351))
        self.listWidgetTagList.setObjectName(_fromUtf8("listWidgetTagList"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 120, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.labelOPCServersList = QtGui.QLabel(self.groupBox)
        self.labelOPCServersList.setGeometry(QtCore.QRect(20, 20, 61, 20))
        self.labelOPCServersList.setObjectName(_fromUtf8("labelOPCServersList"))
        self.spinBoxSampleTime = QtGui.QSpinBox(self.groupBox)
        self.spinBoxSampleTime.setGeometry(QtCore.QRect(20, 50, 46, 22))
        self.spinBoxSampleTime.setObjectName(_fromUtf8("spinBoxSampleTime"))
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
        PHistorianUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PHistorianUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PHistorianUI.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(PHistorianUI)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        PHistorianUI.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        PHistorianUI.insertToolBarBreak(self.toolBar)
        self.actionStartCollect = QtGui.QAction(PHistorianUI)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Start-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStartCollect.setIcon(icon)
        self.actionStartCollect.setObjectName(_fromUtf8("actionStartCollect"))
        self.actionActionStopCollect = QtGui.QAction(PHistorianUI)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Stop-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionActionStopCollect.setIcon(icon1)
        self.actionActionStopCollect.setObjectName(_fromUtf8("actionActionStopCollect"))
        self.actionOPC_Servers = QtGui.QAction(PHistorianUI)
        self.actionOPC_Servers.setObjectName(_fromUtf8("actionOPC_Servers"))
        self.menuFile.addAction(self.actionStartCollect)
        self.menuView.addAction(self.actionOPC_Servers)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStartCollect)
        self.toolBar.addAction(self.actionActionStopCollect)

        self.retranslateUi(PHistorianUI)
        QtCore.QMetaObject.connectSlotsByName(PHistorianUI)

    def retranslateUi(self, PHistorianUI):
        PHistorianUI.setWindowTitle(_translate("PHistorianUI", "MainWindow", None))
        PHistorianUI.setStatusTip(_translate("PHistorianUI", "Not Connected", None))
        self.pushButtonConnectOPC.setText(_translate("PHistorianUI", "Connect", None))
        self.label.setText(_translate("PHistorianUI", "List of OPC Servers", None))
        self.groupBox.setTitle(_translate("PHistorianUI", "GroupBox", None))
        self.labelOPCServersList.setText(_translate("PHistorianUI", "sample Time", None))
        self.menuFile.setTitle(_translate("PHistorianUI", "File", None))
        self.menuView.setTitle(_translate("PHistorianUI", "View", None))
        self.menuHelp.setTitle(_translate("PHistorianUI", "Help", None))
        self.toolBar.setWindowTitle(_translate("PHistorianUI", "toolBar", None))
        self.actionStartCollect.setText(_translate("PHistorianUI", "startCollect", None))
        self.actionStartCollect.setToolTip(_translate("PHistorianUI", "start Dat Collection", None))
        self.actionActionStopCollect.setText(_translate("PHistorianUI", "actionStopCollect", None))
        self.actionOPC_Servers.setText(_translate("PHistorianUI", "OPC Servers", None))


