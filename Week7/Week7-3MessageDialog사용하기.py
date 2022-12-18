import sys
from PyQt5.QtWidgets import * 
from PyQt5 import uic

ui_file = uic.loadUiType("Week7-3MessageDialog사용하기.ui")[0]

class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.button1.clicked.connect(self.close)
        self.button2.clicked.connect(self.warning)
        
    def close(self):
        click = QMessageBox.question(self, '종료 버튼 창', '프로그램을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No , QMessageBox.No)

        if click == QMessageBox.Yes:
            super().close()
    
    def warning(self):
        click = QMessageBox.warning(self, '경고 버튼 창', '경고가 발생했습니다', QMessageBox.Help | QMessageBox.Ignore | QMessageBox.Retry)
    
    def closeEvent(self, event):
        click = QMessageBox.question(self, 'X 버튼 창', '프로그램을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        
        if click == QMessageBox.Yes:
            event.accept()
        else : 
            event.ignore()
        
            
app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()