# 7.5 Karsilastirma Operatorleri
# Sonuc her zaman bool (True / False) olur.

a = 10
b = 20

print("a == b :", a == b)    # esit mi
print("a != b :", a != b)    # esit degil mi
print("a > b  :", a > b)     # buyuk mu
print("a < b  :", a < b)     # kucuk mu
print("a >= 10:", a >= 10)   # buyuk esit mi
print("b <= 15:", b <= 15)   # kucuk esit mi

# Sonucu bir degiskende saklama
gecti_mi = 65 >= 50
print("Gecti mi?", gecti_mi, type(gecti_mi))

# Zincirleme karsilastirma
not_ = 75
print("50 <= not < 100:", 50 <= not_ < 100)

# Farkli tipler
print(5 == 5.0)              # True: degerler esit
print(5 == "5")              # False: tipler farkli
print(int("5") == 5)

# String karsilastirma (Unicode sirasina gore)
print("elma" == "elma")
print("elma" == "Elma")      # buyuk/kucuk harf duyarli
print("elma".lower() == "Elma".lower())
print("a" < "b", "apple" < "banana")
print("Z" < "a")             # buyuk harfler kucuklerden once gelir
print(ord("Z"), ord("a"))

# Liste karsilastirma (eleman eleman karsilastirilir)
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] < [1, 2, 4])

# Bool aslinda sayidir
print(True == 1, False == 0)

# Kullanicidan alinan degerlerle
x = int(input("1. sayi: "))
y = int(input("2. sayi: "))
print(f"{x} == {y}: {x == y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
