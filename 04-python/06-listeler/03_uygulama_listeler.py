# 6.3 Uygulama: Listeler

markalar = ["BMW", "Mercedes", "Opel", "Mazda"]

# 1. Listede kac eleman var?
print("1-", len(markalar))

# 2. Listenin ilk ve son elemani nedir?
print("2-", markalar[0], markalar[-1])

# 3. "Mazda" degerini "Toyota" ile degistirin
markalar[-1] = "Toyota"
print("3-", markalar)

# 4. "Mercedes" listede var mi?
print("4-", "Mercedes" in markalar)

# 5. Listenin -2 indeksindeki deger nedir?
print("5-", markalar[-2])

# 6. Listenin ilk 3 elemanini alin
print("6-", markalar[:3])

# 7. Listenin son 2 elemaninin yerine "Toyota" ve "Renault" yazin
markalar[-2:] = ["Toyota", "Renault"]
print("7-", markalar)

# 8. Listeye "Audi" ve "Nissan" degerlerini ekleyin
markalar = markalar + ["Audi", "Nissan"]
print("8-", markalar)

# 9. Listeyi tersten yazdirin
print("9-", markalar[::-1])

# 10. Ogrenci bilgilerini ic ice listede tutun
ogrenciler = [
    ["Sude", "Toprak", [70, 85, 90]],
    ["Ali", "Yilmaz", [50, 60, 45]],
    ["Ayse", "Demir", [95, 80, 88]],
]
print("10- Ilk ogrencinin adi:", ogrenciler[0][0])
print("    Ikinci ogrencinin 2. notu:", ogrenciler[1][2][1])
print("    Ucuncu ogrencinin not ortalamasi:",
      round(sum(ogrenciler[2][2]) / len(ogrenciler[2][2]), 2))

# 11. Kullanicidan 3 sayi alip listeye ekleyin
sayilar = []
sayilar = sayilar + [int(input("1. sayi: "))]
sayilar = sayilar + [int(input("2. sayi: "))]
sayilar = sayilar + [int(input("3. sayi: "))]
print("11- Sayilar:", sayilar)
print("    En buyuk:", max(sayilar), "En kucuk:", min(sayilar),
      "Toplam:", sum(sayilar))
