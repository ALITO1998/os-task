# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 90)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(36, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 40, 171, 25))
        self.comboBox.setStyleSheet("font: italic 11pt \"URW Bookman L\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("ps")
        self.comboBox.addItem("List all the processes grouped by user")
        self.comboBox.addItem("Display process ID of all the processes")
        self.comboBox.addItem("Run/stop a specific process")
        self.comboBox.addItem("Send specific signals to specific process")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 181, 21))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255));\n"
"font: 57 italic 18pt \"URW Chancery L\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 40, 61, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "ps"))
        self.comboBox.setItemText(1, _translate("Dialog", "List all the processes grouped by user"))
        self.comboBox.setItemText(2, _translate("Dialog", "Display process ID of all the processes"))
        self.comboBox.setItemText(3, _translate("Dialog", "Run/stop a specific process"))
        self.comboBox.setItemText(4, _translate("Dialog", "Send specific signals to specific process"))
        self.label.setText(_translate("Dialog", "Choose a command :"))
        self.pushButton.setText(_translate("Dialog", "Run"))


