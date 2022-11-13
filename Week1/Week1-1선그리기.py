import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

ui_file = uic.loadUiType("Week1-1선그리기.ui")[0]

class WindowClass(QMainWindow, ui_file): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def paintEvent(self, event): 
        paint = QPainter()
        paint.begin(self)
        self.drawLine(paint)

    def drawLine(self, paint):
        pen = QPen(Qt.red, 5, Qt.SolidLine)
        paint.setPen(pen)
        paint.drawLine(100, 50, 700, 50)

        pen.setColor(Qt.yellow)
        pen.setStyle(Qt.DashLine)
        paint.setPen(pen)
        paint.drawLine(100, 100, 700, 100)

        pen = QPen(Qt.green, 5, Qt.SolidLine)
        paint.setPen(pen)
        paint.drawLine(100, 150, 700, 150)

        pen.setColor(Qt.yellow)
        pen.setStyle(Qt.DashLine)
        paint.setPen(pen)
        paint.drawLine(100, 200, 700, 200)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


