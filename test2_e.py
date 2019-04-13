# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2_e.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 379)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(36, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 411, 141))
        self.plainTextEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 57 italic 13pt \"URW Chancery L\";")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 6, 81, 31))
        self.label.setStyleSheet("font: 57 italic 18pt \"URW Chancery L\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 190, 231, 31))
        self.label_2.setStyleSheet("font: 57 italic 18pt \"URW Chancery L\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 260, 221, 31))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 57 italic 18pt \"URW Chancery L\";")
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(210, 230, 201, 26))
        self.spinBox.setStyleSheet("font: 57 italic 18pt \"URW Chancery L\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.spinBox.setObjectName("spinBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 300, 201, 25))
        self.lineEdit.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 57 italic 13pt \"URW Chancery L\";")
        self.lineEdit.setObjectName("lineEdit")
        self.goback = QtWidgets.QPushButton(Dialog)
        self.goback.setGeometry(QtCore.QRect(70, 350, 89, 25))
        self.goback.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.goback.setObjectName("goback")
        self.Runn = QtWidgets.QPushButton(Dialog)
        self.Runn.setGeometry(QtCore.QRect(210, 350, 89, 25))
        self.Runn.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Runn.setObjectName("Runn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "1) SIGHUP     2) SIGINT     3) SIGQUIT\n"
"4) SIGILL  5) SIGTRAP 6) SIGABRT\n"
"7) SIGBUS  8) SIGFPE  9) SIGKILL\n"
"10) SIGUSR1  11) SIGSEGV   12) SIGUSR2\n"
"13) SIGPIPE  14) SIGALRM  15) SIGTERM\n"
"16) SIGSTKFLT  17) SIGCHLD  18) SIGCONT\n"
"19) SIGSTOP  20) SIGTSTP  21) SIGTTIN\n"
"22) SIGTTOU  23) SIGURG  24) SIGXCPU\n"
"25) SIGXFSZ   26) SIGVTALRM  27) SIGPROF\n"
"28) SIGWINCH  29) SIGIO  30) SIGPWR\n"
"31) SIGSYS     34) SIGRTMIN  35) SIGRTMIN+1\n"
"36) SIGRTMIN+2  37) SIGRTMIN+3  38) SIGRTMIN+4\n"
"39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7\n"
"42) SIGRTMIN+8  43) SIGRTMIN+9  44) SIGRTMIN+10\n"
"45) SIGRTMIN+11  46) SIGRTMIN+12  47) SIGRTMIN+13\n"
"48) SIGRTMIN+14  49) SIGRTMIN+15  50) SIGRTMAX-14\n"
"51) SIGRTMAX-13  52) SIGRTMAX-12  53) SIGRTMAX-11\n"
"54) SIGRTMAX-10  55) SIGRTMAX-9  56) SIGRTMAX-8\n"
"57) SIGRTMAX-7  58) SIGRTMAX-6  59) SIGRTMAX-5\n"
"60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2\n"
"63) SIGRTMAX-1  64) SIGRTMAX"))
        self.label.setText(_translate("Dialog", "Signal :"))
        self.label_2.setText(_translate("Dialog", "Choose the num of signal :"))
        self.label_3.setText(_translate("Dialog", "Enter the process name :"))
        self.goback.setText(_translate("Dialog", "Go back"))
        self.Runn.setText(_translate("Dialog", "run"))


