# 10.9 Degisken Sayida Parametre: **kwargs
# Parametrenin basina ** konursa istenilen sayida ISIMLI arguman alinabilir.
# Gelen argumanlar fonksiyon icinde bir SOZLUK (dict) olarak tutulur.

def bilgileri_yazdir(**bilgiler):
    print(type(bilgiler), bilgiler)
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")


bilgileri_yazdir(ad="Sude", yas=22, sehir="Ankara")
bilgileri_yazdir(urun="Laptop", fiyat=25000)


def profil_olustur(ad, soyad, **ekstra):
    profil = {"ad": ad, "soyad": soyad}
    profil.update(ekstra)
    return profil


print(profil_olustur("Sude", "Toprak", bolum="Bilgisayar", sinif=3))
print(profil_olustur("Ali", "Yilmaz"))


# *args ve **kwargs birlikte
# Sira: normal parametreler, *args, default parametreler, **kwargs
def karisik(a, b, *args, ayrac="-", **kwargs):
    print("a:", a, "b:", b)
    print("args:", args)
    print("ayrac:", ayrac)
    print("kwargs:", kwargs)


karisik(1, 2, 3, 4, 5, ayrac="|", renk="mavi", boyut="L")


# Sozlugu ** ile acarak gonderme
ayarlar = {"ad": "Ayse", "yas": 30, "meslek": "muhendis"}
bilgileri_yazdir(**ayarlar)


def baglanti_kur(sunucu, port, kullanici):
    print(f"{kullanici}@{sunucu}:{port}")


baglanti = {"sunucu": "localhost", "port": 5432, "kullanici": "admin"}
baglanti_kur(**baglanti)


# Ornek: HTML etiketi olusturan fonksiyon
def etiket(ad, icerik, **ozellikler):
    ozellik_metni = ""
    for k, v in ozellikler.items():
        ozellik_metni += f' {k}="{v}"'
    return f"<{ad}{ozellik_metni}>{icerik}</{ad}>"


print(etiket("a", "Tikla", href="https://python.org", target="_blank"))
print(etiket("p", "Paragraf", id="giris"))
