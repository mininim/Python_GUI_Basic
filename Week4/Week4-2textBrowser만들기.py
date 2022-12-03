import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser
from PyQt5 import uic

ui_file = uic.loadUiType("Week4-2textBrowser만들기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button1.clicked.connect(self.pythonPrint)
        self.button2.clicked.connect(self.browserPrint)
        self.button3.clicked.connect(self.browserClear)
        self.button4.clicked.connect(self.mission1)
        self.button5.clicked.connect(self.mission2)


    def pythonPrint(self):
        print(self.textBrowser.toPlainText())
    
    def browserPrint(self):
        self.textBrowser.setPlainText("나는 아이브코딩에 다니는 김코딩입니다")
    
    def browserClear(self):
        self.textBrowser.clear()
        
    def mission1(self):
        self.textBrowser.setPlainText("이름 / 나이 / 학교")
        
    def mission2(self):
        self.textBrowser.clear()
        print("모든 텍스트가 지워졌습니다")
        
        
    

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()

