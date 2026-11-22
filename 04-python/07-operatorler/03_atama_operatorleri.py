# 7.3 Atama Operatorleri

x = 10
print("x =", x)

x += 5          # x = x + 5
print("x += 5   ->", x)

x -= 3          # x = x - 3
print("x -= 3   ->", x)

x *= 2          # x = x * 2
print("x *= 2   ->", x)

x /= 4          # x = x / 4 (sonuc float olur)
print("x /= 4   ->", x)

x //= 2         # x = x // 2
print("x //= 2  ->", x)

x **= 3         # x = x ** 3
print("x **= 3  ->", x)

x %= 7          # x = x % 7
print("x %= 7   ->", x)

# Stringlerde += ve *=
mesaj = "Merhaba"
mesaj += " Dunya"
print(mesaj)
cizgi = "-"
cizgi *= 20
print(cizgi)

# Listelerde +=
liste = [1, 2]
liste += [3, 4]
print(liste)

# Coklu atama
a, b, c = 1, 2, 3
print(a, b, c)

# Deger degistirme (swap)
a, b = b, a
print("a:", a, "b:", b)

# Tuple / liste acma
sayilar = (10, 20, 30)
s1, s2, s3 = sayilar
print(s1, s2, s3)
ilk, *kalanlar = [1, 2, 3, 4, 5]
print(ilk, kalanlar)

# Walrus operatoru := (Python 3.8+): ifadenin icinde atama yapar
if (uzunluk := len("Python")) > 3:
    print("Uzunluk:", uzunluk)
