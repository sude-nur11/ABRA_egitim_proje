# 4.5 Veri Tipleri
# type() fonksiyonu bir degerin veri tipini gosterir.

# Sayisal tipler
tam_sayi = 42
ondalikli = 3.14
karmasik = 2 + 3j
print(tam_sayi, type(tam_sayi))       # int
print(ondalikli, type(ondalikli))     # float
print(karmasik, type(karmasik))       # complex
print("Karmasik sayinin reel ve sanal kismi:", karmasik.real, karmasik.imag)

# Metin tipi
metin = "Python"
print(metin, type(metin))             # str

# Mantiksal tip
dogru = True
yanlis = False
print(dogru, type(dogru))             # bool
print("10 > 5:", 10 > 5)              # karsilastirmalar bool dondurur

# Bos deger
bos = None
print(bos, type(bos))                 # NoneType

# Koleksiyon tipleri (ileriki bolumlerde detayli islenecek)
liste = [1, 2, 3]
demet = (1, 2, 3)
kume = {1, 2, 3}
sozluk = {"ad": "Sude", "yas": 22}
print(liste, type(liste))             # list
print(demet, type(demet))             # tuple
print(kume, type(kume))               # set
print(sozluk, type(sozluk))           # dict

# isinstance ile tip kontrolu
print("42 int mi?", isinstance(42, int))
print("'42' int mi?", isinstance("42", int))
print("3.14 sayi mi?", isinstance(3.14, (int, float)))

# Buyuk sayilar: Python'da int'in siniri yoktur
buyuk = 2 ** 100
print("2^100 =", buyuk)

# Okunabilirlik icin sayilarda _ kullanilabilir
nufus = 85_000_000
print("Nufus:", nufus)

# Bilimsel gosterim float uretir
kucuk = 1.5e-3
print(kucuk, type(kucuk))
