import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QRadioButton, QCheckBox
from PyQt5 import uic 

ui_file = uic.loadUiType("Week3-2레이아웃사용하기.ui")[0]

def add_animal(list, name):
    list.append(name)
    return list

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        label1 = QLabel("수직레이아웃")
        label2 = QLabel("수평레이아웃")

        self.verticalLayout.addWidget(label1)
        self.horizontalLayout.addWidget(label2)



app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()