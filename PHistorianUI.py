# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PHistorian.ui'
#
# Created: Wed Feb 05 22:41:43 2014
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
        PHistorianUI.resize(553, 575)
        self.centralwidget = QtGui.QWidget(PHistorianUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.spinBoxSampleTime = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxSampleTime.setGeometry(QtCore.QRect(470, 100, 46, 22))
        self.spinBoxSampleTime.setObjectName(_fromUtf8("spinBoxSampleTime"))
        self.listWidgetTagList = QtGui.QListWidget(self.centralwidget)
        self.listWidgetTagList.setGeometry(QtCore.QRect(280, 30, 181, 191))
        self.listWidgetTagList.setObjectName(_fromUtf8("listWidgetTagList"))
        self.pushButtonStartDataCollection = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStartDataCollection.setGeometry(QtCore.QRect(340, 240, 121, 21))
        self.pushButtonStartDataCollection.setObjectName(_fromUtf8("pushButtonStartDataCollection"))
        self.dockWidget = QtGui.QDockWidget(self.centralwidget)
        self.dockWidget.setGeometry(QtCore.QRect(20, 30, 161, 181))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.pushButtonConnectOPC = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButtonConnectOPC.setGeometry(QtCore.QRect(20, 120, 75, 23))
        self.pushButtonConnectOPC.setObjectName(_fromUtf8("pushButtonConnectOPC"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidgetServers = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidgetServers.setGeometry(QtCore.QRect(10, 30, 141, 81))
        self.listWidgetServers.setObjectName(_fromUtf8("listWidgetServers"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.labelOPCServersList = QtGui.QLabel(self.centralwidget)
        self.labelOPCServersList.setGeometry(QtCore.QRect(470, 60, 61, 20))
        self.labelOPCServersList.setObjectName(_fromUtf8("labelOPCServersList"))
        PHistorianUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PHistorianUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PHistorianUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PHistorianUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PHistorianUI.setStatusBar(self.statusbar)

        self.retranslateUi(PHistorianUI)
        QtCore.QMetaObject.connectSlotsByName(PHistorianUI)

    def retranslateUi(self, PHistorianUI):
        PHistorianUI.setWindowTitle(_translate("PHistorianUI", "MainWindow", None))
        PHistorianUI.setStatusTip(_translate("PHistorianUI", "Not Connected", None))
        self.pushButtonStartDataCollection.setText(_translate("PHistorianUI", "start data collection", None))
        self.pushButtonConnectOPC.setText(_translate("PHistorianUI", "Connect", None))
        self.label.setText(_translate("PHistorianUI", "List of OPC Servers", None))
        self.labelOPCServersList.setText(_translate("PHistorianUI", "sample Time", None))

