# 9.7 Uygulama: While Dongusu - 2
# Sayi tahmin oyunu: 1-100 arasinda tutulan sayiyi 5 hakta bilin.
# Her yanlis tahminde hak 1 azalir, puan 20 azalir.

import random

sayi = random.randint(1, 100)
can = int(input("Kac hak kullanmak istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmininiz: "))

    if sayi == tahmin:
        puan = 100 - (100 / can) * (sayac - 1)
        print(f"Tebrikler {sayac}. defada bildiniz. Toplam puaniniz: {puan:.0f}")
        break
    elif sayi > tahmin:
        print("Yukari")
    else:
        print("Asagi")

    if hak == 0:
        print(f"Hakkiniz bitti. Tutulan sayi: {sayi}")
    else:
        print(f"Kalan hak: {hak}")

# 2. Menu uygulamasi: kullanici cikis yapana kadar calisir
print("\n--- Alisveris Listesi ---")
liste = []
while True:
    print("1- Ekle  2- Sil  3- Listele  4- Cikis")
    secim = input("Secim: ")

    if secim == "1":
        liste.append(input("Urun: "))
    elif secim == "2":
        urun = input("Silinecek urun: ")
        if urun in liste:
            liste.remove(urun)
        else:
            print("Urun listede yok.")
    elif secim == "3":
        print("Liste:", liste if liste else "bos")
    elif secim == "4":
        print("Cikis yapildi.")
        break
    else:
        print("Gecersiz secim.")
