import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic

ui_file = uic.loadUiType("Week8-2시그널과슬롯사용하기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scrollbar.valueChanged.connect(self.lcd.display)
        self.button.clicked.connect(self.reset)
    
    def reset(self):
        self.scrollbar.setValue(0)
        
                
app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()