import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic


ui_file = uic.loadUiType("Week7-1Tabwidget사용하기.ui")[0]


class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.tab1.setStyleSheet('image : url(dog1.png)')
        self.tab2.setStyleSheet('image : url(cat.png)')
        
        self.tab3 = QWidget()
        self.tab3.setStyleSheet('image: url(dog2.png)')
        self.tabWidget.addTab(self.tab3, '댕댕이')
       
        
app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()