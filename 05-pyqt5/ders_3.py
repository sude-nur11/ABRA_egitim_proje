import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QPushButton, QWidgetAction
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslik="koddunyam"
        self.sol=10
        self.ust=10
        self.en=640
        self.boy=400
        self.arayuz()

    def arayuz(self):
        self.setWindowTitle(self.baslik)
        self.setGeometry(self.sol,self.ust,self.en,self.boy)

        anaMenu=self.menuBar()
        fileMenu=anaMenu.addMenu("file")
        editMenu=anaMenu.addMenu("edit")
        viewMenu=anaMenu.addMenu("view")
        newProject=fileMenu.addMenu("new")
        tiklamaButonu=QAction('tikla',self)
        newProject.addAction(tiklamaButonu)
        tiklamaButonu.triggered.connect(self.tiklandi)

        cikisButonu=QAction(QIcon("bug.png"),'cikis',self)
        cikisButonu.setShortcut('Ctrl+Q')
        cikisButonu.setStatusTip("App kapat")
        cikisButonu.triggered.connect(self.close)
        fileMenu.addAction(cikisButonu)

        self.show()
    def tiklandi(self):
        print("tiklandi")

if __name__=="__main__":
    app=QApplication(sys.argv)
    calis=App()
    sys.exit(app.exec_())
