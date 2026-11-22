# 9.1 Dongu Nedir?
# Dongu, bir kod blogunun belirli sayida ya da bir kosul saglandigi surece
# tekrar tekrar calistirilmasini saglar.
# Python'da iki tur dongu vardir:
#   for   -> bir dizinin (liste, string, range ...) elemanlari uzerinde gezinir
#   while -> kosul True oldugu surece calisir

# Dongu olmadan 1'den 5'e kadar sayilari yazdirmak:
print(1)
print(2)
print(3)
print(4)
print(5)

# for dongusu ile:
for sayi in range(1, 6):
    print("for:", sayi)

# while dongusu ile:
sayac = 1
while sayac <= 5:
    print("while:", sayac)
    sayac += 1

# Dongu olmadan liste elemanlarinin toplami:
notlar = [70, 85, 90, 45, 60]
toplam = notlar[0] + notlar[1] + notlar[2] + notlar[3] + notlar[4]
print("Toplam (dongusuz):", toplam)

# Dongu ile (liste ne kadar uzun olursa olsun calisir):
toplam = 0
for n in notlar:
    toplam += n
print("Toplam (dongu ile):", toplam)

# Dongu terimleri
# - iterasyon: dongunun her bir tekrari
# - iterable : uzerinde dongu kurulabilen nesne (list, str, tuple, dict, set, range)
# - sonsuz dongu: kosulu hic False olmayan dongu (while True gibi)
iterasyon = 0
for harf in "Python":
    iterasyon += 1
    print(f"{iterasyon}. iterasyon -> {harf}")

# Hangi dongu ne zaman?
# Tekrar sayisi biliniyorsa / bir dizi geziliyorsa -> for
# Tekrar sayisi bilinmiyor, bir kosula bagliysa     -> while
bakiye = 1000
ay = 0
while bakiye < 2000:
    bakiye *= 1.1
    ay += 1
print(f"Bakiye {ay} ayda 2000'i gecti: {bakiye:.2f}")
