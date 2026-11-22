# 7.2 Aritmetik Operatorler

x = 17
y = 5

print("Toplama       x + y  =", x + y)
print("Cikarma       x - y  =", x - y)
print("Carpma        x * y  =", x * y)
print("Bolme         x / y  =", x / y)      # sonuc her zaman float
print("Tam bolme     x // y =", x // y)     # ondalik kisim atilir
print("Mod (kalan)   x % y  =", x % y)
print("Us alma       x ** y =", x ** y)

# Negatif sayilarda tam bolme asagi yuvarlar
print(-17 // 5, -17 % 5)

# Float ile islemler
print(7.5 + 2, 7.5 // 2, 7.5 % 2)

# Kayan nokta hassasiyeti
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))

# Karekok ve kupkok us operatoru ile
print("25'in karekoku:", 25 ** 0.5)
print("27'nin kupkoku:", round(27 ** (1 / 3), 2))

# divmod: bolum ve kalani birlikte verir
bolum, kalan = divmod(x, y)
print("divmod:", bolum, kalan)

# Mod ile tek/cift kontrolu
sayi = 24
print(sayi, "cift mi?", sayi % 2 == 0)

# Basamaklarina ayirma
sayi = 4729
birler = sayi % 10
onlar = sayi // 10 % 10
yuzler = sayi // 100 % 10
binler = sayi // 1000
print("Basamaklar:", binler, yuzler, onlar, birler)
print("Basamak toplami:", binler + yuzler + onlar + birler)

# Ortalama hesaplama
n1, n2, n3 = 70, 85, 92
print("Ortalama:", (n1 + n2 + n3) / 3)

# Abs ve round
print(abs(-12), round(3.14159, 3))
