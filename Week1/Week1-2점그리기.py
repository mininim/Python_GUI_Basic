import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

import random

ui_file = uic.loadUiType("Week1-2점그리기.ui")[0]

class WindowClass(QMainWindow, ui_file): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        self.drawRandomPoint(paint)
        paint.end()
    
    def drawRandomPoint(self, paint):
        pen = QPen()
        pen.setColor(Qt.red)
        size = self.size()

        for i in range(1, 20):
            pen.setWidth(random.randint(10, 50))
            paint.setPen(pen)
            pen_x = random.randint(1, size.width() - 1)
            pen_y = random.randint(1, size.height() - 1)
            paint.drawPoint(pen_x, pen_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()