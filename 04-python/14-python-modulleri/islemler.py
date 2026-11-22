# 14.3 Uygulama: Modul Tanimlama icin olusturulan modul.
# Hesap makinesi islemleri ve ogrenci notu fonksiyonlari icerir.

PI = 3.14159


def topla(a, b):
    return a + b


def cikar(a, b):
    return a - b


def carp(a, b):
    return a * b


def bol(a, b):
    if b == 0:
        raise ZeroDivisionError("Sifira bolme yapilamaz.")
    return a / b


def us_al(a, b):
    return a ** b


def ortalama(notlar):
    return sum(notlar) / len(notlar) if notlar else 0


def harf_notu(puan):
    if puan >= 90:
        return "AA"
    elif puan >= 80:
        return "BA"
    elif puan >= 70:
        return "BB"
    elif puan >= 60:
        return "CB"
    elif puan >= 50:
        return "CC"
    return "FF"


ISLEMLER = {"+": topla, "-": cikar, "*": carp, "/": bol, "**": us_al}

if __name__ == "__main__":
    print(topla(3, 4), bol(10, 4), harf_notu(85))
