import sys 
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title ='koddunyam'
        self.sol=0
        self.ust=0
        self.en=300
        self.boy=200
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.sol,self.ust,self.en,self.boy)
        self.createTable()

        #tablo yerleştirme
        self.arayuz=QVBoxLayout()
        self.arayuz.addWidget(self.tabl0Widget)
        self.setLayout(self.arayuz)

        #ekrana getirme
        self.show()

    def createTable(self):
        self.tabl0Widget=QTableWidget()
        #tablo özelliklerini atıycaz
        self.tabl0Widget.setRowCount(4)
        self.tabl0Widget.setColumnCount(2)
        #içini doldurma
        self.tabl0Widget.setItem(0,0,QTableWidgetItem("No:0,0"))
        self.tabl0Widget.setItem(0,1,QTableWidgetItem("No:0,1"))
        self.tabl0Widget.setItem(1,0,QTableWidgetItem("No:1,0"))
        self.tabl0Widget.setItem(1,1,QTableWidgetItem("No:1,1"))
        self.tabl0Widget.setItem(2,0,QTableWidgetItem("No:2,0"))
        self.tabl0Widget.setItem(2,1,QTableWidgetItem("No:2,1"))
        self.tabl0Widget.setItem(3,0,QTableWidgetItem("No:3,0"))
        self.tabl0Widget.setItem(3,1,QTableWidgetItem("No:3,1"))
        self.tabl0Widget.move(0,0)

        #tabloya komut
        self.tabl0Widget.doubleClicked.connect(self.tiklama)

    def tiklama(self):
        for tabloKonum in self.tabl0Widget.selectedItems():
            print(tabloKonum.row(),tabloKonum.column(),tabloKonum.text())

if __name__=="__main__":
    app=QApplication(sys.argv)
    calis=App()
    sys.exit(app.exec_())
