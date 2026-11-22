# 11.7 Not Uygulamasi: Not Girisi
# Ogrenci adini ve 3 notunu alip "sinav_notlari.txt" dosyasina kaydeden uygulama.
# Kayitlar "Ad Soyad: not1,not2,not3" formatinda tutulur.

DOSYA_ADI = "sinav_notlari.txt"


def not_gir():
    ad = input("Ogrenci adi: ").strip()
    soyad = input("Ogrenci soyadi: ").strip()
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")

    # Notlarin sayi olup olmadigini kontrol et
    for n in (not1, not2, not3):
        if not n.isdigit() or not 0 <= int(n) <= 100:
            print("Notlar 0-100 arasinda tam sayi olmalidir.")
            return

    with open(DOSYA_ADI, "a", encoding="utf-8") as dosya:
        dosya.write(f"{ad} {soyad}: {not1},{not2},{not3}\n")
    print("Kayit eklendi.")


def notlari_goster():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
    except FileNotFoundError:
        print("Henuz kayit yok.")
        return
    print("--- Kayitli notlar ---")
    print(icerik if icerik else "Henuz kayit yok.")


while True:
    print("\n1- Not gir")
    print("2- Notlari goster")
    print("3- Cikis")
    islem = input("Islem: ")

    if islem == "1":
        not_gir()
    elif islem == "2":
        notlari_goster()
    elif islem == "3":
        break
    else:
        print("Yanlis secim.")
