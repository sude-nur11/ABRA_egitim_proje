# 13.6 Uygulama: Raising Exceptions


# 1. Parola kontrolu: Turkce karakter, bosluk ve uzunluk kontrolu yapan fonksiyon
def check_password(parola):
    if not parola.isascii():           # Turkce karakterler ASCII disindadir
        raise TypeError("Parola Turkce karakter iceremez.")
    if " " in parola:
        raise TypeError("Parola bosluk iceremez.")
    if len(parola) < 6:
        raise ValueError("Parola en az 6 karakter olmalidir.")
    if parola.isdigit() or parola.isalpha():
        raise ValueError("Parola hem harf hem rakam icermelidir.")
    return True


parola = input("1- Parola: ")
try:
    check_password(parola)
    print("   Gecerli parola.")
except (TypeError, ValueError) as hata:
    print("   Hata:", hata)


# 2. Faktoriyel fonksiyonu: negatif ve tam sayi olmayan degerler icin hata
def faktoriyel(n):
    if not isinstance(n, int):
        raise TypeError("Faktoriyel sadece tam sayilar icin hesaplanir.")
    if n < 0:
        raise ValueError("Negatif sayinin faktoriyeli hesaplanamaz.")
    sonuc = 1
    for i in range(2, n + 1):
        sonuc *= i
    return sonuc


for x in [5, -2, 3.5, 0]:
    try:
        print(f"2- {x}! = {faktoriyel(x)}")
    except (TypeError, ValueError) as hata:
        print(f"2- {x}: {hata}")


# 3. Person sinifinda gecersiz bilgi kontrolu
class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alani 10 karakterden fazla olamaz.")
        if not name.isalpha():
            raise Exception("Name alani sadece harflerden olusmalidir.")
        if year < 1900 or year > 2026:
            raise Exception("Gecersiz dogum yili.")
        self.name = name
        self.year = year


for ad, yil in [("Sude", 2004), ("Muhammedalikemal", 1990), ("Ali3", 1995), ("Ayse", 1850)]:
    try:
        p = Person(ad, yil)
        print(f"3- {p.name} olusturuldu.")
    except Exception as hata:
        print(f"3- {ad}: {hata}")
