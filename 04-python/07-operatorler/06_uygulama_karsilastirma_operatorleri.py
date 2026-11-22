# 7.6 Uygulama: Karsilastirma Operatorleri

# 1. Girilen iki sayidan hangisi buyuktur?
a = int(input("a: "))
b = int(input("b: "))
print("1- a > b:", a > b, "| b > a:", b > a, "| esit:", a == b)

# 2. Kullanicidan alinan 2 vize (%60) ve final (%40) notuna gore
#    ortalamanin 50 ve uzerinde olup olmadigini kontrol edin
vize1 = float(input("1. vize: "))
vize2 = float(input("2. vize: "))
final = float(input("Final: "))
ortalama = ((vize1 + vize2) / 2) * 0.6 + final * 0.4
print(f"2- Ortalama: {ortalama:.2f}, gecti mi: {ortalama >= 50}")

# 3. Girilen sayinin tek mi cift mi oldugunu kontrol edin
sayi = int(input("Bir sayi: "))
print("3- Cift mi:", sayi % 2 == 0)

# 4. Girilen sayinin negatif olup olmadigini kontrol edin
print("4- Negatif mi:", sayi < 0)

# 5. Parola ve e-posta bilgisini sisteme kayitli bilgilerle karsilastirin
kayitli_email = "sude@ornek.com"
kayitli_parola = "abc123"
email = input("E-posta: ")
parola = input("Parola: ")
print("5- E-posta dogru mu:", email == kayitli_email)
print("   Parola dogru mu:", parola == kayitli_parola)

# 6. Kullanici adinin uzunlugu 5-15 karakter arasinda mi?
kullanici_adi = input("Kullanici adi: ")
print("6- Uzunluk uygun mu:", 5 <= len(kullanici_adi) <= 15)

# 7. Girilen yas 18 ve uzeri mi?
yas = int(input("Yas: "))
print("7- Resit mi:", yas >= 18)

# 8. Bir sayinin digerinin kati olup olmadigi
x, y = 36, 6
print(f"8- {x}, {y}'nin kati mi:", x % y == 0)

# 9. Iki kelimenin alfabetik sirasi
k1, k2 = "Python", "Java"
print(f"9- '{k1}' alfabetik olarak '{k2}'den once mi:", k1 < k2)
