# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.A_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.A_checkBox.setGeometry(QtCore.QRect(160, 60, 92, 23))
        self.A_checkBox.setObjectName("A_checkBox")
        self.B_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.B_checkBox.setGeometry(QtCore.QRect(160, 110, 92, 23))
        self.B_checkBox.setObjectName("B_checkBox")
        self.C_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.C_checkBox.setGeometry(QtCore.QRect(160, 160, 92, 23))
        self.C_checkBox.setObjectName("C_checkBox")
        self.checkBoxs =[self.A_checkBox,self.B_checkBox,self.C_checkBox]
        self.label = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 290, 300, 300))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.start_process())
        #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 220, 89, 25))
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.pressed.connect(self.start_process)
        self.Select_all_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Select_all_checkBox.setGeometry(QtCore.QRect(140, 220, 92, 23))
        self.Select_all_checkBox.setObjectName("Select_all_checkBox")
        self.Select_all_checkBox.stateChanged.connect(self.on_stateChange)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.A_checkBox.setText(_translate("MainWindow", "A"))
        self.B_checkBox.setText(_translate("MainWindow", "B"))
        self.C_checkBox.setText(_translate("MainWindow", "C"))
        self.label.appendPlainText(_translate("MainWindow", "Text"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.Select_all_checkBox.setText(_translate("MainWindow", "Select ALL"))

    def on_stateChange(self,state):
        # print(self.checkBoxs)
        for checkBox in self.checkBoxs:
            checkBox.setCheckState(state)


    # def checked(self):
    #     if self.A_checkBox.isChecked()==True:
    #         self.A= 1
    #     else:
    #         self.A=0 
    #     if self.B_checkBox.isChecked()==True:
    #         self.B= 2
    #     else:
    #         self.B=0
    #     if self.C_checkBox.isChecked()==True:
    #         self.C= 3
    #     else:
    #         self.C=0           
    #     # self.label.setText(f'{self.A}{self.B}{self.C}')
    #     self.label.setText(str(self.A+self.B+self.C))
    #     # self.label.setText("Clicked")  
        # 
        # 
        # 
        # 

    def message(self, s):
        self.label.appendPlainText(s)

    def start_process(self):
        self.p = None
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QtCore.QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("python", ['8t8r_dl.py'])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QtCore.QProcess.NotRunning: 'Not running',
            QtCore.QProcess.Starting: 'Starting',
            QtCore.QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
