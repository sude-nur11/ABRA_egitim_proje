# 9.6 Uygulama: While Dongusu

# 1. Kullanicidan alinan iki sayi arasindaki tum asal sayilari bulun
baslangic = int(input("Baslangic: "))
bitis = int(input("Bitis: "))

print("1- Asal sayilar:", end=" ")
sayi = baslangic
while sayi <= bitis:
    if sayi > 1:
        bolen = 2
        asal = True
        while bolen < sayi:
            if sayi % bolen == 0:
                asal = False
                break
            bolen += 1
        if asal:
            print(sayi, end=" ")
    sayi += 1
print()

# 2. 1-100 arasindaki tek sayilari yazdirin
print("2-", end=" ")
i = 1
while i < 100:
    if i % 2 == 1:
        print(i, end=" ")
    i += 1
print()

# 3. 1-100 arasindaki sayilari azalan sekilde yazdirin (10'ar)
print("3-", end=" ")
i = 100
while i > 0:
    print(i, end=" ")
    i -= 10
print()

# 4. Kullanicidan alinan 5 sayiyi while ile listeye ekleyip sirali yazdirin
sayilar = []
i = 0
while i < 5:
    sayilar.append(int(input(f"{i + 1}. sayi: ")))
    i += 1
sayilar.sort()
print("4-", sayilar)

# 5. Sayilar listesindeki elemanlari while ile yazdirin
i = 0
while i < len(sayilar):
    print(f"5- {i}. indeks: {sayilar[i]}")
    i += 1

# 6. Kullanicidan alinan urun bilgilerini bir listede saklayin
adet = int(input("Kac urun ekleyeceksiniz: "))
urunler = []
i = 0
while i < adet:
    ad = input("Urun adi: ")
    fiyat = float(input("Urun fiyati: "))
    urunler.append({"ad": ad, "fiyat": fiyat})
    i += 1

for urun in urunler:
    print(f"6- Urun: {urun['ad']}, fiyat: {urun['fiyat']}")
