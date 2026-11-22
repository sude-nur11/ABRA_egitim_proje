# 12.1 OOP Nedir?
# OOP (Object Oriented Programming - Nesne Yonelimli Programlama), gercek hayattaki
# varliklari (araba, ogrenci, hesap ...) ozellikleri (nitelik) ve davranislari
# (metot) olan NESNELER olarak modelleme yaklasimidir.
#
# Sinif (class): nesnelerin taslagi / kalibi. Ornek: "Araba" kavrami
# Nesne (object / instance): siniftan uretilen somut ornek. Ornek: "34 ABC 12 plakali araba"
# Nitelik (attribute): nesnenin ozellikleri. Ornek: marka, renk, hiz
# Metot (method): nesnenin yapabildigi isler. Ornek: hizlan(), dur()

# OOP olmadan: her araba icin ayri degiskenler / sozlukler
araba1_marka = "Toyota"
araba1_hiz = 0
araba2_marka = "Ford"
araba2_hiz = 0

araba1_hiz += 20
print(araba1_marka, araba1_hiz)


# OOP ile: veri ve o veriyle ilgili islemler bir arada tutulur
class Araba:
    def __init__(self, marka, renk):
        self.marka = marka
        self.renk = renk
        self.hiz = 0

    def hizlan(self, miktar):
        self.hiz += miktar
        print(f"{self.marka} hizlandi: {self.hiz} km/s")

    def dur(self):
        self.hiz = 0
        print(f"{self.marka} durdu.")


a1 = Araba("Toyota", "beyaz")
a2 = Araba("Ford", "siyah")
a1.hizlan(20)
a1.hizlan(30)
a2.hizlan(50)
a1.dur()

# Aslinda Python'da her sey bir nesnedir
sayi = 5
metin = "python"
liste = [3, 1, 2]
print(type(sayi), type(metin), type(liste))   # her biri bir sinifin nesnesi
print(metin.upper())                          # str sinifinin upper metodu
liste.sort()                                  # list sinifinin sort metodu
print(liste)

# OOP'nin 4 temel prensibi:
# 1. Encapsulation (kapsulleme): veriyi ve islemlerini bir arada tutup disariya kapatma
# 2. Inheritance (kalitim): bir sinifin baska bir siniftan ozellik devralmasi
# 3. Polymorphism (cok bicimlilik): ayni metodun farkli siniflarda farkli calismasi
# 4. Abstraction (soyutlama): gereksiz detaylari gizleyip sadece gerekeni gosterme
print(isinstance(a1, Araba))
