import os
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class main(QDialog):
    def __init__(self):
        super(main,self).__init__()
        loadUi('test2.ui',self)
        self.pushButton.clicked.connect(self.run)
        

    def run(self):
        x = self.comboBox.currentText()
        if (x == "ps"):
            self.dialog = socand()
        if (x == "List all the processes grouped by user"):
            self.dialog = theard()
        if (x == "Display process ID of all the processes"):
            self.dialog = fifth()    
        if (x == "Run/stop a specific process"):
            self.dialog = fuorth()
        if (x == "Send specific signals to specific process"):
            self.dialog = frist()
        
        self.dialog.exec_()

class fifth(QDialog):
    def __init__(self):
        super(fifth,self).__init__()
        loadUi('test2_c_r.ui',self)
        x = os.uname()[1]
        if ("-VirtualBox" in x):
            a = x.index("-VirtualBox")
            x = x[:a]
        result = os.popen("pgrep -u"+x+" -l").read()
        self.plainTextEdit.insertPlainText(result)
        self.pushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.close()

class fuorth(QDialog):
    def __init__(self):
        super(fuorth,self).__init__()
        loadUi('test2_d.ui',self)
        self.goback.clicked.connect(self.go_back)
        self.Run.clicked.connect(self.run)


    def go_back(self):
        self.close()

    def run(self):
        a = self.textbox.text()
        e = os.popen("pkill -9 "+a)
        self.dialog = fuorth_r()
        self.close()
        self.dialog.exec_()


class fuorth_r(QDialog):
    def __init__(self):
        super(fuorth_r,self).__init__()
        loadUi('test2_d_r.ui',self)
        self.goback.clicked.connect(self.go_back)

    def go_back(self):
        self.close()


class socand(QDialog):
    def __init__(self):
        super(socand,self).__init__()
        loadUi('test2_a_r.ui',self)
        result = os.popen("ps").read()
        self.plainTextEdit.insertPlainText(result)
        self.pushButton.clicked.connect(self.go_back)


    def go_back(self):
        self.close()


class theard(QDialog):
    def __init__(self):
        super(theard,self).__init__()
        loadUi('test2_b.ui',self)
        self.goback.clicked.connect(self.go_back)
        self.Run.clicked.connect(self.run)
        
         

    def go_back(self):
        self.close()

    def run(self):
        self.dialog = theard_r()
        self.dialog.exec_()
        self.close()

class theard_r(theard):
    def __init__(self, parent = theard):
        super(theard_r,self).__init__()
        loadUi('test2_b_r.ui',self)
        a = self.textbox.text()
        q = os.popen("ps -u"+a).read()
        self.plainTextEdit.insertPlainText(q)
        self.pushButton.clicked.connect(self.go_back)


    def go_back(self):
        self.close()

class frist(QDialog):
    def __init__(self):
        super(frist,self).__init__()
        loadUi('test2_e.ui',self)
        self.goback.clicked.connect(self.go_back)
        self.Runn.clicked.connect(self.run)
        self.spinBox.setMaximum(64)
        
    def run(self):
        a = self.spinBox.value()
        b = self.lineEdit.text()
        c = os.popen("pkill -"+str(a)+" "+b)
        self.dialog = fuorth_r()
        self.close()
        self.dialog.exec_()
    
    def go_back(self):
        self.close()

app = QApplication(sys.argv)
widget = main()
widget.show()
sys.exit(app.exec_())
