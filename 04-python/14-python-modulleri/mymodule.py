# 14.2 Module Tanimlama icin olusturulan ornek modul.
# Bu dosya diger dosyalardan "import mymodule" ile kullanilir.

# Degiskenler
sehir = "Ankara"
person = {
    "name": "Sude",
    "age": 22,
    "city": "Ankara",
}
numbers = [1, 2, 3, 4, 5]


# Fonksiyonlar
def merhaba(isim):
    return f"Merhaba {isim}"


def topla(*sayilar):
    return sum(sayilar)


def daire_alani(yaricap):
    return 3.14 * yaricap ** 2


# Sinif
class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def yas_hesapla(self, guncel_yil=2026):
        return guncel_yil - self.year

    def __str__(self):
        return f"{self.name} ({self.year})"


# __name__ degiskeni:
# Dosya dogrudan calistirilirsa __name__ == "__main__" olur.
# Baska bir dosyadan import edilirse __name__ == "mymodule" olur.
# Boylece asagidaki kodlar sadece dosya dogrudan calistirildiginda calisir.
if __name__ == "__main__":
    print("mymodule dogrudan calistirildi.")
    print(merhaba("Test"))
    print(topla(1, 2, 3))
    print(Person("Ali", 1998))
