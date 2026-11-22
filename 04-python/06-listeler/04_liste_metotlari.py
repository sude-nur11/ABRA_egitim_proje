# 6.4 Liste Metotlari

sayilar = [1, 10, 5, 16, 4]
harfler = ["d", "a", "c", "b"]

# Eleman ekleme
harfler.append("e")            # sona ekler
print("append:", harfler)
harfler.insert(0, "z")         # belirtilen indekse ekler
print("insert:", harfler)
harfler.extend(["x", "y"])     # bir listenin elemanlarini ekler
print("extend:", harfler)

# Eleman silme
harfler.remove("z")            # degere gore ilk buldugunu siler
print("remove:", harfler)
silinen = harfler.pop()        # son elemani siler ve dondurur
print("pop:", harfler, "silinen:", silinen)
harfler.pop(0)                 # indekse gore siler
print("pop(0):", harfler)
del harfler[0]                 # del ifadesi ile silme
print("del:", harfler)

# Siralama
sayilar.sort()
print("sort:", sayilar)
sayilar.sort(reverse=True)
print("sort(reverse):", sayilar)
sayilar.reverse()
print("reverse:", sayilar)
print("sorted (yeni liste):", sorted(harfler), "orijinal:", harfler)

# Arama ve sayma
sayilar = [1, 5, 3, 5, 7, 5]
print("index(5):", sayilar.index(5))
print("count(5):", sayilar.count(5))

# Kopyalama
kopya = sayilar.copy()
kopya.append(100)
print("orijinal:", sayilar, "kopya:", kopya)

# Temizleme
kopya.clear()
print("clear:", kopya)

# Sik kullanilan fonksiyonlar
print("len:", len(sayilar), "min:", min(sayilar), "max:", max(sayilar),
      "sum:", sum(sayilar))

# Kelimeleri uzunluklarina gore siralama
kelimeler = ["python", "c", "java", "javascript"]
kelimeler.sort(key=len)
print(kelimeler)
