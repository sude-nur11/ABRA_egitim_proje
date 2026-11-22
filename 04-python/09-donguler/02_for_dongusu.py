# 9.2 For Dongusu

# Liste uzerinde
sayilar = [1, 2, 3, 4, 5]
for sayi in sayilar:
    print(sayi)

# Her elemani islemden gecirme
for sayi in sayilar:
    print(f"{sayi} * {sayi} = {sayi * sayi}")

# String uzerinde
isim = "Sude"
for harf in isim:
    print(harf)

# Kosul ile birlikte
for sayi in sayilar:
    if sayi % 2 == 0:
        print(sayi, "cift")

# Toplam hesaplama
toplam = 0
for sayi in sayilar:
    toplam += sayi
print("Toplam:", toplam)

# Tuple listesi uzerinde (unpacking)
ogrenciler = [("Sude", 90), ("Ali", 75), ("Ayse", 85)]
for ad, puan in ogrenciler:
    print(f"{ad}: {puan}")

# Sozluk uzerinde
urun = {"ad": "Laptop", "fiyat": 25000, "stok": 10}
for anahtar in urun:
    print(anahtar)
for deger in urun.values():
    print(deger)
for anahtar, deger in urun.items():
    print(anahtar, "=", deger)

# Ic ice for donguleri
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("-" * 10)

# Set uzerinde
for renk in {"kirmizi", "yesil", "mavi"}:
    print(renk)

# Yeni liste olusturma
kareler = []
for sayi in sayilar:
    kareler.append(sayi ** 2)
print(kareler)

# Ayni islem list comprehension ile
print([sayi ** 2 for sayi in sayilar])
