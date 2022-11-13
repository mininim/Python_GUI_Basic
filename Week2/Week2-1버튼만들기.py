import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic


ui_file = uic.loadUiType("Week2-1버튼만들기.ui")[0]

class WindowClass(QMainWindow, ui_file): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button1.clicked.connect(self.button1_Click)
        self.button2.clicked.connect(self.button2_Click)
        self.button3.clicked.connect(self.button3_Click)

    
    def button1_Click(self):
        print("나는 강아지를 키워")

    def button2_Click(self):
        print("나는 고양이를 키워")
    
    def button3_Click(self):
        print("나는 토끼를 키워")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


