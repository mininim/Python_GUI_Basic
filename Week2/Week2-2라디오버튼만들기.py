import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton
from PyQt5 import uic


ui_file = uic.loadUiType("Week2-2라디오버튼만들기.ui")[0]

class WindowClass(QMainWindow, ui_file): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radio1.clicked.connect(self.radio_Click)
        self.radio2.clicked.connect(self.radio_Click)
        self.radio3.clicked.connect(self.radio_Click)
        self.radio4.clicked.connect(self.radio_Click)

    def radio_Click(self):
        animal = ""
        if self.radio1.isChecked():
            animal = "기린"
        elif self.radio2.isChecked():
            animal = "코끼리"
        elif self.radio3.isChecked():
            animal = "황제펭귄"
        elif self.radio4.isChecked():
            animal = "티라노사우루스"
        
        print("내가 가장 보고 시은 동물은", animal,"입니다")
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


