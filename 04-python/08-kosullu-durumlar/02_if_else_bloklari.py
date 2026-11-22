# 8.2 if / else Bloklari

# Ornek 1: Yasa gore ehliyet kontrolu
yas = int(input("Yasiniz: "))

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsiniz.")
    print(18 - yas, "yil sonra alabilirsiniz.")

# Ornek 2: Tek / cift kontrolu
sayi = int(input("Bir sayi: "))
if sayi % 2 == 0:
    print(sayi, "cift sayidir.")
else:
    print(sayi, "tek sayidir.")

# Ornek 3: Kullanici girisi
kayitli_kullanici = "sude"
kayitli_parola = "1234"

kullanici = input("Kullanici adi: ")
parola = input("Parola: ")

if kullanici == kayitli_kullanici and parola == kayitli_parola:
    print("Giris basarili, hos geldiniz", kullanici)
else:
    print("Kullanici adi veya parola hatali.")

# Ornek 4: Ic ice if / else
if kullanici == kayitli_kullanici:
    if parola == kayitli_parola:
        print("(ic ice) Giris basarili.")
    else:
        print("(ic ice) Parola hatali.")
else:
    print("(ic ice) Boyle bir kullanici yok.")

# Ornek 5: Tek satirda if / else (ternary operator)
durum = "pozitif" if sayi >= 0 else "negatif"
print("Sayi", durum)

# Ornek 6: Listede eleman kontrolu
yasakli_kelimeler = ["kotu", "cirkin"]
yorum = input("Yorumunuz: ").lower()
if any(kelime in yorum for kelime in yasakli_kelimeler):
    print("Yorumunuz uygunsuz ifade iceriyor.")
else:
    print("Yorumunuz yayinlandi.")
