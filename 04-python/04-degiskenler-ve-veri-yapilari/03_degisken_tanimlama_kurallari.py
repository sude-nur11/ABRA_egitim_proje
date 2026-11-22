# 4.3 Degisken Tanimlama Kurallari

# 1. Degisken adi harf veya alt cizgi (_) ile baslamalidir.
isim = "gecerli"
_isim = "gecerli"
# 1isim = "gecersiz"   -> SyntaxError

# 2. Degisken adi sadece harf, rakam ve _ icerebilir.
ogrenci1 = "gecerli"
ogrenci_no = 101
# ogrenci-no = 101     -> SyntaxError (- isareti kullanilamaz)
# ogrenci no = 101     -> SyntaxError (bosluk kullanilamaz)

# 3. Buyuk / kucuk harf duyarlidir.
sayi = 1
Sayi = 2
SAYI = 3
print(sayi, Sayi, SAYI)   # ucu farkli degiskendir

# 4. Python'un anahtar kelimeleri degisken adi olamaz.
import keyword
print("Anahtar kelimeler:", keyword.kwlist)
print("'for' anahtar kelime mi?", keyword.iskeyword("for"))
print("'ogrenci' anahtar kelime mi?", keyword.iskeyword("ogrenci"))
# for = 5   -> SyntaxError

# 5. Hazir fonksiyon isimlerini (print, list, str, sum ...) kullanmaktan kacinin.
# Hata vermez ama o fonksiyonun yerine gecer:
# print = 5
# print("merhaba")  -> TypeError: 'int' object is not callable

# Isimlendirme stilleri
ogrenci_adi_soyadi = "snake_case"     # Python'da degiskenler icin onerilen
ogrenciAdiSoyadi = "camelCase"
OgrenciAdiSoyadi = "PascalCase"       # Python'da sinif isimleri icin kullanilir
print(ogrenci_adi_soyadi, ogrenciAdiSoyadi, OgrenciAdiSoyadi)

# Anlamli isimler kullanmak kodun okunabilirligini artirir
a = 3000           # kotu: ne oldugu anlasilmiyor
aylik_maas = 3000  # iyi: ne oldugu belli
print(a == aylik_maas)

# Degisken adlarinda Turkce karakter (c, g, i, o, s, u'nun Turkce halleri) kullanilabilir
# ama onerilmez. Sadece Ingilizce alfabe kullanmak en guvenli yoldur.
yas = 22
print("yas:", yas)
