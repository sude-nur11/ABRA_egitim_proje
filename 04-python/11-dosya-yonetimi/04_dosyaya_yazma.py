# 11.4 Dosyaya Yazma
# "w" modu: dosya yoksa olusturur, varsa onceki icerigi SILIP yeniden yazar.

# write(): string yazar, otomatik satir sonu eklemez
with open("yazma.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Sude Toprak\n")
    dosya.write("Ali Yilmaz\n")

with open("yazma.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())

# Tekrar "w" ile acinca eski icerik silinir
with open("yazma.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Eski icerik silindi, bu yeni icerik.\n")

with open("yazma.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())

# Sayilar yazilmadan once str'ye cevrilmelidir
with open("sayilar.txt", "w", encoding="utf-8") as dosya:
    for i in range(1, 6):
        dosya.write(str(i) + "\n")
    # dosya.write(10)  -> TypeError

# writelines(): bir listeyi yazar (satir sonlari elle eklenmeli)
meyveler = ["elma", "armut", "muz"]
with open("meyveler.txt", "w", encoding="utf-8") as dosya:
    dosya.writelines([m + "\n" for m in meyveler])

# print fonksiyonu ile dosyaya yazma
with open("print_ile.txt", "w", encoding="utf-8") as dosya:
    print("print ile dosyaya yazildi", file=dosya)
    print("Ad:", "Sude", "Yas:", 22, file=dosya)

# Tablo seklinde veri yazma (CSV benzeri)
ogrenciler = [("Sude", 90), ("Ali", 75), ("Ayse", 85)]
with open("notlar.csv", "w", encoding="utf-8") as dosya:
    dosya.write("ad,not\n")
    for ad, puan in ogrenciler:
        dosya.write(f"{ad},{puan}\n")

for dosya_adi in ["sayilar.txt", "meyveler.txt", "print_ile.txt", "notlar.csv"]:
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        print(f"--- {dosya_adi} ---")
        print(dosya.read())

# Kullanicidan alinan bilgiyi dosyaya yazma
isim = input("Gunluge yazilacak not: ")
with open("gunluk.txt", "w", encoding="utf-8") as dosya:
    dosya.write(isim + "\n")
print("Not gunluk.txt dosyasina kaydedildi.")
