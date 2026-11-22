# 12.4 Methods (Metotlar)
# Sinif icinde tanimlanan fonksiyonlardir. Ilk parametreleri self'tir.

class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # instance metotlari
    def intro(self):
        print(f"Merhaba, ben {self.name}.")

    def calculate_age(self, current_year=2026):
        return current_year - self.year

    def birthday(self):
        self.year -= 1          # nesnenin niteligini degistirebilir
        print(f"{self.name} bir yas buyudu.")


p1 = Person("Sude", 2004)
p2 = Person("Ali", 1998)

p1.intro()
p2.intro()
print(f"{p1.name} {p1.calculate_age()} yasinda")
print(f"{p2.name} {p2.calculate_age()} yasinda")

# Metodu siniftan cagirma (self elle gonderilir)
Person.intro(p1)


class Circle:
    pi = 3.14                     # sinif niteligi

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * self.yaricap ** 2

    # sinif metodu: nesneye degil sinifa ait, cls parametresi alir
    @classmethod
    def capa_gore(cls, cap):
        return cls(cap / 2)

    # statik metot: ne nesneye ne sinifa ihtiyac duyar
    @staticmethod
    def birim():
        return "cm"


c1 = Circle(5)
c2 = Circle.capa_gore(20)
print(f"c1 alan: {c1.alan_hesapla()} {Circle.birim()}2, cevre: {c1.cevre_hesapla()}")
print(f"c2 yaricap: {c2.yaricap}, alan: {c2.alan_hesapla()}")


# Metotlar birbirini cagirabilir
class Hesap:
    def __init__(self, sahip, bakiye=0):
        self.sahip = sahip
        self.bakiye = bakiye

    def yatir(self, miktar):
        self.bakiye += miktar
        self.ozet()

    def cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")
        else:
            self.bakiye -= miktar
        self.ozet()

    def ozet(self):
        print(f"{self.sahip}: {self.bakiye} TL")


h = Hesap("Sude", 500)
h.yatir(250)
h.cek(1000)
h.cek(300)
