# 10.10 Uygulama: Bankamatik
# Hesap bakiyesi yetersizse ek hesaptan kullanma secenegi sunan bankamatik uygulamasi

sudeHesap = {
    "ad": "Sude Toprak",
    "hesapNo": "13245678",
    "bakiye": 3000,
    "ekHesap": 2000,
}

aliHesap = {
    "ad": "Ali Yilmaz",
    "hesapNo": "12345678",
    "bakiye": 2000,
    "ekHesap": 1000,
}


def bakiye_sorgula(hesap):
    print(f"{hesap['ad']} | Bakiye: {hesap['bakiye']} TL | Ek hesap: {hesap['ekHesap']} TL")


def para_yatir(hesap, miktar):
    hesap["bakiye"] += miktar
    print(f"{miktar} TL yatirildi.")
    bakiye_sorgula(hesap)


def para_cek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranizi alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ek_hesap_kullanimi = input("Ek hesap kullanilsin mi? (e/h): ")
            if ek_hesap_kullanimi == "e":
                ek_hesap_kullanilacak = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ek_hesap_kullanilacak
                print("Paranizi alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
        else:
            print("Uzgunuz, bakiye yetersiz.")
    bakiye_sorgula(hesap)


hesaplar = {"1": sudeHesap, "2": aliHesap}

while True:
    print("\n1- Bakiye sorgula  2- Para cek  3- Para yatir  q- Cikis")
    secim = input("Islem: ")
    if secim == "q":
        print("Iyi gunler.")
        break
    if secim not in ("1", "2", "3"):
        print("Gecersiz islem.")
        continue

    hesap = hesaplar.get(input("Hesap (1- Sude, 2- Ali): "))
    if hesap is None:
        print("Hesap bulunamadi.")
        continue

    if secim == "1":
        bakiye_sorgula(hesap)
    elif secim == "2":
        para_cek(hesap, int(input("Cekilecek miktar: ")))
    else:
        para_yatir(hesap, int(input("Yatirilacak miktar: ")))
