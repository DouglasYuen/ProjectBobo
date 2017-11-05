# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_v3SQ.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 550)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 700))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.labelSelections = QtWidgets.QLabel(self.centralWidget)
        self.labelSelections.setGeometry(QtCore.QRect(540, 10, 170, 30))
        self.labelSelections.setObjectName("labelSelections")
        self.clearAllButton = QtWidgets.QPushButton(self.centralWidget)
        self.clearAllButton.setGeometry(QtCore.QRect(310, 453, 225, 32))
        self.clearAllButton.setObjectName("clearAllButton")
        self.printButton = QtWidgets.QPushButton(self.centralWidget)
        self.printButton.setGeometry(QtCore.QRect(540, 425, 400, 60))
        self.printButton.setMaximumSize(QtCore.QSize(589, 16777215))
        self.printButton.setObjectName("printButton")
        self.labelConditions = QtWidgets.QLabel(self.centralWidget)
        self.labelConditions.setGeometry(QtCore.QRect(10, 10, 141, 30))
        self.labelConditions.setObjectName("labelConditions")
        self.conditionsViewer = QtWidgets.QColumnView(self.centralWidget)
        self.conditionsViewer.setGeometry(QtCore.QRect(10, 70, 520, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.conditionsViewer.setFont(font)
        self.conditionsViewer.setObjectName("conditionsViewer")
        self.addButtonCondition = QtWidgets.QPushButton(self.centralWidget)
        self.addButtonCondition.setGeometry(QtCore.QRect(10, 425, 150, 60))
        self.addButtonCondition.setObjectName("addButtonCondition")
        self.AlphaBox = QtWidgets.QLineEdit(self.centralWidget)
        self.AlphaBox.setGeometry(QtCore.QRect(10, 40, 520, 22))
        self.AlphaBox.setObjectName("AlphaBox")
        self.MainConditionList = QtWidgets.QListWidget(self.centralWidget)
        self.MainConditionList.setGeometry(QtCore.QRect(540, 40, 192, 380))
        self.MainConditionList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.MainConditionList.setObjectName("MainConditionList")
        self.removeButton = QtWidgets.QPushButton(self.centralWidget)
        self.removeButton.setGeometry(QtCore.QRect(310, 425, 225, 32))
        self.removeButton.setObjectName("removeButton")
        self.SubConditionList = QtWidgets.QListWidget(self.centralWidget)
        self.SubConditionList.setGeometry(QtCore.QRect(743, 40, 192, 380))
        self.SubConditionList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.SubConditionList.setObjectName("SubConditionList")
        self.addButtonSubCondition = QtWidgets.QPushButton(self.centralWidget)
        self.addButtonSubCondition.setGeometry(QtCore.QRect(160, 425, 150, 60))
        self.addButtonSubCondition.setObjectName("addButtonSubCondition")
        self.labelSelections_2 = QtWidgets.QLabel(self.centralWidget)
        self.labelSelections_2.setGeometry(QtCore.QRect(750, 10, 170, 30))
        self.labelSelections_2.setObjectName("labelSelections_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSelections.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Main Condition</span></p></body></html>"))
        self.clearAllButton.setText(_translate("MainWindow", "Clear all"))
        self.printButton.setText(_translate("MainWindow", "Print"))
        self.labelConditions.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Bobo Library</span></p></body></html>"))
        self.addButtonCondition.setText(_translate("MainWindow", "Add to Condition"))
        self.removeButton.setText(_translate("MainWindow", "Remove From List"))
        self.addButtonSubCondition.setText(_translate("MainWindow", "Add to Subcondition"))
        self.labelSelections_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Subcondition</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

