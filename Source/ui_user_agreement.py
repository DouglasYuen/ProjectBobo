# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_agreement_window.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userAgreement(object):
    def setupUi(self, userAgreement):

        self.newWindow = None

        userAgreement.setObjectName("userAgreement")
        userAgreement.resize(431, 505)
        userAgreement.setMinimumSize(QtCore.QSize(400, 300))
        userAgreement.setMaximumSize(QtCore.QSize(800, 600))
        self.centralWidget = QtWidgets.QWidget(userAgreement)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 391, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.agreeButton = QtWidgets.QPushButton(self.centralWidget)
        self.agreeButton.setGeometry(QtCore.QRect(270, 430, 101, 41))
        self.agreeButton.setObjectName("agreeButton")
        self.declineButton = QtWidgets.QPushButton(self.centralWidget)
        self.declineButton.setGeometry(QtCore.QRect(60, 430, 101, 41))
        self.declineButton.setObjectName("declineButton")
        userAgreement.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(userAgreement)
        self.statusBar.setObjectName("statusBar")
        userAgreement.setStatusBar(self.statusBar)

        self.retranslateUi(userAgreement)
        QtCore.QMetaObject.connectSlotsByName(userAgreement)

    def retranslateUi(self, userAgreement):
        _translate = QtCore.QCoreApplication.translate
        userAgreement.setWindowTitle(_translate("userAgreement", "MainWindow"))
        self.agreeButton.setText(_translate("userAgreement", "I Agree"))
        self.declineButton.setText(_translate("userAgreement", "Decline"))

