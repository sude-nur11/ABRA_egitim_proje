# 6.11 Value ve Referans Tipler
# Deger tipleri (int, float, str, bool, tuple) degistirilemez (immutable).
# Referans tipleri (list, dict, set) degistirilebilir (mutable) ve
# atama yapildiginda kopyalanmaz, AYNI nesneyi gosterirler.

# Deger tipi ornegi
x = 5
y = x
x = 10
print("x:", x, "y:", y)                 # y etkilenmez
print(id(x), id(y))

metin1 = "python"
metin2 = metin1
metin1 = metin1.upper()
print(metin1, metin2)                   # metin2 etkilenmez

# Referans tipi ornegi
a = ["elma", "armut"]
b = a                                   # b, a ile ayni listeyi gosterir
b.append("muz")
print("a:", a)                          # a da degisti!
print("b:", b)
print("Ayni nesne mi?", a is b, id(a) == id(b))

# Sozluklerde de ayni durum gecerlidir
ayar1 = {"tema": "koyu"}
ayar2 = ayar1
ayar2["tema"] = "acik"
print(ayar1)

# Cozum: kopya olusturmak
c = a.copy()          # ya da a[:] veya list(a)
c.append("kiraz")
print("a:", a, "c:", c, "Ayni nesne mi?", a is c)

# Ic ice yapilarda copy() yetmez (shallow copy)
import copy
matris = [[1, 2], [3, 4]]
yuzeysel = matris.copy()
derin = copy.deepcopy(matris)
matris[0][0] = 99
print("yuzeysel kopya:", yuzeysel)      # ic liste ortak oldugu icin degisti
print("derin kopya:", derin)            # etkilenmedi

# == degerleri, is nesnenin kendisini karsilastirir
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2, l1 is l2)
