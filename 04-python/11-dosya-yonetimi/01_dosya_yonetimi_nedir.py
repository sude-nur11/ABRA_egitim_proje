# 11.1 Dosya Yonetimi Nedir?
# Program kapandiginda degiskenlerdeki veriler kaybolur. Verileri kalici olarak
# saklamak icin dosyalara yazar, ihtiyac oldugunda dosyalardan okuruz.
#
# open(dosya_adi, mod, encoding) fonksiyonu ile dosya acilir.
#
# Dosya acma modlari:
#   "r"  -> okuma (varsayilan). Dosya yoksa FileNotFoundError verir.
#   "w"  -> yazma. Dosya yoksa olusturur, varsa ICERIGINI SILER.
#   "a"  -> ekleme. Dosya yoksa olusturur, varsa sonuna ekler.
#   "x"  -> olusturma. Dosya varsa hata verir.
#   "r+" -> hem okuma hem yazma.
#   "b"  -> binary mod (resim, ses gibi dosyalar icin): "rb", "wb"
#   "t"  -> text mod (varsayilan)

import os

# Dosya olusturma
dosya = open("deneme.txt", "w", encoding="utf-8")
dosya.write("Bu dosya Python ile olusturuldu.\n")
dosya.close()               # isimiz bitince dosyayi kapatmaliyiz

# Dosya bilgileri
print("Dosya var mi:", os.path.exists("deneme.txt"))
print("Dosya boyutu:", os.path.getsize("deneme.txt"), "byte")
print("Tam yolu:", os.path.abspath("deneme.txt"))

# Dosyayi okuma
dosya = open("deneme.txt", "r", encoding="utf-8")
print("Icerik:", dosya.read())
print("Dosya adi:", dosya.name, "- Mod:", dosya.mode)
dosya.close()
print("Dosya kapandi mi:", dosya.closed)

# "x" modu: dosya zaten varsa hata verir
try:
    open("deneme.txt", "x")
except FileExistsError:
    print("deneme.txt zaten mevcut, 'x' modu ile olusturulamaz.")

# Olmayan dosyayi okumaya calismak
try:
    open("olmayan_dosya.txt", "r")
except FileNotFoundError:
    print("Dosya bulunamadi.")

# Dosya yolu: goreli (relative) ve mutlak (absolute)
# "deneme.txt"                  -> programin calistigi klasorde
# "klasor/deneme.txt"           -> alt klasorde
# "/home/kullanici/deneme.txt"  -> mutlak yol
print("Calisma dizini:", os.getcwd())

# Dosyayi silme
os.remove("deneme.txt")
print("Silindikten sonra var mi:", os.path.exists("deneme.txt"))
