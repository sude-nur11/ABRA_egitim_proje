# 14.3 Uygulama: Modul Tanimlama
# islemler.py modulunu kullanarak hesap makinesi ve not hesaplama uygulamasi

import islemler
from islemler import harf_notu, ortalama


def hesap_makinesi():
    print("\n--- Hesap Makinesi ---")
    print("Islemler:", ", ".join(islemler.ISLEMLER.keys()))
    try:
        a = float(input("1. sayi: "))
        islem = input("Islem: ")
        b = float(input("2. sayi: "))
    except ValueError:
        print("Gecersiz sayi.")
        return

    fonksiyon = islemler.ISLEMLER.get(islem)
    if fonksiyon is None:
        print("Gecersiz islem.")
        return

    try:
        print(f"Sonuc: {a} {islem} {b} = {fonksiyon(a, b)}")
    except ZeroDivisionError as hata:
        print("Hata:", hata)


def not_hesapla():
    print("\n--- Not Hesaplama ---")
    notlar = []
    while True:
        giris = input("Not girin (bitirmek icin bos birakin): ")
        if giris == "":
            break
        if giris.isdigit():
            notlar.append(int(giris))
        else:
            print("Gecersiz not.")
    ort = ortalama(notlar)
    print(f"Ortalama: {ort:.2f}, harf notu: {harf_notu(ort)}")


def daire():
    r = float(input("Yaricap: "))
    print(f"Alan: {islemler.carp(islemler.PI, islemler.us_al(r, 2)):.2f}")


while True:
    print("\n1- Hesap makinesi  2- Not hesaplama  3- Daire alani  q- Cikis")
    secim = input("Secim: ")
    if secim == "1":
        hesap_makinesi()
    elif secim == "2":
        not_hesapla()
    elif secim == "3":
        daire()
    elif secim == "q":
        break
    else:
        print("Gecersiz secim.")
