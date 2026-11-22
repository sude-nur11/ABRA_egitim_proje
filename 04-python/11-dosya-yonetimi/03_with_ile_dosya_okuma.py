# 11.3 With ile Dosya Okuma
# with blogu bittiginde dosya OTOMATIK olarak kapatilir.
# Hata olussa bile kapatilir. Dosya islemlerinde onerilen yontemdir.

# Ornek dosya
with open("newfile.txt", "w", encoding="utf-8") as f:
    f.write("Sude Toprak\nAli Yilmaz\nAyse Demir\nCan Kaya\n")

# Klasik yontem: close() unutulabilir
dosya = open("newfile.txt", "r", encoding="utf-8")
print(dosya.read())
dosya.close()

# with ile
with open("newfile.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())
print("with disinda dosya kapali mi:", dosya.closed)

# with ile satir satir okuma
with open("newfile.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir.strip())

# with ile readline
with open("newfile.txt", "r", encoding="utf-8") as dosya:
    ilk = dosya.readline().strip()
    ikinci = dosya.readline().strip()
print("Ilk iki satir:", ilk, "|", ikinci)

# with ile readlines ve liste islemleri
with open("newfile.txt", "r", encoding="utf-8") as dosya:
    isimler = [satir.strip() for satir in dosya.readlines()]
print("Isim listesi:", isimler)
print("Alfabetik:", sorted(isimler))

# Sadece ad ve soyadlari ayirma
with open("newfile.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        ad, soyad = satir.split()
        print(f"Ad: {ad:<6} Soyad: {soyad}")

# seek ile icerigi ikinci kez okuma
with open("newfile.txt", "r", encoding="utf-8") as dosya:
    ilk_okuma = dosya.read()
    ikinci_okuma = dosya.read()      # imlec sonda oldugu icin bos doner
    dosya.seek(0)
    ucuncu_okuma = dosya.read()
print("Ikinci okuma bos mu:", ikinci_okuma == "")
print("Seek sonrasi ayni mi:", ilk_okuma == ucuncu_okuma)

# Ayni anda iki dosyayla calisma: kopyalama
with open("newfile.txt", "r", encoding="utf-8") as kaynak, \
        open("kopya.txt", "w", encoding="utf-8") as hedef:
    hedef.write(kaynak.read().upper())

with open("kopya.txt", "r", encoding="utf-8") as f:
    print(f.read())
