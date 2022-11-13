import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5 import uic
from PyQt5.QtCore import Qt

ui_file = uic.loadUiType("Week1-3도형그리기.ui")[0]

class WindowClass(QWidget): 
    def __init__(self):
        super().__init__()
        self.drawLabel()

    def drawLabel(self):
        오 = QLabel()
        따봉 = QLabel()

        오.setStyleSheet(
            "border-style: solid;"
            "border-width: 3px;"
            "border-color: red;"
            "border-radius: 10px;"
            "image: url(오.png)"
        )

        따봉.setStyleSheet(
            "border-style: double;"
            "border-width: 7px;"
            "border-color: blue;"
            "background-color: yellow;"
            "image: url(따봉.png)"
        )

        hbox = QVBoxLayout()
        hbox.addWidget(오)
        hbox.addWidget(따봉)
        self.setLayout(hbox)

        self.setGeometry(400, 400, 500, 400)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()

    app.exec_()


