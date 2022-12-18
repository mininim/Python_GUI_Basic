import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_file = uic.loadUiType("학생과제3주차.ui")[0]

class WindowClass(QMainWindow, ui_file) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.year = "연도"
        self.month = "월"
        self.date = "일"

        self.all.clicked.connect(self.all_check_click)
        self.one.stateChanged.connect(self.check_click)
        self.two.stateChanged.connect(self.check_click)
        self.three.stateChanged.connect(self.check_click)
        
        self.b.clicked.connect(self.button_click)

        self.y.activated[str].connect(self.select)
        self.m.activated[str].connect(self.select)
        self.d.activated[str].connect(self.select)
    
    def all_check_click(self) :
        if self.all.isChecked():
            self.one.setCheckState(2)
            self.two.setCheckState(2)
            self.three.setCheckState(2)
        
        if not self.all.isChecked() :
            self.one.setCheckState(0)
            self.two.setCheckState(0)
            self.three.setCheckState(0)
    
    def check_click(self) :
        if self.one.isChecked() and self.two.isChecked() and self.three.isChecked() :
            self.all.setCheckState(2)
        else :
            self.all.setCheckState(0)

    def select(self) :
        self.year = str(self.y.currentText())
        self.month = str(self.m.currentText())
        self.date = str(self.d.currentText())

    def button_click(self) :
        if self.one.isChecked() and self.two.isChecked() and self.three.isChecked() and self.year != "연도" and self.month != "월" and self.date != "일"  :
            print(self.year,"/",self.month,"/",self.date)
        else :
            print("실패")

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()