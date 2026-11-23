import sys 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget, QAction, QTableWidget, QPushButton, QVBoxLayout

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title='sude'
        self.sol=0
        self.ust=0
        self.en=300
        self.boy=200
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol, self.ust, self.en, self.boy)

        self.tab_App=Tablar(self)
        self.setCentralWidget(self.tab_App)
        self.show()

class Tablar(QWidget):
    def __init__(self,temel):
        super(QWidget,self).__init__(temel)
        self.arayuz=QVBoxLayout(self)

        #tabları oluşturma
        self.tablar=QTabWidget()
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tablar.resize(300,200)

        #tabları isimlendirme
        self.tablar.addTab(self.tab1,"Tab 1")
        self.tablar.addTab(self.tab2,"Tab 2")

        #tab1 içeriği
        self.tab1.arayuz=QVBoxLayout(self)
        self.buton1=QPushButton("Tab 1 Buton")
        self.tab1.arayuz.addWidget(self.buton1)
        self.tab1.setLayout(self.tab1.arayuz)
        self.buton1.clicked.connect(self.tiklama1)

        #tab2 içeriği
        self.tab2.arayuz=QVBoxLayout(self)
        self.buton2=QPushButton("Tab 2 Buton")
        self.tab2.arayuz.addWidget(self.buton2)
        self.tab2.setLayout(self.tab2.arayuz)
        self.buton2.clicked.connect(self.tiklama2)

        #tabları widgete ekleme
        self.arayuz.addWidget(self.tablar)
        self.setLayout(self.arayuz)
        
    def tiklama1(self):
        print("Tab 1 butonuna tiklandi")

    def tiklama2(self):
        print("Tab 2 butonuna tiklandi")

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    calis=App()
    sys.exit(app.exec_())