# 4.4 Uygulama: Degisken Tanimlama
# Bir ogrencinin bilgilerini degiskenlerde tutup ekrana yazdirma

# Ogrenci bilgileri
ogrenci_adi = "Sude"
ogrenci_soyadi = "Toprak"
ogrenci_no = 2024101
bolum = "Bilgisayar Muhendisligi"
sinif = 3

# Ders notlari
vize = 70
final = 85
proje = 90

# Agirlikli ortalama: vize %30, final %50, proje %20
ortalama = vize * 0.3 + final * 0.5 + proje * 0.2
gecti_mi = ortalama >= 50

print("========== OGRENCI BILGI KARTI ==========")
print("Ad Soyad  :", ogrenci_adi, ogrenci_soyadi)
print("Numara    :", ogrenci_no)
print("Bolum     :", bolum)
print("Sinif     :", sinif)
print("-----------------------------------------")
print("Vize      :", vize)
print("Final     :", final)
print("Proje     :", proje)
print("Ortalama  :", ortalama)
print("Gecti mi? :", gecti_mi)
print("=========================================")

# Uygulama 2: Dikdortgenin alan ve cevresini hesaplama
uzun_kenar = 12
kisa_kenar = 5
alan = uzun_kenar * kisa_kenar
cevre = 2 * (uzun_kenar + kisa_kenar)
print("Dikdortgen alani:", alan, "- cevresi:", cevre)

# Uygulama 3: Dairenin alani ve cevresi
pi = 3.14
yaricap = 7
daire_alan = pi * yaricap ** 2
daire_cevre = 2 * pi * yaricap
print("Daire alani:", daire_alan, "- cevresi:", daire_cevre)

# Uygulama 4: Kullanicidan alinan bilgilerle selamlama
kullanici_adi = input("Adiniz: ")
dogum_yili = int(input("Dogum yiliniz: "))
yas = 2026 - dogum_yili
print("Merhaba", kullanici_adi + ",", "bu yil", yas, "yasindasiniz.")
