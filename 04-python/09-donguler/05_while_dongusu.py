# 9.5 While Dongusu
# while kosul:
#     kosul True oldugu surece calisan kodlar

# 1'den 10'a kadar sayilar
x = 1
while x <= 10:
    print(x, end=" ")
    x += 1          # kosulu degistiren ifade unutulursa sonsuz dongu olusur
print()

# Geri sayim
sayac = 5
while sayac > 0:
    print("Geri sayim:", sayac)
    sayac -= 1
print("Basla!")

# Liste elemanlarini while ile dolasma
isimler = ["Sude", "Ali", "Ayse", "Can"]
i = 0
while i < len(isimler):
    print(f"{i}. eleman: {isimler[i]}")
    i += 1

# 1'den 100'e kadar sayilarin toplami
i = 1
toplam = 0
while i <= 100:
    toplam += i
    i += 1
print("1-100 toplami:", toplam)

# Bir sayinin basamak sayisini bulma
sayi = 987654
basamak = 0
gecici = sayi
while gecici > 0:
    gecici //= 10
    basamak += 1
print(sayi, "sayisi", basamak, "basamaklidir.")

# Kullanicidan dogru deger alana kadar sorma
parola = ""
while parola != "1234":
    parola = input("Parola (1234): ")
print("Giris basarili.")

# while - else: dongu break ile kesilmezse else calisir
n = 0
while n < 3:
    print("n:", n)
    n += 1
else:
    print("Dongu normal sekilde sona erdi.")

# Liste bosalana kadar eleman alma
gorevler = ["rapor yaz", "mail at", "toplanti"]
while gorevler:
    gorev = gorevler.pop(0)
    print("Yapiliyor:", gorev)
print("Tum gorevler bitti.")
