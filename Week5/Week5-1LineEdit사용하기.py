import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

ui_file = uic.loadUiType("Week5-1LineEdit사용하기.ui")[0]
push = 0 

class WindowClass(QMainWindow, ui_file):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button1.clicked.connect(self.button_click)
    
    def button_click(self):
        global push
        push = push + 1
        if self.lineEdit.text()== "토끼":
            self.label4.setText(self.lineEdit.text()+"는 정답 입니다")
        elif push == 1:
            self.label2.setText("내 눈은 빨간색이에요")
            self.label4.setText(self.lineEdit.text()+"는 정답이 아닙니다")
        else:
            self.label3.setText("나는 하얗고 긴 귀를 가졌어요")
            self.label4.setText(self.lineEdit.text()+"는 답이 아닙니다")



app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()




