# 4.1 Degisken Nedir?
# Degisken, bir degeri bellekte saklamak ve daha sonra kullanmak icin
# o degere verdigimiz isimdir. Bir kutuya etiket yapistirmak gibi dusunulebilir.

# Degisken kullanmadan:
print(1250 * 0.18)
print(1250 + 1250 * 0.18)

# Degisken kullanarak ayni hesap daha okunakli olur:
fiyat = 1250
kdv_orani = 0.18
kdv = fiyat * kdv_orani
toplam = fiyat + kdv

print("Fiyat:", fiyat)
print("KDV:", kdv)
print("Toplam:", toplam)

# Degiskenin degeri program icinde degistirilebilir (adi da buradan gelir)
fiyat = 2000
kdv = fiyat * kdv_orani
toplam = fiyat + kdv
print("Yeni toplam:", toplam)

# Degiskenler bellekte bir adres tutar, id() ile bu adres gorulebilir
sayi = 10
print("sayi degiskeninin degeri:", sayi)
print("sayi degiskeninin bellekteki adresi:", id(sayi))

# Bir degiskenin degeri baska bir degiskene aktarilabilir
a = 5
b = a
print("a:", a, "b:", b)

# Degiskenler birbirleriyle isleme sokulabilir
ad = "Sude"
soyad = "Toprak"
tam_ad = ad + " " + soyad
print("Tam ad:", tam_ad)

# Degiskenin degerini kendi eski degeri uzerinden guncelleme
sayac = 0
sayac = sayac + 1
sayac = sayac + 1
print("Sayac:", sayac)
