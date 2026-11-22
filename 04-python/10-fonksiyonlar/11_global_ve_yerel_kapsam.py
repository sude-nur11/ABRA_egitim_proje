# 10.11 Global ve Yerel (Local) Kapsam (Scope)
# Global degisken: fonksiyon disinda tanimlanir, her yerden okunabilir.
# Yerel degisken : fonksiyon icinde tanimlanir, sadece o fonksiyonda gecerlidir.

x = "global x"


def fonksiyon1():
    y = "yerel y"
    print("Fonksiyon icinde:", x)    # global degisken okunabilir
    print("Fonksiyon icinde:", y)


fonksiyon1()
print("Fonksiyon disinda:", x)
# print(y)   -> NameError: y sadece fonksiyon icinde gecerli


# Ayni isimde yerel degisken tanimlanirsa global olani golgeler
isim = "Ali"


def degistir():
    isim = "Sude"          # yeni bir YEREL degisken
    print("Icerde:", isim)


degistir()
print("Disarida:", isim)    # global degismedi


# global anahtar kelimesi ile global degiskeni degistirme
sayac = 0


def artir():
    global sayac
    sayac += 1


for _ in range(5):
    artir()
print("Sayac:", sayac)


# global kullanmadan once deger atanirsa hata olusur
toplam = 10


def hatali():
    try:
        toplam += 1        # yerel kabul edilir ama degeri yok
    except UnboundLocalError as hata:
        print("Hata:", hata)


hatali()


# Ic ice fonksiyonlar ve nonlocal
def dis_fonksiyon():
    mesaj = "dis"

    def ic_fonksiyon():
        nonlocal mesaj
        mesaj = "ic fonksiyon tarafindan degistirildi"

    ic_fonksiyon()
    print(mesaj)


dis_fonksiyon()

# LEGB kurali: Python bir ismi su sirayla arar
# Local -> Enclosing (dis fonksiyon) -> Global -> Built-in
len_degeri = len("abc")     # len built-in kapsamda bulunur
print(len_degeri)


# Iyi uygulama: global yerine parametre ve return kullanmak
def artir_dogru(deger):
    return deger + 1


sayac = artir_dogru(sayac)
print("Sayac:", sayac)
