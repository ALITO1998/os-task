# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2_d.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 95)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(36, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 211, 17))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255));\n"
"font: 57 italic 18pt \"URW Chancery L\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.Run = QtWidgets.QPushButton(Dialog)
        self.Run.setGeometry(QtCore.QRect(310, 10, 89, 25))
        self.Run.setStyleSheet("color: rgb(164, 0, 0);")
        self.Run.setObjectName("Run")
        self.goback = QtWidgets.QPushButton(Dialog)
        self.goback.setGeometry(QtCore.QRect(310, 40, 89, 25))
        self.goback.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.goback.setObjectName("goback")
        self.textbox = QtWidgets.QLineEdit(Dialog)
        self.textbox.setGeometry(QtCore.QRect(100, 40, 201, 25))
        self.textbox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255));")
        self.textbox.setObjectName("textbox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter the process name :"))
        self.Run.setText(_translate("Dialog", "Run"))
        self.goback.setText(_translate("Dialog", "Go Back"))


