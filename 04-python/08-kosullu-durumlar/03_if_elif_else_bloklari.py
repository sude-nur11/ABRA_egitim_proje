# 8.3 if / elif / else Bloklari
# Birden fazla kosul sirayla kontrol edilir. Ilk True olan kosulun blogu calisir,
# diger kosullara bakilmaz.

# Ornek 1: Not harf karsiligi
puan = int(input("Notunuz (0-100): "))

if puan < 0 or puan > 100:
    print("Gecersiz not.")
elif puan >= 90:
    print("Harf notu: AA")
elif puan >= 85:
    print("Harf notu: BA")
elif puan >= 80:
    print("Harf notu: BB")
elif puan >= 75:
    print("Harf notu: CB")
elif puan >= 65:
    print("Harf notu: CC")
elif puan >= 58:
    print("Harf notu: DC")
elif puan >= 50:
    print("Harf notu: DD")
else:
    print("Harf notu: FF - Kaldiniz")

# Ornek 2: Sayinin pozitif, negatif veya sifir olmasi
sayi = int(input("Bir sayi: "))
if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sifir")

# Ornek 3: Mevsim bulma
ay = int(input("Ay (1-12): "))
if ay in (12, 1, 2):
    print("Kis")
elif ay in (3, 4, 5):
    print("Ilkbahar")
elif ay in (6, 7, 8):
    print("Yaz")
elif ay in (9, 10, 11):
    print("Sonbahar")
else:
    print("Gecersiz ay")

# Neden elif? Sadece if kullanilirsa birden fazla blok calisabilir:
x = 95
if x >= 50:
    print("50'den buyuk")
if x >= 90:
    print("90'dan buyuk")      # ikisi de calisir

if x >= 90:
    print("elif ile: 90'dan buyuk")
elif x >= 50:
    print("elif ile: 50'den buyuk")   # calismaz
