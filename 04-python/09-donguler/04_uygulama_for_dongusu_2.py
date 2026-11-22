# 9.4 Uygulama: For Dongusu - 2

# 1. Girilen bir sayinin asal olup olmadigini bulun
sayi = int(input("Sayi: "))
asal_mi = True
if sayi < 2:
    asal_mi = False
for i in range(2, sayi):
    if sayi % i == 0:
        asal_mi = False
        break
print(f"1- {sayi} asal {'sayidir' if asal_mi else 'sayi degildir'}")

# 2. Girilen sayinin faktoriyelini hesaplayin
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"2- {sayi}! = {faktoriyel}")

# 3. Bir metindeki sesli harfleri bulun
metin = input("Bir metin girin: ").lower()
sesliler = "aeiou"
bulunan = []
for harf in metin:
    if harf in sesliler and harf not in bulunan:
        bulunan.append(harf)
print("3- Metindeki sesli harfler:", bulunan)

# 4. Bir metindeki kelimelerin kac kez gectigini sayin
sayac = {}
for kelime in metin.split():
    if kelime in sayac:
        sayac[kelime] += 1
    else:
        sayac[kelime] = 1
print("4-", sayac)

# 5. Carpim tablosunu ekrana yazdirin
print("5- Carpim tablosu")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

# 6. Yildizlarla ucgen cizdirin
print("6-")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# 7. Iki listenin ortak elemanlari
liste1 = [1, 2, 3, 4, 5, 6]
liste2 = [4, 5, 6, 7, 8]
ortak = []
for eleman in liste1:
    if eleman in liste2:
        ortak.append(eleman)
print("7- Ortak elemanlar:", ortak)
