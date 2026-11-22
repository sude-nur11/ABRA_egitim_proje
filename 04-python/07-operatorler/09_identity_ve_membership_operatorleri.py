# 7.9 Identity (Kimlik) ve Membership (Uyelik) Operatorleri

# --- Identity: is, is not ---
# Iki degiskenin bellekte AYNI nesneyi gosterip gostermedigini kontrol eder.
# == ise sadece degerlerin esitligine bakar.

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x == y:", x == y)      # True: degerler ayni
print("x is y:", x is y)      # False: farkli nesneler
print("x is z:", x is z)      # True: ayni nesne
print("x is not y:", x is not y)
print("id:", id(x), id(y), id(z))

# None kontrolunde is kullanilir
sonuc = None
print("sonuc is None:", sonuc is None)

# Kucuk sayilar ve kisa stringler Python tarafindan onbellege alinir
a = 100
b = 100
print("a is b:", a is b)

# --- Membership: in, not in ---
# Bir degerin bir dizi (liste, string, tuple, set, dict) icinde olup olmadigini kontrol eder.

meyveler = ["elma", "armut", "muz"]
print("'elma' in meyveler:", "elma" in meyveler)
print("'kiraz' not in meyveler:", "kiraz" not in meyveler)

metin = "Python Programlama"
print("'Python' in metin:", "Python" in metin)
print("'python' in metin:", "python" in metin)    # buyuk/kucuk harf duyarli

sayilar = (1, 2, 3)
print("2 in sayilar:", 2 in sayilar)

ogrenci = {"ad": "Sude", "yas": 22}
print("'ad' in ogrenci:", "ad" in ogrenci)        # anahtarlarda arar
print("'Sude' in ogrenci:", "Sude" in ogrenci)
print("'Sude' in values:", "Sude" in ogrenci.values())

# Ornek: sesli harf sayma
cumle = "python programlama dili"
sesliler = "aeiioouu"
sayac = 0
for harf in cumle:
    if harf in sesliler:
        sayac += 1
print("Sesli harf sayisi:", sayac)
