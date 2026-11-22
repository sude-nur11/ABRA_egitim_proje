# 4.6 Veri Tipi Donusumu (Type Casting)

# str -> int / float
sayi_metin = "25"
print(sayi_metin + "5")            # metin birlestirme: 255
print(int(sayi_metin) + 5)         # sayisal toplama: 30
print(float("3.75") * 2)

# int -> float ve float -> int
print(float(10))                   # 10.0
print(int(9.99))                   # 9 (yuvarlamaz, ondalik kismi atar)
print(round(9.99))                 # 10 (yuvarlama icin round)

# Sayi -> str
yas = 22
mesaj = "Yasim " + str(yas)
print(mesaj)

# bool donusumleri
print(bool(1), bool(0))            # True False
print(bool("merhaba"), bool(""))   # True False
print(bool([1, 2]), bool([]))      # True False
print(bool(None))                  # False
print(int(True), int(False))       # 1 0

# Koleksiyonlar arasi donusum
metin = "python"
print(list(metin))                 # ['p', 'y', 't', 'h', 'o', 'n']
print(tuple([1, 2, 3]))
print(set([1, 1, 2, 2, 3]))        # tekrarlar silinir
print(list({"a": 1, "b": 2}))      # sozlugun anahtarlari

# Sayi sistemleri arasi donusum
print(bin(10), oct(10), hex(10))
print(int("1010", 2))              # ikilik tabandan onluk tabana
print(int("ff", 16))

# Karakter <-> sayi (ASCII / Unicode)
print(ord("A"), chr(66))

# Hatali donusum ornekleri
try:
    int("abc")
except ValueError as hata:
    print("Hata:", hata)

try:
    int("3.5")                     # ondalikli metin dogrudan int'e cevrilemez
except ValueError as hata:
    print("Hata:", hata)
print(int(float("3.5")))           # once float sonra int
