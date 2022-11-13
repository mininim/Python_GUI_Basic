import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
from PyQt5 import uic

ui_file = uic.loadUiType("Week2-3콤보박스만들기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox1.activated[str].connect(self.select)
        self.comboBox2.activated[str].connect(self.select)

    def select(self):
        age = str(self.comboBox1.currentText())
        height = str(self.comboBox2.currentText())
        print("저는", age , "살이고, 제 키는", height, "cm 입니다")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

