# 6.6 Tuple (Demet)
# Tuple, listeye benzer ancak DEGISTIRILEMEZ (immutable). () ile tanimlanir.
# Degismemesi gereken veriler icin kullanilir (orn. koordinatlar, gunler).

gunler = ("Pazartesi", "Sali", "Carsamba", "Persembe", "Cuma", "Cumartesi", "Pazar")
koordinat = (39.92, 32.85)
tek_elemanli = ("tek",)          # tek elemanli tuple icin sondaki virgul sart
tek_degil = ("tek")              # bu bir string'dir
parantezsiz = 1, 2, 3            # parantez olmadan da tuple olusur

print(type(tek_elemanli), type(tek_degil), type(parantezsiz))
print(gunler)

# Erisim ve dilimleme listelerle aynidir
print(gunler[0])
print(gunler[-1])
print(gunler[:5])                # hafta ici
print(gunler[5:])                # hafta sonu
print(len(gunler))

# Metotlar (sadece iki metodu vardir)
sayilar = (1, 2, 3, 2, 2, 4)
print("count(2):", sayilar.count(2))
print("index(3):", sayilar.index(3))

# Degistirme denemesi
try:
    gunler[0] = "Monday"
except TypeError as hata:
    print("Hata:", hata)

# Tuple acma (unpacking)
enlem, boylam = koordinat
print("Enlem:", enlem, "Boylam:", boylam)
ilk, *orta, son = (1, 2, 3, 4, 5)
print(ilk, orta, son)

# Degistirmek gerekirse listeye cevrilip tekrar tuple yapilir
liste = list(sayilar)
liste.append(5)
sayilar = tuple(liste)
print(sayilar)

# Tuple birlestirme
print((1, 2) + (3, 4))

# Tuple icinde liste: listenin kendisi degistirilebilir
karisik = ("Sude", [70, 80])
karisik[1].append(90)
print(karisik)
