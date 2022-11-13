import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

ui_file = uic.loadUiType("Week1-3도형그리기.ui")[0]

class WindowClass(QMainWindow, ui_file): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def paintEvent(self, event): 
        paint = QPainter()
        paint.begin(self)
        self.drawFigure(paint)

    def drawFigure(self, paint):
        pen = QPen(Qt.green, 10)
        paint.setBrush(Qt.blue)
        paint.setPen(pen)
        paint.drawRect(100, 100, 150, 150)
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


