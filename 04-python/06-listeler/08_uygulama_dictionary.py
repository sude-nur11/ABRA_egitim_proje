# 6.8 Uygulama: Dictionary
# Kullanicidan ogrenci bilgilerini alip sozlukte saklama

ogrenciler = {}

# 1. ogrenci
numara = input("Ogrenci no: ")
ad = input("Ogrenci adi: ")
soyad = input("Ogrenci soyad: ")
telefon = input("Ogrenci telefon: ")

ogrenciler[numara] = {
    "ad": ad,
    "soyad": soyad,
    "telefon": telefon,
}

# 2. ogrenci
numara = input("Ogrenci no: ")
ad = input("Ogrenci adi: ")
soyad = input("Ogrenci soyad: ")
telefon = input("Ogrenci telefon: ")

ogrenciler.update({
    numara: {
        "ad": ad,
        "soyad": soyad,
        "telefon": telefon,
    }
})

print("*" * 40)
print("Kayitli ogrenciler:", ogrenciler)

# Ogrenci numarasina gore bilgi getirme
aranan = input("Bilgilerini gormek istediginiz ogrenci no: ")
ogrenci = ogrenciler.get(aranan)

if ogrenci:
    print(f"Adi      : {ogrenci['ad']}")
    print(f"Soyadi   : {ogrenci['soyad']}")
    print(f"Telefon  : {ogrenci['telefon']}")
else:
    print("Bu numarada ogrenci bulunamadi.")

# Sozlukteki tum ogrencileri listeleme
print("*" * 40)
for no, bilgi in ogrenciler.items():
    print(no, "-", bilgi["ad"], bilgi["soyad"])
