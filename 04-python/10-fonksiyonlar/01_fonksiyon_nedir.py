# 10.1 Fonksiyon Nedir?
# Fonksiyon; belirli bir isi yapan, bir isim altinda toplanmis ve
# istenildigi kadar tekrar cagrilabilen kod blogudur.
# Avantajlari: kod tekrarini onler, kodu parcalara ayirir, okunabilirligi artirir.

# Daha once kullandigimiz hazir (built-in) fonksiyonlar:
print("print bir fonksiyondur")
print(len("Python"))
print(type(10))
print(max([3, 8, 1]))
print(sum([1, 2, 3]))
print(round(3.567, 1))
print(int("42") + 1)

# Fonksiyon olmadan ayni isi tekrar tekrar yazmak:
liste1 = [70, 85, 90]
toplam = 0
for n in liste1:
    toplam += n
print("Ortalama 1:", toplam / len(liste1))

liste2 = [50, 60, 45, 80]
toplam = 0
for n in liste2:
    toplam += n
print("Ortalama 2:", toplam / len(liste2))


# Fonksiyon ile ayni isi bir kez yazip istedigimiz kadar kullanmak:
def ortalama_hesapla(liste):
    toplam = 0
    for n in liste:
        toplam += n
    return toplam / len(liste)


print("Ortalama 1:", ortalama_hesapla(liste1))
print("Ortalama 2:", ortalama_hesapla(liste2))
print("Ortalama 3:", ortalama_hesapla([100, 95]))

# Fonksiyonlar da birer nesnedir
print(type(ortalama_hesapla))
print(ortalama_hesapla)

# Fonksiyonun yapisi:
# def fonksiyon_adi(parametre1, parametre2):    -> tanimlama
#     """aciklama (docstring)"""
#     yapilacak islemler                        -> govde
#     return sonuc                              -> deger dondurme
#
# fonksiyon_adi(arguman1, arguman2)             -> cagirma

# help() ile hazir fonksiyonlarin aciklamasi okunabilir
print(len.__doc__)
