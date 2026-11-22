# 11.8 Not Uygulamasi: Ogrenci Degerlendirmesi
# "sinav_notlari.txt" dosyasindaki kayitlari okuyup her ogrencinin ortalamasini
# ve harf notunu hesaplar, sonucu "sonuclar.txt" dosyasina yazar.
# (Once 07_not_uygulamasi_not_girisi.py ile kayit eklenmelidir.)

GIRIS_DOSYASI = "sinav_notlari.txt"
SONUC_DOSYASI = "sonuclar.txt"


def not_hesapla(satir):
    satir = satir.strip()
    ad_soyad, notlar = satir.split(":")
    not_listesi = [int(n) for n in notlar.split(",")]

    ortalama = sum(not_listesi) / len(not_listesi)

    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 85:
        harf = "BA"
    elif ortalama >= 80:
        harf = "BB"
    elif ortalama >= 75:
        harf = "CB"
    elif ortalama >= 70:
        harf = "CC"
    elif ortalama >= 65:
        harf = "DC"
    elif ortalama >= 60:
        harf = "DD"
    elif ortalama >= 50:
        harf = "FD"
    else:
        harf = "FF"

    return f"{ad_soyad}: ortalama {ortalama:.2f}, harf notu {harf}\n"


def ortalamalari_oku():
    try:
        with open(GIRIS_DOSYASI, "r", encoding="utf-8") as dosya:
            satirlar = [s for s in dosya if s.strip()]
    except FileNotFoundError:
        print(f"{GIRIS_DOSYASI} bulunamadi. Once not girisi yapin.")
        return []
    return [not_hesapla(s) for s in satirlar]


def sonuclari_kaydet(sonuclar):
    with open(SONUC_DOSYASI, "w", encoding="utf-8") as dosya:
        dosya.writelines(sonuclar)
    print(f"{len(sonuclar)} ogrencinin sonucu {SONUC_DOSYASI} dosyasina kaydedildi.")


sonuclar = ortalamalari_oku()
if sonuclar:
    print("--- Ogrenci Degerlendirmesi ---")
    for s in sonuclar:
        print(s, end="")

    gecenler = [s for s in sonuclar if not s.strip().endswith(("FD", "FF"))]
    print(f"\nToplam: {len(sonuclar)}, gecen: {len(gecenler)}, "
          f"kalan: {len(sonuclar) - len(gecenler)}")
    sonuclari_kaydet(sonuclar)
