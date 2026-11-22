# 6.9 Dictionary Metotlari

urun = {"ad": "Laptop", "marka": "ABC", "fiyat": 25000, "stok": 10}

# keys, values, items
print(urun.keys())
print(urun.values())
print(urun.items())
print(list(urun.keys()))

# Dongu ile sozlukte gezinme
for anahtar in urun:
    print(anahtar, "->", urun[anahtar])
for anahtar, deger in urun.items():
    print(f"{anahtar}: {deger}")

# get: anahtarin degerini getirir, yoksa varsayilan degeri doner
print(urun.get("renk", "belirtilmemis"))

# update: birden fazla anahtari ekler / gunceller
urun.update({"fiyat": 23000, "renk": "gri"})
print(urun)

# setdefault: anahtar yoksa ekler, varsa mevcut degeri dondurur
urun.setdefault("garanti", 2)
urun.setdefault("fiyat", 0)
print(urun)

# pop: anahtari siler ve degerini dondurur
stok = urun.pop("stok")
print("Silinen stok:", stok, urun)

# popitem: son eklenen elemani siler
print("popitem:", urun.popitem(), urun)

# copy
kopya = urun.copy()
kopya["ad"] = "Tablet"
print("orijinal:", urun["ad"], "kopya:", kopya["ad"])

# fromkeys: verilen anahtarlarla yeni sozluk
notlar = dict.fromkeys(["Sude", "Ali", "Ayse"], 0)
print(notlar)

# clear
kopya.clear()
print("clear:", kopya)

# Kelime sayma ornegi
metin = "elma armut elma kiraz armut elma"
sayac = {}
for kelime in metin.split():
    sayac[kelime] = sayac.get(kelime, 0) + 1
print(sayac)
print("En cok gecen:", max(sayac, key=sayac.get))
