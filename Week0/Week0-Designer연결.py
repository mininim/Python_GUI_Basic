import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#ui 파일 로딩 
ui_file = uic.loadUiType('./Week0-emty.ui')[0]

#Custom window 생성 :  QMainWindow 상속
class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec_()






