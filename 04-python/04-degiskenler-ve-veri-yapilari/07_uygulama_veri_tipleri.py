# 4.7 Uygulama: Veri Tipleri
# Kullanicidan alinan degerlerle hesaplama yapma.
# input() her zaman str dondurdugu icin donusum yapilmalidir.

print("--- Urun Fiyat Hesaplama ---")
urun_adi = input("Urun adi: ")
birim_fiyat = float(input("Birim fiyat (TL): "))
adet = int(input("Adet: "))
indirim_var = input("Indirim kuponunuz var mi? (e/h): ") == "e"

ara_toplam = birim_fiyat * adet
indirim = ara_toplam * 0.10 if indirim_var else 0
kdv = (ara_toplam - indirim) * 0.20
genel_toplam = ara_toplam - indirim + kdv

print("\n--- Fatura ---")
print("Urun        :", urun_adi, type(urun_adi))
print("Birim fiyat :", birim_fiyat, type(birim_fiyat))
print("Adet        :", adet, type(adet))
print("Indirim     :", indirim_var, type(indirim_var))
print("Ara toplam  :", round(ara_toplam, 2))
print("Indirim     :", round(indirim, 2))
print("KDV         :", round(kdv, 2))
print("Genel toplam:", round(genel_toplam, 2))

print("\n--- Sicaklik Donusturucu ---")
celsius = float(input("Sicaklik (C): "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(str(celsius) + " C = " + str(fahrenheit) + " F")
print(str(celsius) + " C = " + str(kelvin) + " K")

print("\n--- Saniye Donusturucu ---")
toplam_saniye = int(input("Saniye: "))
saat = toplam_saniye // 3600
dakika = (toplam_saniye % 3600) // 60
saniye = toplam_saniye % 60
print(toplam_saniye, "saniye =", saat, "saat", dakika, "dakika", saniye, "saniye")
