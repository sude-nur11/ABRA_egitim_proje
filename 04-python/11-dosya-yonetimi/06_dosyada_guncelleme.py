# 11.6 Dosyada Guncelleme
# Dosyanin ortasindaki bir satiri dogrudan degistiremeyiz.
# Yontem: dosyayi oku -> veriyi bellekte degistir -> dosyaya yeniden yaz.

with open("guncelleme.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Sude Toprak\nAli Yilmaz\nAyse Demir\n")

# 1. Dosyanin sonuna ekleme
with open("guncelleme.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Can Kaya\n")

# 2. Dosyanin basina ekleme
with open("guncelleme.txt", "r+", encoding="utf-8") as dosya:
    icerik = dosya.read()
    dosya.seek(0)                      # imleci basa al
    dosya.write("Deniz Ak\n" + icerik)

with open("guncelleme.txt", "r", encoding="utf-8") as dosya:
    print("Basa ve sona ekleme:\n" + dosya.read())

# 3. Araya ekleme: listeye cevirip insert ile
with open("guncelleme.txt", "r+", encoding="utf-8") as dosya:
    liste = dosya.readlines()
    liste.insert(2, "Mehmet Celik\n")
    dosya.seek(0)
    dosya.writelines(liste)

with open("guncelleme.txt", "r", encoding="utf-8") as dosya:
    print("Araya ekleme:\n" + dosya.read())

# 4. Belirli bir satiri degistirme
with open("guncelleme.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()

satirlar = [s.replace("Ali Yilmaz", "Ali Ozturk") for s in satirlar]

with open("guncelleme.txt", "w", encoding="utf-8") as dosya:
    dosya.writelines(satirlar)

# 5. Belirli bir satiri silme
with open("guncelleme.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()

with open("guncelleme.txt", "w", encoding="utf-8") as dosya:
    for satir in satirlar:
        if not satir.startswith("Can"):
            dosya.write(satir)

with open("guncelleme.txt", "r", encoding="utf-8") as dosya:
    print("Degistirme ve silme sonrasi:\n" + dosya.read())

# 6. truncate ile dosyanin bir kismini silme
with open("guncelleme.txt", "r+", encoding="utf-8") as dosya:
    dosya.readline()
    dosya.readline()
    dosya.truncate()                   # imlecten sonrasini siler

with open("guncelleme.txt", "r", encoding="utf-8") as dosya:
    print("truncate sonrasi:\n" + dosya.read())
