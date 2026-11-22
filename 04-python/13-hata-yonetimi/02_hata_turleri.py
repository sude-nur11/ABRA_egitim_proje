# 13.2 Hata Turleri
# Her ornekte hata try-except ile yakalanip turu ve mesaji ekrana yazdirilmistir.


def hata_goster(aciklama, fonksiyon):
    try:
        fonksiyon()
    except Exception as hata:
        print(f"{aciklama:<45} -> {type(hata).__name__}: {hata}")


# NameError: tanimlanmamis bir degisken kullanilirsa
hata_goster("Tanimsiz degisken", lambda: print(tanimsiz_degisken))

# TypeError: uyumsuz tipler arasinda islem yapilirsa
hata_goster("String ile sayi toplama", lambda: "10" + 5)
hata_goster("Fonksiyona eksik parametre", lambda: len())

# ValueError: dogru tipte ama gecersiz degerde arguman
hata_goster("Metni sayiya cevirme", lambda: int("on"))
hata_goster("Listede olmayan elemanin indeksi", lambda: [1, 2].index(5))

# ZeroDivisionError: sifira bolme
hata_goster("Sifira bolme", lambda: 10 / 0)

# IndexError: olmayan bir indekse erisim
hata_goster("Olmayan indeks", lambda: [1, 2, 3][10])

# KeyError: sozlukte olmayan bir anahtar
hata_goster("Olmayan sozluk anahtari", lambda: {"ad": "Sude"}["yas"])

# AttributeError: nesnede olmayan bir nitelik / metot
hata_goster("Olmayan metot", lambda: "metin".append("a"))

# FileNotFoundError: olmayan dosyayi acma
hata_goster("Olmayan dosya", lambda: open("yok.txt"))

# ModuleNotFoundError: olmayan modulu import etme
hata_goster("Olmayan modul", lambda: __import__("olmayan_modul"))

# OverflowError: sayinin sinirlarini asma (float icin)
hata_goster("Cok buyuk float", lambda: 10.0 ** 1000)

# RecursionError: cok derin ozyineleme
def sonsuz():
    return sonsuz()


hata_goster("Sonsuz ozyineleme", sonsuz)

# StopIteration: elemani bitmis iteratorden eleman isteme
it = iter([1])
next(it)
hata_goster("Bitmis iterator", lambda: next(it))

# SyntaxError calismadan once yakalanir; ancak exec/eval ile gosterilebilir
hata_goster("Yazim hatasi", lambda: eval("print('a'"))

# IndentationError da bir SyntaxError turudur
hata_goster("Girinti hatasi", lambda: exec("if True:\nprint('a')"))
