# 5.4 Uygulama: Strings
# Slicing ve formatlama ile ilgili uygulamalar

website = "http://www.ornekwebsitesi.com"
kurs = "Python Programlama Dili Egitimi"

# 1. Kursun kac karakterli oldugunu yazdirin
print("1-", len(kurs))

# 2. Website icinden "www" ifadesini alin
print("2-", website[7:10])

# 3. Website icinden "com" ifadesini alin
print("3-", website[-3:])

# 4. Kurs icinden ilk 15 ve son 15 karakteri alin
print("4-", kurs[:15], "|", kurs[-15:])

# 5. Kurs ifadesindeki karakterleri tersten yazdirin
print("5-", kurs[::-1])

# 6. Isim ve yas bilgisini formatlayarak yazdirin
isim, yas = "Sude", 22
print(f"6- Benim adim {isim} ve {yas} yasindayim.")

# 7. Metindeki bosluk sayisi
print("7-", kurs.count(" "))

# 8. Her kelimenin ilk harfini alma
kelimeler = kurs.split()
bas_harfler = ""
for kelime in kelimeler:
    bas_harfler += kelime[0]
print("8-", bas_harfler)

# 9. Kullanicidan alinan ad ve soyadi duzenleme
ad = input("Adiniz: ").strip()
soyad = input("Soyadiniz: ").strip()
print(f"9- {ad.capitalize()} {soyad.upper()}")

# 10. Kullanici adi olusturma: ad + soyadin ilk 3 harfi + dogum yilinin son 2 hanesi
dogum_yili = input("Dogum yiliniz: ")
kullanici_adi = (ad[:3] + soyad[:3] + dogum_yili[-2:]).lower()
print("10- Kullanici adiniz:", kullanici_adi)

# 11. Sifreyi gizleme
sifre = input("Sifre: ")
print("11- Sifreniz:", sifre[0] + "*" * (len(sifre) - 2) + sifre[-1])
