# 9.3 Uygulama: For Dongusu

sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1. Sayilar listesindeki hangi sayilar 3'un katidir?
print("1-", end=" ")
for s in sayilar:
    if s % 3 == 0:
        print(s, end=" ")
print()

# 2. Sayilar listesindeki sayilarin toplami kactir?
toplam = 0
for s in sayilar:
    toplam += s
print("2- Toplam:", toplam)

# 3. Sayilar listesindeki tek sayilarin karesini alin
print("3-", end=" ")
for s in sayilar:
    if s % 2 == 1:
        print(s ** 2, end=" ")
print()

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# 4. Sehirlerden hangileri en fazla 5 karakterlidir?
print("4-", end=" ")
for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir, end=" ")
print()

urunler = [
    {"name": "samsung S6", "price": "3000"},
    {"name": "samsung S7", "price": "4000"},
    {"name": "samsung S8", "price": "5000"},
    {"name": "samsung S9", "price": "6000"},
    {"name": "samsung S10", "price": "7000"},
]

# 5. Urunlerin fiyatlari toplami nedir?
toplam = 0
for urun in urunler:
    toplam += int(urun["price"])
print("5- Toplam fiyat:", toplam)

# 6. Urunlerden fiyati en fazla 5000 olanlari gosterin
print("6-", end=" ")
for urun in urunler:
    if int(urun["price"]) <= 5000:
        print(urun["name"], end=", ")
print()

# 7. Listedeki en buyuk sayiyi max() kullanmadan bulun
en_buyuk = sayilar[0]
for s in sayilar:
    if s > en_buyuk:
        en_buyuk = s
print("7- En buyuk:", en_buyuk)
