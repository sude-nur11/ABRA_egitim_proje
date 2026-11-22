# 12.3 Constructor (Yapici Metot): __init__
# Nesne olusturuldugu anda otomatik calisir. Nesneye baslangic degerlerini vermek icin
# kullanilir. self, olusturulan nesnenin kendisini temsil eder.

class Person:
    # sinif niteligi: tum nesneler icin ortak
    tur = "insan"

    def __init__(self, name, year, address="belirtilmemis"):
        # nesne nitelikleri (instance attributes): her nesneye ozel
        self.name = name
        self.year = year
        self.address = address
        print(f"{name} icin nesne olusturuldu.")


p1 = Person("Sude", 2004, "Ankara")
p2 = Person("Ali", 1998)

print(p1.name, p1.year, p1.address, p1.tur)
print(p2.name, p2.year, p2.address, p2.tur)

# __init__ parametreleri verilmezse hata olusur
try:
    p3 = Person()
except TypeError as hata:
    print("Hata:", hata)


class Ogrenci:
    okul = "BTK Akademi"
    ogrenci_sayisi = 0                 # tum nesnelerin paylastigi sayac

    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.dersler = []              # her nesne icin ayri liste
        self.email = f"{ad.lower()}.{soyad.lower()}@ornek.com"
        Ogrenci.ogrenci_sayisi += 1


o1 = Ogrenci("Sude", "Toprak", 101)
o2 = Ogrenci("Ayse", "Demir", 102)
o1.dersler.append("Python")

print(o1.ad, o1.email, o1.dersler)
print(o2.ad, o2.email, o2.dersler)
print("Toplam ogrenci:", Ogrenci.ogrenci_sayisi)


# __str__: nesne print edildiginde ne yazilacagini belirler
class Kitap:
    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def __str__(self):
        return f"{self.ad} - {self.yazar} ({self.sayfa} sayfa)"

    def __len__(self):
        return self.sayfa


k = Kitap("Suc ve Ceza", "Dostoyevski", 687)
print(k)
print(len(k))
