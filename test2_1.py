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
        Dialog.setStyleSheet("")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(70, 40, 211, 25))
        self.comboBox.setStyleSheet("font: 11pt \"Sans\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 181, 21))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 40, 61, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "List all the processes"))
        self.comboBox.setItemText(1, _translate("Dialog", "List all the processes grouped by user"))
        self.comboBox.setItemText(2, _translate("Dialog", "Display process ID of all the processes"))
        self.comboBox.setItemText(3, _translate("Dialog", "Run/stop a specific process"))
        self.comboBox.setItemText(4, _translate("Dialog", "Send specific signals to specific process"))
        self.label.setText(_translate("Dialog", "Choose a command :"))
        self.pushButton.setText(_translate("Dialog", "Run"))


