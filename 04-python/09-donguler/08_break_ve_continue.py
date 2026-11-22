# 9.8 Break ve Continue
# break   : donguyu tamamen sonlandirir
# continue: o anki iterasyonu atlar, donguye bir sonraki adimdan devam eder

# break ornegi
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print("-> 5'e gelince durdu")

# continue ornegi
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print("-> 5 atlandi")

# Stringde break
isim = "Sude Toprak"
for harf in isim:
    if harf == " ":
        break
    print(harf, end="")
print(" -> bosluga kadar")

# Stringde continue: sesli harfleri atlama
for harf in "programlama":
    if harf in "aeiou":
        continue
    print(harf, end="")
print(" -> sessiz harfler")

# while ile break
x = 0
while x < 10:
    x += 1
    if x == 7:
        break
    print(x, end=" ")
print("-> 7'de durdu")

# while ile continue: 1-100 arasi tek sayilarin toplami
x = 0
toplam = 0
while x < 100:
    x += 1
    if x % 2 == 0:
        continue
    toplam += x
print("Tek sayilarin toplami:", toplam)

# while True ve break: kullanici 'q' yazana kadar sayi topla
toplam = 0
while True:
    giris = input("Sayi (cikis icin q): ")
    if giris == "q":
        break
    if not giris.isdigit():
        print("Lutfen sayi girin.")
        continue
    toplam += int(giris)
print("Girilen sayilarin toplami:", toplam)

# break ile else'in calismamasi
for sayi in [2, 4, 6, 7, 8]:
    if sayi % 2 == 1:
        print("Ilk tek sayi:", sayi)
        break
else:
    print("Tek sayi bulunamadi.")
