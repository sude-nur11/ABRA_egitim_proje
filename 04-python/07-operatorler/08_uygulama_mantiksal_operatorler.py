# 7.8 Uygulama: Mantiksal Operatorler

# 1. Girilen sayinin 0-100 arasinda olup olmadigini kontrol edin
sayi = int(input("Sayi: "))
print("1- 0-100 arasinda mi:", sayi > 0 and sayi < 100)

# 2. Girilen sayinin pozitif cift sayi olup olmadigini kontrol edin
print("2- Pozitif cift mi:", sayi > 0 and sayi % 2 == 0)

# 3. Kullanici adi ve parola dogru mu?
kayitli_email = "sude@ornek.com"
kayitli_parola = "abc123"
email = input("E-posta: ")
parola = input("Parola: ")
print("3- Giris basarili mi:", email == kayitli_email and parola == kayitli_parola)

# 4. Girilen 3 sayiyi buyukluk olarak karsilastirin
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("4- a en buyuk mu:", a > b and a > c)
print("   b en buyuk mu:", b > a and b > c)
print("   c en buyuk mu:", c > a and c > b)

# 5. Kullanicidan 2 vize (%60) ve final (%40) notu alip ortalama hesaplayin.
#    Ortalama en az 50 ve final notu en az 50 olmali.
vize1 = float(input("1. vize: "))
vize2 = float(input("2. vize: "))
final = float(input("Final: "))
ortalama = ((vize1 + vize2) / 2) * 0.6 + final * 0.4
gecti = ortalama >= 50 and final >= 50
print(f"5- Ortalama: {ortalama:.2f}, gecme durumu: {gecti}")

# 6. Kisinin adi, kilosu ve boyu ile VKI hesaplayip araligini bulun
#    0-18.4 zayif, 18.5-24.9 normal, 25-29.9 kilolu, 30+ obez
ad = input("Ad: ")
kilo = float(input("Kilo: "))
boy = float(input("Boy (m): "))
vki = kilo / (boy ** 2)
print(f"6- {ad}, VKI: {vki:.1f}")
print("   Zayif:", vki >= 0 and vki <= 18.4)
print("   Normal:", vki > 18.4 and vki <= 24.9)
print("   Kilolu:", vki > 24.9 and vki <= 29.9)
print("   Obez:", vki >= 29.9)

# 7. Yilin artik yil olup olmadigi: 4'e bolunup 100'e bolunmeyen ya da 400'e bolunen
yil = int(input("Yil: "))
print("7- Artik yil mi:", (yil % 4 == 0 and yil % 100 != 0) or yil % 400 == 0)
