import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ders_9'
        self.sol = 0
        self.ust = 0
        self.en = 300
        self.boy = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol, self.ust, self.en, self.boy)

        self.SayiGirdisi()
        self.TercihGirdisi()
        self.MetinGirdisi()

        self.show()

    def SayiGirdisi(self):
        sayi, okBasildi = QInputDialog.getInt(self, "Sayi girdisi", "lutfen bir sayi giriniz")
        if okBasildi:
            print("girilen sayi: ", sayi)

    def TercihGirdisi(self):
        tercih, okBasildi = QInputDialog.getItem(self, "Tercih girdisi", "lutfen bir renk seciniz", ["mavi", "kirmizi", "sari"])
        if okBasildi:
            print("secilen renk: ", tercih)

    def MetinGirdisi(self):
        metin, okBasildi = QInputDialog.getText(self, "Metin girdisi", "lutfen bir metin giriniz")
        if okBasildi:
            print("girilen metin: ", metin)

if __name__=='__main__':
    app= QApplication(sys.argv)
    pencere=App()
    sys.exit(app.exec_())