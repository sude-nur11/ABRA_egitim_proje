# 10.6 Default (Varsayilan) Parametre
# Parametreye varsayilan deger verilirse, cagirirken o arguman gonderilmeyebilir.

def selamla(isim="misafir"):
    print(f"Merhaba {isim}")


selamla()             # Merhaba misafir
selamla("Sude")       # Merhaba Sude


def us_al(taban, us=2):
    return taban ** us


print(us_al(5))       # 25 (us=2 varsayilan)
print(us_al(5, 3))    # 125


def kullanici_olustur(ad, soyad, rol="uye", aktif=True):
    return {"ad": ad, "soyad": soyad, "rol": rol, "aktif": aktif}


print(kullanici_olustur("Sude", "Toprak"))
print(kullanici_olustur("Ali", "Yilmaz", "admin"))
print(kullanici_olustur("Ayse", "Demir", "editor", False))


# Varsayilan degerli parametreler, varsayilansiz olanlardan SONRA yazilmalidir
# def hatali(a=1, b):   -> SyntaxError


def fiyat_hesapla(fiyat, kdv=0.20, indirim=0):
    indirimli = fiyat - fiyat * indirim
    return round(indirimli + indirimli * kdv, 2)


print(fiyat_hesapla(100))
print(fiyat_hesapla(100, 0.10))
print(fiyat_hesapla(100, 0.20, 0.15))


# print fonksiyonunun da varsayilan parametreleri vardir: sep=" " ve end="\n"
print("a", "b", "c")
print("a", "b", "c", sep="-", end=" <- sep ve end degisti\n")


# Dikkat: varsayilan deger olarak liste kullanmak beklenmedik sonuclar dogurur
def hatali_ekle(eleman, liste=[]):
    liste.append(eleman)
    return liste


print(hatali_ekle(1))
print(hatali_ekle(2))      # [1, 2] -> onceki cagri ile ayni liste kullanildi


def dogru_ekle(eleman, liste=None):
    if liste is None:
        liste = []
    liste.append(eleman)
    return liste


print(dogru_ekle(1))
print(dogru_ekle(2))       # [2]
