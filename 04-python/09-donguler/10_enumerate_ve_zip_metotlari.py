# 9.10 Enumerate ve Zip Metotlari

# --- enumerate ---
# Dizinin elemanlarini sira numarasi (indeks) ile birlikte verir.

meyveler = ["elma", "armut", "muz", "kiraz"]

# enumerate olmadan
indeks = 0
for meyve in meyveler:
    print(indeks, meyve)
    indeks += 1

# enumerate ile
for indeks, meyve in enumerate(meyveler):
    print(indeks, meyve)

# Baslangic degeri verme
for sira, meyve in enumerate(meyveler, start=1):
    print(f"{sira}. {meyve}")

print(list(enumerate(meyveler)))

# Stringde enumerate
for i, harf in enumerate("Python"):
    print(i, harf, end=" | ")
print()

# Belirli elemanin indeksini bulma
sayilar = [5, 8, 3, 8, 1, 8]
indeksler = [i for i, s in enumerate(sayilar) if s == 8]
print("8'in gectigi indeksler:", indeksler)

# --- zip ---
# Birden fazla diziyi eleman eleman eslestirir.

isimler = ["Sude", "Ali", "Ayse"]
yaslar = [22, 25, 30]
sehirler = ["Ankara", "Izmir", "Bursa"]

for isim, yas in zip(isimler, yaslar):
    print(f"{isim} {yas} yasinda")

for isim, yas, sehir in zip(isimler, yaslar, sehirler):
    print(f"{isim}, {yas}, {sehir}")

print(list(zip(isimler, yaslar)))

# Iki listeden sozluk olusturma
sozluk = dict(zip(isimler, yaslar))
print(sozluk)

# Farkli uzunlukta listelerde kisa olanin uzunlugu kadar eslestirir
print(list(zip([1, 2, 3], ["a", "b"])))

# zip ve enumerate birlikte
for i, (isim, yas) in enumerate(zip(isimler, yaslar), start=1):
    print(f"{i}- {isim}: {yas}")

# Iki listenin eleman eleman toplami
l1 = [1, 2, 3]
l2 = [10, 20, 30]
print([a + b for a, b in zip(l1, l2)])
