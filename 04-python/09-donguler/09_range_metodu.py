# 9.9 Range Metodu
# range(baslangic, bitis, adim) -> bitis degeri DAHIL DEGILDIR

print(range(5))
print(list(range(5)))              # [0, 1, 2, 3, 4]
print(list(range(3, 8)))           # [3, 4, 5, 6, 7]
print(list(range(0, 20, 3)))       # [0, 3, 6, 9, 12, 15, 18]
print(list(range(10, 0, -1)))      # geri sayim
print(list(range(10, 0, -2)))
print(list(range(5, 0)))           # bos liste: adim pozitifken baslangic > bitis

# for dongusunde range
for i in range(5):
    print("Merhaba", i)

# 1'den n'e kadar sayilarin toplami
n = 50
toplam = 0
for i in range(1, n + 1):
    toplam += i
print(f"1-{n} toplami:", toplam)
print("sum ile:", sum(range(1, n + 1)))

# Cift sayilar
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# Liste indekslerinde range kullanimi
meyveler = ["elma", "armut", "muz"]
for i in range(len(meyveler)):
    print(i, meyveler[i])

# Listeyi tersten gezme
for i in range(len(meyveler) - 1, -1, -1):
    print(meyveler[i])

# range nesnesinin ozellikleri
r = range(0, 100, 5)
print("Uzunluk:", len(r))
print("Ilk:", r[0], "Son:", r[-1])
print("50 icinde mi:", 50 in r)
print("51 icinde mi:", 51 in r)

# Carpim tablosu
sayi = 7
for i in range(1, 11):
    print(f"{sayi} x {i:2} = {sayi * i}")

# range ile liste olusturma
kareler = [x ** 2 for x in range(1, 11)]
print(kareler)
