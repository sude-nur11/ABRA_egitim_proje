# 10.8 Degisken Sayida Parametre: *args
# Parametrenin basina * konursa istenilen sayida arguman alinabilir.
# Gelen argumanlar fonksiyon icinde bir TUPLE olarak tutulur.

def topla(*sayilar):
    print("Gelen:", sayilar, type(sayilar))
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam


print(topla(1, 2))
print(topla(1, 2, 3, 4, 5))
print(topla())


def en_buyuk(*sayilar):
    if not sayilar:
        return None
    buyuk = sayilar[0]
    for s in sayilar:
        if s > buyuk:
            buyuk = s
    return buyuk


print(en_buyuk(3, 17, 8, 21, 5))


# Normal parametre ile birlikte kullanim (normal parametreler once yazilir)
def selamla(selam, *isimler):
    for isim in isimler:
        print(f"{selam} {isim}")


selamla("Merhaba", "Sude", "Ali", "Ayse")


def ortalama(ders, *notlar):
    ort = sum(notlar) / len(notlar)
    print(f"{ders} dersi ortalamasi: {ort:.2f}")


ortalama("Matematik", 70, 85, 90)
ortalama("Fizik", 50, 65)

# Listeyi * ile acarak gonderme
notlar = [80, 90, 100]
ortalama("Python", *notlar)
print(topla(*range(1, 11)))


# Ornek: Birden fazla kelimeyi birlestiren fonksiyon
def cumle_kur(*kelimeler, ayirici=" "):
    return ayirici.join(kelimeler)


print(cumle_kur("Python", "ogrenmek", "keyifli"))
print(cumle_kur("2026", "11", "21", ayirici="-"))

# print fonksiyonu da *args kullanir
print(1, 2, 3, "dort", 5.0)
