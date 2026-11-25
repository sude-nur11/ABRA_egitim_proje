import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title='ders_7'
        self.sol=0
        self.ust=0
        self.en=300
        self.boy=200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol, self.ust, self.en, self.boy)

        self.GridOlustur()
        self.YatayDuzen()

        ekranArayuz = QVBoxLayout()
        ekranArayuz.addWidget(self.gridkumesi)
        ekranArayuz.addWidget(self.yatayDuzen)
        self.setLayout(ekranArayuz)
        self.show()

    def GridOlustur(self):
        self.gridkumesi = QGroupBox("Grid kutular")
        arayuz = QGridLayout()
        arayuz.setColumnStretch(1, 2)
        arayuz.setColumnStretch(2, 5)

        arayuz.addWidget(QPushButton("1"), 0, 0)
        arayuz.addWidget(QPushButton("2"), 0, 1)
        arayuz.addWidget(QPushButton("3"), 0, 2)
        arayuz.addWidget(QPushButton("4"), 1, 0)
        arayuz.addWidget(QPushButton("5"), 1, 1)
        arayuz.addWidget(QPushButton("6"), 1, 2)
        arayuz.addWidget(QPushButton("7"), 2, 0)
        arayuz.addWidget(QPushButton("8"), 2, 1)
        arayuz.addWidget(QPushButton("9"), 2, 2)
        arayuz.addWidget(QPushButton("0"), 3, 1)
        
        self.gridkumesi.setLayout(arayuz)

    def YatayDuzen(self):
        self.yatayDuzen = QGroupBox("en sevdiginiz renk nedir?")
        arayuz2 = QHBoxLayout()
        butonM=QPushButton("mavi")
        butonM.clicked.connect(self.tiklaM)
        arayuz2.addWidget(butonM)

        butonK=QPushButton("kirmizi")
        butonK.clicked.connect(self.tiklaK)
        arayuz2.addWidget(butonK)

        butonS=QPushButton("sari")
        butonS.clicked.connect(self.tiklaS)
        arayuz2.addWidget(butonS)

        #kendi arayüzüne burda ekledik
        self.yatayDuzen.setLayout(arayuz2)

    def tiklaM(self):
        print("mavi buton tiklandi")

    def tiklaK(self):
        print("kirmizi buton tiklandi")

    def tiklaS(self):
        print("sari buton tiklandi")

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())        
      