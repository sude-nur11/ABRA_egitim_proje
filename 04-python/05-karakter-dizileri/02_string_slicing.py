# 5.2 String Slicing (Dilimleme)
# Indeksleme: metin[indeks] -> indeks 0'dan baslar, negatif indeks sondan sayar.

metin = "Python Programlama"
#        012345678901234567

print(metin[0])      # P
print(metin[1])      # y
print(metin[7])      # P
print(metin[-1])     # a  (son karakter)
print(metin[-2])     # m
print(metin[len(metin) - 1])   # son karakter (alternatif yol)

# Dilimleme: metin[baslangic:bitis:adim]  -> bitis indeksi DAHIL DEGILDIR
print(metin[0:6])    # Python
print(metin[7:18])   # Programlama
print(metin[:6])     # bastan 6. indekse kadar
print(metin[7:])     # 7. indeksten sona kadar
print(metin[:])      # tamami
print(metin[-11:])   # son 11 karakter
print(metin[-11:-5]) # Progra

# Adim (step) kullanimi
print(metin[::2])    # ikiser atlayarak
print(metin[1::2])   # 1'den baslayip ikiser atlayarak
print(metin[::-1])   # tersten yazdirma
print(metin[5::-1])  # 5. indeksten basa dogru

# Ornek: Palindrom kontrolu
kelime = "kayak"
print(kelime, "palindrom mu?", kelime == kelime[::-1])

# Ornek: E-posta adresinden kullanici adini alma
email = "sude.toprak@ornek.com"
kullanici = email[:email.index("@")]
alan_adi = email[email.index("@") + 1:]
print("Kullanici:", kullanici, "- Alan adi:", alan_adi)

# Ornek: Tarihi parcalarina ayirma
tarih = "21.11.2026"
gun = tarih[:2]
ay = tarih[3:5]
yil = tarih[-4:]
print("Gun:", gun, "Ay:", ay, "Yil:", yil)

# Hatali indeks
try:
    print(metin[100])
except IndexError as hata:
    print("Hata:", hata)
print(metin[5:100])  # dilimlemede tasma hata vermez
