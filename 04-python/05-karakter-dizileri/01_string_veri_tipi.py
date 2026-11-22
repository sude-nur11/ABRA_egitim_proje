# 5.1 String Veri Tipi
# String (str): karakterlerden olusan metin tipidir. Tirnak icinde yazilir.

tek_tirnak = 'Merhaba'
cift_tirnak = "Merhaba"
uc_tirnak = """Bu metin
birden fazla
satirdan olusur."""

print(tek_tirnak)
print(cift_tirnak)
print(uc_tirnak)
print(type(tek_tirnak))

# Tirnak icinde tirnak kullanma
print("Onun adi 'Sude' idi.")
print('Onun adi "Sude" idi.')
print("Onun adi \"Sude\" idi.")   # kacis karakteri ile

# Kacis karakterleri
print("Satir 1\nSatir 2")         # \n yeni satir
print("Ad:\tSude")                # \t tab
print("C:\\Kullanicilar\\sude")   # \\ ters egik cizgi
print(r"C:\new\test")             # raw string: kacis karakterleri islenmez

# String birlestirme (+) ve tekrarlama (*)
ad = "Sude"
soyad = "Toprak"
tam_ad = ad + " " + soyad
print(tam_ad)
print("=" * 30)
print("ha" * 3)

# Uzunluk
print("Karakter sayisi:", len(tam_ad))

# String icinde arama (in)
print("Sude" in tam_ad)
print("Ali" not in tam_ad)

# Bos string
bos = ""
print("Bos string uzunlugu:", len(bos))

# String'ler degistirilemez (immutable)
metin = "python"
# metin[0] = "P"   -> TypeError
metin = "P" + metin[1:]           # yeni bir string olusturulur
print(metin)

# String karsilastirma
print("elma" == "elma", "a" < "b", "Z" < "a")
