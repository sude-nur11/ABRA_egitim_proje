import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app=QApplication(sys.argv)
    ekran=QDialog()

    # buton düzenlemesi
    bi=QPushButton(ekran)
    bi.setText("baslat")
    bi.move(20,20)
    bi.clicked.connect(bi_tiklandi)

    # buton 2 düzenlemesi
    bi2=QPushButton(ekran)
    bi2.setText("durdur")
    bi2.move(120,20)
    bi2.clicked.connect(bi2_tiklandi)

    # ekran düzenlemesi
    ekran.setGeometry(100,100,200,50)
    ekran.setWindowTitle("koddunyam")
    ekran.show()
    sys.exit(app.exec_())


def bi_tiklandi():
    print("başlat butonuna tiklandi")   


def bi2_tiklandi():
    print("durdur butonuna tiklandi") 


if __name__=='__main__':
    window()