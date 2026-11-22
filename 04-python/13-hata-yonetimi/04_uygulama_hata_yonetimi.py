# 13.4 Uygulama: Hata Yonetimi

# 1. Liste icindeki elemanlardan sayi olmayanlari ayiklayin
liste = ["1", "2", "5a", "10b", "abc", "10", "50"]
sayilar = []
hatali = []

for eleman in liste:
    try:
        sayilar.append(int(eleman))
    except ValueError:
        hatali.append(eleman)

print("1- Sayilar:", sayilar)
print("   Sayiya cevrilemeyenler:", hatali)

# 2. Kullanici 'q' girene kadar sayi alip, sayi girdiyse ekrana yazdirin;
#    sayi girmediyse 'gecersiz sayi' uyarisi verin
while True:
    giris = input("2- Sayi (cikis icin q): ")
    if giris == "q":
        break
    try:
        sayi = float(giris)
        print("   Girdiginiz sayi:", sayi)
    except ValueError:
        print("   Gecersiz sayi.")

# 3. Kullanicidan alinan liste indeksine gore eleman getirin
meyveler = ["elma", "armut", "muz"]
try:
    indeks = int(input("3- Indeks (0-2): "))
    print("   Eleman:", meyveler[indeks])
except ValueError:
    print("   Indeks sayi olmalidir.")
except IndexError:
    print(f"   Indeks 0 ile {len(meyveler) - 1} arasinda olmalidir.")

# 4. Sozlukten guvenli veri okuma
ogrenci = {"ad": "Sude", "yas": 22}
for anahtar in ["ad", "yas", "bolum"]:
    try:
        print(f"4- {anahtar}: {ogrenci[anahtar]}")
    except KeyError:
        print(f"4- '{anahtar}' bilgisi bulunamadi.")


# 5. Guvenli bolme fonksiyonu
def guvenli_bol(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Sifira bolunemez"
    except TypeError:
        return "Sadece sayilar bolunebilir"


print("5-", guvenli_bol(10, 2), "|", guvenli_bol(10, 0), "|", guvenli_bol("10", 2))

# 6. Dosya okuma hatasi
dosya_adi = input("6- Okunacak dosya adi: ")
try:
    with open(dosya_adi, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"   '{dosya_adi}' bulunamadi.")
finally:
    print("   Dosya islemi tamamlandi.")
