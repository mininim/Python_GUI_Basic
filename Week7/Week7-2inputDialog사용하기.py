import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_file = uic.loadUiType("Week7-2inputDialog사용하기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.button1.clicked.connect(self.insert_name)
        self.button2.clicked.connect(self.insert_phone)
        self.button3.clicked.connect(self.delete)
        
    def insert_name(self):
        text, ok = QInputDialog.getText(self, '정보입력', '이름을 입력하세요: ')
        if ok :
            self.name.setText(str(text))
    
    def insert_phone(self):
        text, ok = QInputDialog.getText(self, '정보입력', '번호를 입력하세요: ')
        if ok :
            self.phone.setText(str(text))
    
    def delete(self):
        self.name.setText("")
        self.phone.setText("")
        
app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()