# 10.5 Uygulama: Fonksiyonlar

# 1. Gonderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyon
def yazdir(kelime, adet):
    print(kelime * adet)


yazdir("Merhaba ", 3)


# 2. Kendine gonderilen sinirsiz sayidaki parametreyi listeye ceviren fonksiyon
def listeye_cevir(*params):
    return list(params)


print(listeye_cevir(10, 20, 30, "merhaba"))


# 3. Gonderilen 2 sayi arasindaki tum asal sayilari bulan fonksiyon
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True


def asal_sayilari_bul(sayi1, sayi2):
    return [s for s in range(sayi1, sayi2 + 1) if asal_mi(s)]


print(asal_sayilari_bul(10, 50))


# 4. Kendisine gonderilen bir sayinin tam bolenlerini bulan fonksiyon
def tam_bolenleri_bul(sayi):
    bolenler = []
    for i in range(2, sayi):
        if sayi % i == 0:
            bolenler.append(i)
    return bolenler


print(tam_bolenleri_bul(90))


# 5. Kelimedeki harfleri ters ceviren ve palindrom kontrolu yapan fonksiyonlar
def ters_cevir(metin):
    return metin[::-1]


def palindrom_mu(metin):
    temiz = metin.replace(" ", "").lower()
    return temiz == ters_cevir(temiz)


print(ters_cevir("Python"))
print(palindrom_mu("Ey Edip Adanada pide ye"))


# 6. Ogrenci notuna gore harf notu donduren fonksiyon
def harf_notu(puan):
    if puan >= 90:
        return "AA"
    elif puan >= 80:
        return "BA"
    elif puan >= 70:
        return "BB"
    elif puan >= 60:
        return "CB"
    elif puan >= 50:
        return "CC"
    return "FF"


notlar = {"Sude": 92, "Ali": 67, "Ayse": 45}
for isim, puan in notlar.items():
    print(f"{isim}: {puan} -> {harf_notu(puan)}")
