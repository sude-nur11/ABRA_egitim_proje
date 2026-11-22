# 6.5 Uygulama: Liste Metotlari

isimler = ["Ali", "Yagmur", "Hakan", "Deniz"]
yillar = [1998, 2000, 1998, 1987]

# 1. "Cenk" ismini listenin sonuna ekleyin
isimler.append("Cenk")
print("1-", isimler)

# 2. "Sena" degerini listenin basina ekleyin
isimler.insert(0, "Sena")
print("2-", isimler)

# 3. "Deniz" ismini listeden silin
isimler.remove("Deniz")
print("3-", isimler)

# 4. "Deniz" isminin indeksi nedir? (silindigi icin once kontrol)
if "Deniz" in isimler:
    print("4-", isimler.index("Deniz"))
else:
    print("4- Deniz listede yok")

# 5. "Ali" listenin bir elemani mi?
print("5-", "Ali" in isimler)

# 6. Liste elemanlarini ters cevirin
isimler.reverse()
print("6-", isimler)

# 7. Liste elemanlarini alfabetik olarak siralayin
isimler.sort()
print("7-", isimler)

# 8. yillar listesini rakamsal buyukluge gore siralayin
yillar.sort()
print("8-", yillar)

# 9. str = "Chevrolet,Dacia" karakter dizisini listeye cevirin
markalar = "Chevrolet,Dacia".split(",")
print("9-", markalar)

# 10. yillar dizisinin en buyuk ve en kucuk elemani nedir?
print("10-", max(yillar), min(yillar))

# 11. yillar dizisinde kac tane 1998 var?
print("11-", yillar.count(1998))

# 12. yillar dizisinin tum elemanlarini silin
yillar.clear()
print("12-", yillar)

# 13. Kullanicidan alinan 3 markayi bir listede saklayin
markalar = []
markalar.append(input("1. marka: "))
markalar.append(input("2. marka: "))
markalar.append(input("3. marka: "))
markalar.sort()
print("13-", markalar)
