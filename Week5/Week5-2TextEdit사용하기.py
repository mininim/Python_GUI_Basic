import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import uic 

ui_file = uic.loadUiType("Week5-2TextEdit사용하기.ui")[0]


class WindowClass(QMainWindow, ui_file):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.size = 12 
    
        self.button1.clicked.connect(self.changeFont)
        self.button2.clicked.connect(self.changeBlue)
        self.button3.clicked.connect(self.textClear)
        self.button4.clicked.connect(self.sizeUp)
        self.button5.clicked.connect(self.sizeDown)

    def changeFont(self):
        font = QtGui.QFont("Gulim",20)
        self.textEdit.setCurrentFont(font)
        
    def changeBlue(self):
        from PyQt5.QtCore import Qt
        self.textEdit.setTextColor(Qt.blue)
    
    def textClear(self):
        self.textEdit.clear()
        
    def sizeUp(self):
        self.size = self.size + 1
        self.textEdit.setFontPointSize(self.size)
        
    def sizeDown(self):
        self.size = self.size - 1
        self.textEdit.setFontPointSize(self.size)
        

       

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()




