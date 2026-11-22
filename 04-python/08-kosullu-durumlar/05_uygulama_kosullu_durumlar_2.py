# 8.5 Uygulama: Kosullu Durumlar - 2

# 1. Girilen bir sayinin 0-100 arasinda olup olmadigini kontrol edin
sayi = int(input("Sayi: "))
if 0 < sayi < 100:
    print("1- Sayi 0-100 arasindadir.")
else:
    print("1- Sayi 0-100 arasinda degildir.")

# 2. Girilen bir sayinin pozitif cift sayi olup olmadigini kontrol edin
if sayi > 0:
    if sayi % 2 == 0:
        print("2- Pozitif cift sayi")
    else:
        print("2- Pozitif tek sayi")
else:
    print("2- Pozitif degil")

# 3. Email ve parola bilgileri ile giris kontrolu yapin
email = "sude@ornek.com"
parola = "abc123"
girilen_email = input("Email: ")
girilen_parola = input("Parola: ")

if girilen_email == email and girilen_parola == parola:
    print("3- Uygulamaya giris yapildi.")
elif girilen_email != email:
    print("3- Email bilgisi hatali.")
else:
    print("3- Parola bilgisi hatali.")

# 4. Girilen 3 sayiyi buyukluk olarak karsilastirin
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a >= b and a >= c:
    print(f"4- En buyuk sayi a: {a}")
elif b >= a and b >= c:
    print(f"4- En buyuk sayi b: {b}")
else:
    print(f"4- En buyuk sayi c: {c}")

# 5. Kisinin adi, kilo ve boy bilgilerini alip kilo indeksini hesaplayin
#    Formul: kilo / boy**2
#    0-18.4 zayif, 18.5-24.9 normal, 25-29.9 fazla kilolu,
#    30-34.9 sisman (obez), 35+ asiri sisman
ad = input("Adiniz: ")
kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz (m): "))
indeks = kilo / boy ** 2

if indeks < 18.5:
    sonuc = "zayif"
elif indeks < 25:
    sonuc = "normal"
elif indeks < 30:
    sonuc = "fazla kilolu"
elif indeks < 35:
    sonuc = "sisman (obez)"
else:
    sonuc = "asiri sisman"
print(f"5- {ad}, kilo indeksiniz {indeks:.2f} ve kilo degerlendirmeniz: {sonuc}")
