# 5.6 Uygulama: String
# String metotlari ile ilgili uygulamalar

website = "http://www.ornekwebsitesi.com"
kurs = "Python Programlama Dili Egitimi"

# 1. 'kurs' ifadesindeki tum karakterleri buyuk ve kucuk harf yapin
print("1-", kurs.upper(), "|", kurs.lower())

# 2. 'kurs' ifadesinde kac tane 'a' karakteri var?
print("2-", kurs.lower().count("a"))

# 3. 'www' ile baslayip 'com' ile bitiyor mu?
adres = website.replace("http://", "")
print("3-", adres.startswith("www"), adres.endswith("com"))

# 4. 'kurs' icinde 'Dili' kelimesinin konumunu bulun
print("4-", kurs.find("Dili"))

# 5. 'kurs' ifadesinin bas ve sondaki bosluklari silin
bosluklu = "    " + kurs + "    "
print("5-", f"[{bosluklu.strip()}]")

# 6. 'kurs' ifadesinin kelimelerini listeye cevirin
print("6-", kurs.split())

# 7. 'kurs' ifadesindeki bosluklari '-' ile degistirin (URL dostu yazim)
print("7-", kurs.lower().replace(" ", "-"))

# 8. maketrans / translate ile karakter donusumu: a -> 4, e -> 3, i -> 1 ve bosluklari silme
tablo = str.maketrans("aei", "431", " ")
print("8-", kurs.translate(tablo))

# 9. Kullanicidan alinan cumlenin analizi
cumle = input("Bir cumle yazin: ").strip()
print("9- Karakter sayisi:", len(cumle))
print("   Kelime sayisi:", len(cumle.split()))
print("   Buyuk harfle:", cumle.upper())
print("   Bas harfleri buyuk:", cumle.title())
print("   Ters hali:", cumle[::-1])

# 10. E-posta dogrulama
email = input("E-posta: ").strip().lower()
if email.count("@") == 1 and "." in email.split("@")[1]:
    kullanici, alan = email.split("@")
    print(f"10- Gecerli. Kullanici: {kullanici}, alan adi: {alan}")
else:
    print("10- Gecersiz e-posta.")
