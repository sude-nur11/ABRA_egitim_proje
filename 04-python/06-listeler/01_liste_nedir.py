# 6.1 Liste Nedir?
# Liste; birden fazla degeri tek bir degiskende, sirali sekilde tutan
# ve sonradan DEGISTIRILEBILEN (mutable) bir veri yapisidir. [] ile gosterilir.

# Liste olmadan 5 ogrencinin notunu tutmak:
not1 = 70
not2 = 85
not3 = 90
not4 = 45
not5 = 60
ortalama = (not1 + not2 + not3 + not4 + not5) / 5
print("Ortalama (degiskenlerle):", ortalama)

# Liste ile ayni islem:
notlar = [70, 85, 90, 45, 60]
print("Notlar:", notlar)
print("Ortalama (liste ile):", sum(notlar) / len(notlar))

# Listenin ozellikleri
# 1. Siralidir: her elemanin bir indeksi vardir
print("Ilk not:", notlar[0])
print("Son not:", notlar[-1])

# 2. Degistirilebilir
notlar[3] = 50
print("Guncel notlar:", notlar)

# 3. Farkli tipte veriler icerebilir
karisik = ["Sude", 22, 1.65, True, None]
print("Karisik liste:", karisik)

# 4. Ayni elemani birden fazla kez icerebilir
tekrarli = [1, 1, 2, 2, 3]
print("Tekrarli liste:", tekrarli)

# 5. Liste icinde liste olabilir
ogrenci = ["Sude", [70, 85, 90]]
print("Ogrenci:", ogrenci[0], "Notlari:", ogrenci[1])

# String ile liste arasindaki fark
metin = "python"
liste = ["p", "y", "t", "h", "o", "n"]
print(metin[0], liste[0])
liste[0] = "P"           # liste degistirilebilir
# metin[0] = "P"         # string degistirilemez -> TypeError
print(liste)
print(type(notlar), len(notlar))
