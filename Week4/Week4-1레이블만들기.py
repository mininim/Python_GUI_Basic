import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton, QCheckBox
from PyQt5 import uic

ui_file = uic.loadUiType("Week4-1레이블만들기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button1.clicked.connect(self.button1_Click)
        self.button2.clicked.connect(self.button2_Click)
        self.button3.clicked.connect(self.button3_Click)
        self.pushButton.clicked.connect(self.pushButton_Click)
        self.checkBox.clicked.connect(self.checkBoxRadio_Click)
        self.radioButton.clicked.connect(self.checkBoxRadio_Click)
        self.label.setText("")


    def button1_Click(self):
        self.disablecheckBoxAndRadio()
        font = self.label.font()
        font.setPointSize(12)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setText("나는 강아지를 키워")

    def button2_Click(self):
        self.disablecheckBoxAndRadio()
        font = self.label.font()
        font.setPointSize(16)
        font.setItalic(True)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setText("나는 고양이를 키워")

    def button3_Click(self):
        self.disablecheckBoxAndRadio()
        font = self.label.font()
        font.setPointSize(16)
        font.setItalic(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("나는 토끼를 키워")
    
    
    def pushButton_Click(self):
        self.disablecheckBoxAndRadio()
        font = self.label.font()
        font.setPointSize(12)
        font.setItalic(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("푸쉬버튼")
    
    def checkBoxRadio_Click(self):
        if self.checkBox.isChecked() and self.radioButton.isChecked():
            font = self.label.font()
            font.setPointSize(12)
            font.setItalic(False)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setText("체크박스 & 라디오버튼")
        elif self.checkBox.isChecked():
            font = self.label.font()
            font.setPointSize(12)
            font.setItalic(False)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setText("체크박스 & 라디오버튼")
        elif self.radioButton.isChecked():
            font = self.label.font()
            font.setPointSize(12)
            font.setItalic(False)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setText("라디오버튼")
        else:
            self.label.setText("")
    
    def disablecheckBoxAndRadio(self):
        self.checkBox.setCheckState(0)
        self.radioButton.setChecked(0)
        

    

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()

