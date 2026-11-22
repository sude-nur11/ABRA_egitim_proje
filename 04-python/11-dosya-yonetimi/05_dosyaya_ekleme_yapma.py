# 11.5 Dosyaya Ekleme Yapma
# "a" (append) modu: dosya yoksa olusturur, varsa mevcut icerigin SONUNA ekler.

with open("ekleme.txt", "w", encoding="utf-8") as dosya:
    dosya.write("1. satir\n")

with open("ekleme.txt", "a", encoding="utf-8") as dosya:
    dosya.write("2. satir\n")
    dosya.write("3. satir\n")

with open("ekleme.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())

# Log (kayit) tutma ornegi
import datetime


def log_yaz(mesaj):
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("uygulama.log", "a", encoding="utf-8") as dosya:
        dosya.write(f"[{zaman}] {mesaj}\n")


log_yaz("Uygulama baslatildi")
log_yaz("Kullanici giris yapti")
log_yaz("Uygulama kapatildi")

with open("uygulama.log", "r", encoding="utf-8") as dosya:
    print(dosya.read())

# Dosyanin BASINA ekleme: once oku, sonra yeni icerikle birlikte yeniden yaz
with open("ekleme.txt", "r", encoding="utf-8") as dosya:
    eski_icerik = dosya.read()
with open("ekleme.txt", "w", encoding="utf-8") as dosya:
    dosya.write("0. satir (basa eklendi)\n" + eski_icerik)

# "r+" modu ile okuyup sonuna yazma
with open("ekleme.txt", "r+", encoding="utf-8") as dosya:
    icerik = dosya.read()          # okuma sonrasi imlec dosyanin sonunda
    dosya.write("4. satir (r+ ile)\n")

with open("ekleme.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())

# "a+" modu: ekleme + okuma. Okumak icin imleci basa almak gerekir.
with open("ekleme.txt", "a+", encoding="utf-8") as dosya:
    dosya.write("5. satir (a+ ile)\n")
    dosya.seek(0)
    print("Satir sayisi:", len(dosya.readlines()))

# Kullanicidan alinan isimleri dosyaya ekleme
while True:
    isim = input("Eklenecek isim (bitirmek icin bos birakin): ")
    if not isim:
        break
    with open("isimler.txt", "a", encoding="utf-8") as dosya:
        dosya.write(isim + "\n")
