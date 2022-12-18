import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5 import uic

ui_file = uic.loadUiType("Week8-3키보드와마우스시그널로슬롯만들기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.close()
        elif event.key() == Qt.Key_B:
            self.showFullScreen()
        elif event.key() == Qt.Key_C:
            self.showNormal()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        self.mouse.setText("x = {0} y = {1}".format(x,y))
        
    

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()