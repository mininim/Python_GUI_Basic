import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5 import uic 

ui_file = uic.loadUiType("Week3-1체크박스.ui")[0]

def add_animal(list, name):
    list.append(name)
    return list

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox1.stateChanged.connect(self.check_Click)
        self.checkBox2.stateChanged.connect(self.check_Click)
        self.checkBox3.stateChanged.connect(self.check_Click)
        self.checkBox4.stateChanged.connect(self.check_Click)
        self.checkBox5.stateChanged.connect(self.check_Click)
    
    def check_Click(self):
        animal_list = []
        if self.checkBox1.isChecked():
            add_animal(animal_list, "강아지")

        if self.checkBox2.isChecked():
            add_animal(animal_list, "냐옹이")

        if self.checkBox3.isChecked():
            add_animal(animal_list, "호랭이")

        if self.checkBox4.isChecked():
            add_animal(animal_list, "사자")

        if self.checkBox5.isChecked():
            add_animal(animal_list, "햄스터")

        print(animal_list)


app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()



"""
checkBox 메소드 
text()      체크 박스의 라벨 텍스트를 반환합니다.
setText() 	체크 박스의 라벨 텍스트를 설정합니다.
isChecked()	체크 박스의 상태를 반환합니다. (True/False)
checkState()체크 박스의 상태를 반환합니다. (2/1/0)
toggle()	체크 박스의 상태를 변경합니다.

"""