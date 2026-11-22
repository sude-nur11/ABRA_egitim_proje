# 7.4 Uygulama: Atama Operatorleri

# 1. x = 8, y = 5 degerlerini yer degistirin
x, y = 8, 5
x, y = y, x
print("1- x:", x, "y:", y)

# 2. x degerini 3 ile carpip y'ye ekleyin
x, y = 8, 5
y += x * 3
print("2- y:", y)

# 3. y'nin x'e bolumunden kalani y'ye atayin
y %= x
print("3- y:", y)

# 4. x'in y'ninci kuvvetini x'e atayin
x **= y
print("4- x:", x)

# 5. Banka hesabi: bakiye uzerinde islemler
bakiye = 1000
print("5- Baslangic bakiye:", bakiye)
bakiye += 500           # para yatirma
print("   500 TL yatirildi:", bakiye)
bakiye -= 200           # para cekme
print("   200 TL cekildi:", bakiye)
bakiye *= 1.05          # %5 faiz
print("   %5 faiz eklendi:", round(bakiye, 2))

# 6. Kullanicidan alinan sayilarla toplama ve carpim
toplam = 0
carpim = 1
sayi = int(input("1. sayi: "))
toplam += sayi
carpim *= sayi
sayi = int(input("2. sayi: "))
toplam += sayi
carpim *= sayi
sayi = int(input("3. sayi: "))
toplam += sayi
carpim *= sayi
print("6- Toplam:", toplam, "Carpim:", carpim)

# 7. Dikdortgen: kenarlari 2 katina cikarinca alan kac katina cikar?
uzun, kisa = 6, 4
alan1 = uzun * kisa
uzun *= 2
kisa *= 2
alan2 = uzun * kisa
print("7- Ilk alan:", alan1, "Yeni alan:", alan2, "Kat:", alan2 // alan1)

# 8. Saniyeyi dakika ve saniyeye cevirme
saniye = 3725
dakika = saniye // 60
saniye %= 60
print("8-", dakika, "dakika", saniye, "saniye")
