# 4.2 Degisken Tanimlama
# Python'da degisken tanimlarken tip yazilmaz: degisken_adi = deger

# Farkli tiplerde degisken tanimlama
ad = "Sude"            # metin (string)
yas = 22               # tam sayi (int)
boy = 1.65             # ondalikli sayi (float)
ogrenci_mi = True      # mantiksal (bool)

print(ad)
print(yas)
print(boy)
print(ogrenci_mi)

# Tek satirda birden fazla degisken tanimlama
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# Birden fazla degiskene ayni degeri atama
a = b = c = 100
print("a:", a, "b:", b, "c:", c)

# Degiskenlerin degerlerini yer degistirme
x, y = y, x
print("Yer degistirme sonrasi x:", x, "y:", y)

# Yeniden atama: degiskenin hem degeri hem tipi degisebilir (dinamik tip)
deger = 5
print(deger, type(deger))
deger = "bes"
print(deger, type(deger))
deger = 5.0
print(deger, type(deger))

# Degiskeni silme
gecici = "silinecek"
print(gecici)
del gecici
# print(gecici)  -> NameError: name 'gecici' is not defined

# Degiskenleri print ile birlikte kullanma
sehir = "Ankara"
plaka = 6
print("Sehir:", sehir, "- Plaka:", plaka)
print(f"{sehir} sehrinin plakasi {plaka:02d}")

# Sabitler: Python'da gercek sabit yoktur, buyuk harfle yazmak bir gelenektir
PI = 3.14159
YERCEKIMI = 9.81
print("PI:", PI, "g:", YERCEKIMI)
