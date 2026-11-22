# 10.3 Fonksiyondan Deger Dondurme
# return ifadesi fonksiyonun sonucunu cagrildigi yere geri gonderir.
# return calistiginda fonksiyon sonlanir.

def yazdir_topla():
    print(5 + 3)          # sadece ekrana yazar, deger dondurmez


def dondur_topla():
    return 5 + 3          # degeri dondurur


sonuc1 = yazdir_topla()
sonuc2 = dondur_topla()
print("sonuc1:", sonuc1)   # None: return yoksa fonksiyon None dondurur
print("sonuc2:", sonuc2)

# Donen deger islemlerde kullanilabilir
print(dondur_topla() * 2)


def pi_degeri():
    return 3.14159


alan = pi_degeri() * 5 ** 2
print("Dairenin alani:", alan)


# return'den sonra yazilan kodlar calismaz
def ornek():
    return "donduruldu"
    print("Bu satir hic calismaz")


print(ornek())


# Kosula gore farkli deger dondurme
def saat_selamlama():
    import datetime
    saat = datetime.datetime.now().hour
    if saat < 12:
        return "Gunaydin"
    elif saat < 18:
        return "Iyi gunler"
    return "Iyi aksamlar"


print(saat_selamlama())


# Birden fazla deger dondurme (tuple olarak doner)
def kullanici_bilgisi():
    ad = "Sude"
    yas = 22
    sehir = "Ankara"
    return ad, yas, sehir


bilgi = kullanici_bilgisi()
print(bilgi, type(bilgi))
ad, yas, sehir = kullanici_bilgisi()
print(ad, yas, sehir)


# Liste ve sozluk dondurme
def tek_sayilar():
    return [i for i in range(20) if i % 2 == 1]


def ayarlar():
    return {"tema": "koyu", "dil": "tr"}


print(tek_sayilar())
print(ayarlar()["tema"])
