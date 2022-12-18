import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 
from PyQt5.uic.uiparser import ButtonGroup

ui_file = uic.loadUiType("Week6-1GroupBox만들기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.button1.clicked.connect(self.button_click)
        self.radio1.clicked.connect(self.radio_click)
        self.check1.stateChanged.connect(self.check_click)

        self.groupBox2.setCheckable(True)
        self.groupBox2.setChecked(False)
        
        
    def button_click(self):
        self.label1.setText("버튼 그룹")
        self.label2.setText("버튼1")

    def radio_click(self):
        if self.radio1.isChecked():
            self.label1.setText("라디오버튼 그룹")
            self.label2.setText("라디오버튼1")
    
    def check_click(self):
        if self.check1.isChecked():
            self.label1.setText("체크박스그룹")
            self.label2.setText("체크박스1")
    
    
app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()