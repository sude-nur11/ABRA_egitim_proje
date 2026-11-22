# 11.2 Dosya Okuma

# Ornek dosyayi olusturalim
with open("newfile.txt", "w", encoding="utf-8") as f:
    f.write("Sude Toprak\nAli Yilmaz\nAyse Demir\nCan Kaya\n")

# 1. read(): tum icerigi tek bir string olarak okur
dosya = open("newfile.txt", "r", encoding="utf-8")
icerik = dosya.read()
print("read():")
print(icerik)
dosya.close()

# 2. read(n): ilk n karakteri okur
dosya = open("newfile.txt", "r", encoding="utf-8")
print("read(4):", dosya.read(4))
print("read(7):", dosya.read(7))     # kaldigi yerden devam eder
dosya.close()

# 3. readline(): her cagrida bir satir okur
dosya = open("newfile.txt", "r", encoding="utf-8")
print("1. satir:", dosya.readline(), end="")
print("2. satir:", dosya.readline(), end="")
dosya.close()

# 4. readlines(): tum satirlari liste olarak dondurur
dosya = open("newfile.txt", "r", encoding="utf-8")
satirlar = dosya.readlines()
print("readlines():", satirlar)
dosya.close()

# 5. for dongusu ile satir satir okuma (buyuk dosyalar icin en verimli yol)
dosya = open("newfile.txt", "r", encoding="utf-8")
for i, satir in enumerate(dosya, start=1):
    print(f"{i}: {satir.strip()}")
dosya.close()

# 6. Imlec (cursor) konumu: tell() ve seek()
dosya = open("newfile.txt", "r", encoding="utf-8")
print("Baslangic konumu:", dosya.tell())
dosya.read(11)
print("11 karakter okunduktan sonra:", dosya.tell())
dosya.seek(0)                        # imleci basa al
print("Basa donunce okunan:", dosya.readline().strip())
dosya.close()

# 7. Hata yonetimi ile okuma
try:
    dosya = open("olmayan.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Dosya okunamadi: dosya bulunamadi.")

# 8. Okunan veriyi isleme: satir ve kelime sayisi
dosya = open("newfile.txt", "r", encoding="utf-8")
metin = dosya.read()
dosya.close()
print("Satir sayisi:", len(metin.splitlines()))
print("Kelime sayisi:", len(metin.split()))
print("Karakter sayisi:", len(metin))
