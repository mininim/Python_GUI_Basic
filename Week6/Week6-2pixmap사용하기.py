import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic


ui_file = uic.loadUiType("Week6-2pixmap사용하기.ui")[0]
image = ["", "cat.png", "dog1.png", "dog2.png"]


class WindowClass(QMainWindow, ui_file):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.num = -1
        
        self.button1.clicked.connect(self.nextImage)
        self.button2.clicked.connect(self.previousImage)
        
    
    def nextImage(self):
        self.num = self.num + 1

        if self.num > 3:
            self.num = 0
        
        if self.num == 0:
            self.img = QPixmap()
            url = "https://media.tenor.com/JuFt6X6XSiMAAAAC/cat-cute-cat.gif"
            webImage = urllib.request.urlopen(url).read()
            self.img.loadFromData(webImage)
            self.img = self.img.scaledToHeight(300)
            self.photo.setPixmap(self.img)
            
        else:
            self.img = QPixmap()
            self.img.load(image[self.num])
            self.img = self.img.scaledToHeight(300)
            self.photo.setPixmap(self.img)
            
    def previousImage(self):
        self.num = self.num - 1
        
        if self.num < 0:
            self.num = 3
            
        if self.num == 0:
            self.img = QPixmap()
            url = "https://media.tenor.com/JuFt6X6XSiMAAAAC/cat-cute-cat.gif"
            
            webImage = urllib.request.urlopen(url).read()
            self.img.loadFromData(webImage)
            self.img = self.img.scaledToHeight(300)
            self.photo.setPixmap(self.img)
        else:
            self.img = QPixmap()
            self.img.load(image[self.num])
            self.img = self.img.scaledToHeight(300)
            self.photo.setPixmap(self.img)

            
    
app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()