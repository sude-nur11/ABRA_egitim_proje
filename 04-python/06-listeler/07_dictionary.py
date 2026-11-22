# 6.7 Dictionary (Sozluk)
# Sozluk, verileri anahtar: deger (key: value) ciftleri olarak tutar. {} ile tanimlanir.
# Elemanlara indeks ile degil anahtar ile erisilir.

# Liste ile sehir-plaka eslestirmek zordur:
sehirler = ["Ankara", "Istanbul", "Izmir"]
plakalar = [6, 34, 35]
print(plakalar[sehirler.index("Izmir")])

# Sozluk ile cok daha kolaydir:
plaka_sozluk = {"Ankara": 6, "Istanbul": 34, "Izmir": 35}
print(plaka_sozluk["Izmir"])

# Yeni eleman ekleme ve guncelleme
plaka_sozluk["Kocaeli"] = 41
plaka_sozluk["Ankara"] = "06"
print(plaka_sozluk)

# Farkli tiplerde degerler
ogrenci = {
    "ad": "Sude",
    "soyad": "Toprak",
    "yas": 22,
    "aktif": True,
    "dersler": ["Python", "C++", "Algoritma"],
    "adres": {"sehir": "Ankara", "ilce": "Cankaya"},
}

print(ogrenci["ad"])
print(ogrenci["dersler"])
print(ogrenci["dersler"][0])
print(ogrenci["adres"]["sehir"])

# get(): anahtar yoksa hata vermez
print(ogrenci.get("bolum"))
print(ogrenci.get("bolum", "Belirtilmemis"))
try:
    print(ogrenci["bolum"])
except KeyError as hata:
    print("KeyError:", hata)

# Silme
del ogrenci["aktif"]
print(ogrenci)

# Anahtar kontrolu ve uzunluk
print("ad" in ogrenci)
print("Sude" in ogrenci)          # in anahtarlarda arar
print(len(ogrenci))

# dict() fonksiyonu ile sozluk olusturma
renk = dict(kirmizi="#ff0000", yesil="#00ff00")
print(renk)

# Anahtarlar benzersizdir, ayni anahtar tekrar yazilirsa son deger gecerli olur
d = {"a": 1, "a": 2}
print(d)
