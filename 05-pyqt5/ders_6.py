import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def ekran():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("ders_6")
    w.setGeometry(0, 0, 300, 400)

    #ana ekran buton düzeni
    buton1 = QPushButton(w)
    buton1.setText("bilgilendirme")
    buton1.move(100, 50)
    buton1.clicked.connect(bilgilendirme)

    w.show()
    sys.exit(app.exec_())

def bilgilendirme():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Bu bir bilgilendirme mesajidir.")
    msg.setInformativeText("Bu mesaj, kullaniciya bilgi vermek için kullanilir.")
    msg.setText("bilgilendirme kutusu")
    msg.setWindowTitle("Bilgilendirme")
    msg.setDetailedText("Bu detayli bilgi, kullaniciya ekstra bilgi vermek için kullanilir.\n \nkoddunyam")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()

if __name__=='__main__':
    ekran()