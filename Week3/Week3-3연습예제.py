# 개인정보 이용 동의 체크 한것을 확인해야한 push 버튼 활성화 


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5 import uic 

ui_file = uic.loadUiType("Week3-3연습예제.ui")[0]

class WindowClass(QMainWindow, ui_file):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBox1.clicked.connect(self.check_Click)
        self.checkBox2.clicked.connect(self.check_Click)
        self.checkBox3.clicked.connect(self.check_Click)

        self.checkBox_all.clicked.connect(self.check_all_Click)

        self.pushButton.clicked.connect(self.register)


    def check_Click(self):
        if self.checkBox1.isChecked() and self.checkBox2.isChecked() and self.checkBox3.isChecked():
            self.checkBox_all.setCheckState(2)
        else:
            self.checkBox_all.setCheckState(0)

    def check_all_Click(self):
        
        if self.checkBox_all.isChecked(): 
            # 모두 선택 체크 박스 

            self.checkBox1.setCheckState(2)

            self.checkBox2.setCheckState(2)
            
            self.checkBox3.setCheckState(2)


        else: # 모두 선택 체크 박스 X
            self.checkBox1.setCheckState(0)

            self.checkBox2.setCheckState(0)
            
            self.checkBox3.setCheckState(0)


    def register(self):
        if self.checkBox1.isChecked() and self.checkBox2.isChecked() and self.checkBox3.isChecked():
            print("가입성공")
            self.label.setText("가입 성공")
        else : 
            print("개인정보 취급 동의 내용 확인")
            self.label.setText("개인정보 취급 동의 내용 확인")

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()




