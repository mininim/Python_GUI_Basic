"""

5-1 예제에  다시풀기 | 문제 수정 기능을 추가하여 퀴즈 프로그램을 만들어보좡

    다시 풀기 기능)

        입력 : ##
        기능 : 처음부터 다시 풀기 

    문제 수정)
        입력 : #정답 #힌트1#힌트2#힌트3
        기능 : 문제를 입력받은 정답과 힌트들로 초기화 한다.
        
히든 메세지 : 10번이상 틀리면 놀리기 멘트

        파이썬 
        split()
        strip()

str.strip()


메소드 추가 개념 

Line Edit 

PlaceHolder:

    1. 
    self.lineEdit.setPlaceholderText(' 비밀번호를 입력하세요 ')

    2. 
    self.lineEdit.setEchMode(QLineEdit.Password)

String: 
    isdigit():
    숫자인지 확인
    
    str.isdigit()
    
"""
"""
    text() ,  text()


--> Bool


"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

ui_file = uic.loadUiType("Week5-3퀴즈프로그램심화예제.ui")[0]
push = 0 
answer = "토끼"
hint0 = "나는 4개의 다리를 가졌어요"
hint1 = "내 눈은 빨간색이에요"
hint2 = "나는 하얗고 긴 귀를 가졌어요"


class WindowClass(QMainWindow, ui_file):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button1.clicked.connect(self.button_click)
    
    def button_click(self):
        global push

        if self.lineEdit.text()[0] == "#":
            push = 0
            if self.lineEdit.text()[1] == "#":
                self.label2.setText("")
                self.label3.setText("")
                self.label4.setText("다시 풀어보기")
            
                self.lineEdit.clear()
            else: 
                

                #  입력 예시 : #강아지 #나는 기요미에요#나는 깜찍해요#나는 뽀짝해요
                input = self.lineEdit.text().split("#")
            
                global answer, hint0, hint1, hint2
                answer = input[1]
                hint0 = input[2]
                hint1 = input[3]
                hint2 = input[4]
            
                self.label1.setText(hint0)
                self.label2.setText("")
                self.label3.setText("")
                self.label4.setText("수정 완료")
            
                self.lineEdit.clear()
            
            
        else:
            push = push + 1
            
            if self.lineEdit.text()== answer:
                self.label4.setText(self.lineEdit.text()+"는 정답 입니다")
            elif push == 1:
                self.label2.setText(hint1)
                self.label4.setText(self.lineEdit.text()+"는 정답이 아닙니다")
            elif push >= 10:
                self.label4.setText(self.lineEdit.text()+"는 답이 아닙니다 이걸 10번넘게 틀리네ㅋㅋ")
            else:
                self.label3.setText(hint2)
                self.label4.setText(self.lineEdit.text()+"는 답이 아닙니다")
            

        
        



app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()