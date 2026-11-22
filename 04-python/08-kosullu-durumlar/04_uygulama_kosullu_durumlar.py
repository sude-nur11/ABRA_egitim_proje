# 8.4 Uygulama: Kosullu Durumlar

# 1. Kullanicidan isim, yas ve egitim bilgisini alip ehliyet alabilme durumunu
#    kontrol edin. Ehliyet icin en az 18 yas ve lise mezunu olmak gerekir.
isim = input("Isminiz: ")
yas = int(input("Yasiniz: "))
egitim = input("Egitim durumunuz (ilkokul/ortaokul/lise/universite): ").lower()

if yas >= 18 and egitim in ("lise", "universite"):
    print(f"1- {isim}, ehliyet alabilirsiniz.")
else:
    print(f"1- {isim}, ehliyet alamazsiniz.")

# 2. 2 vize (%60) ve final (%40) notu ile yil sonu ortalamasi hesaplayin.
#    Ortalamaya gore harf notu verin.
vize1 = float(input("1. vize: "))
vize2 = float(input("2. vize: "))
final = float(input("Final: "))
ortalama = ((vize1 + vize2) / 2) * 0.6 + final * 0.4

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

durum = "gecti" if ortalama >= 50 else "kaldi"
print(f"2- Ortalama: {ortalama:.2f}, harf notu: {harf}, durum: {durum}")

# 3. Trafige cikis tarihi alinan bir aracin servis zamanini hesaplayin.
#    1. bakim 1. yil, 2. bakim 2. yil, 3. bakim 3. yil
import datetime

tarih = input("Aracin trafige cikis tarihi (2019/8/9): ")
yil, ay, gun = map(int, tarih.split("/"))
trafige_cikis = datetime.datetime(yil, ay, gun)
fark = datetime.datetime.now() - trafige_cikis
gecen_gun = fark.days

if gecen_gun <= 365:
    print("3- 1. servis araliginda")
elif gecen_gun <= 365 * 2:
    print("3- 2. servis araliginda")
elif gecen_gun <= 365 * 3:
    print("3- 3. servis araliginda")
else:
    print("3- Hatali sure / servis suresi gecmis")
