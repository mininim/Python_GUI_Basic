import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic

ui_file = uic.loadUiType("Week8-1시그널과슬롯이해하기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.num_1 = 0
        self.num_2 = 0
        
        self.button1.clicked.connect(self.click)
        self.button2.clicked.connect(self.click)
        
    def click(self):
        button = self.sender()
        if button.text() == "버튼1":
            self.num_1 = self.num_1 + 1
            self.label.setText(button.text() + "이 " + f"{self.num_1}번 눌렸습니다." )
        
        else :
            self.num_2 = self.num_2 + 1
            self.label.setText(button.text() + "가 " + f"{self.num_2}번 눌렸습니다." )    
            
                
app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()