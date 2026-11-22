# 6.2 Liste Tanimlama

# Koseli parantez ile
sayilar = [1, 2, 3, 4, 5]
markalar = ["BMW", "Mercedes", "Opel", "Mazda"]
bos_liste = []

# list() fonksiyonu ile
bos_liste2 = list()
harfler = list("python")
araliktaki_sayilar = list(range(1, 11))

print(sayilar)
print(markalar)
print(bos_liste, bos_liste2)
print(harfler)
print(araliktaki_sayilar)

# Elemanlara erisme
print(markalar[0])
print(markalar[-1])
print(markalar[1:3])       # dilimleme stringlerle aynidir
print(markalar[::-1])

# Eleman guncelleme
markalar[2] = "Toyota"
print(markalar)
markalar[0:2] = ["Audi", "Volvo"]
print(markalar)

# Listeleri birlestirme ve cogaltma
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
print(liste1 + liste2)
print(liste1 * 3)
print([0] * 10)

# Ic ice listeler
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matris[1])           # [4, 5, 6]
print(matris[1][2])        # 6
print(matris[2][0])        # 7

# Uzunluk, min, max, sum
print(len(sayilar), min(sayilar), max(sayilar), sum(sayilar))

# Eleman listede var mi?
print("BMW" in markalar)
print("Opel" not in markalar)

# Liste -> string, string -> liste
cumle = "Python ogrenmek cok keyifli"
kelimeler = cumle.split()
print(kelimeler)
print(" ".join(kelimeler))
