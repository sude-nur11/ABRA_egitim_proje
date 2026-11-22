# 10.2 Fonksiyon Tanimlama
# def anahtar kelimesi ile tanimlanir. Fonksiyon cagrilmadan calismaz.

def merhaba():
    print("Merhaba Dunya")


merhaba()
merhaba()


def cizgi():
    print("-" * 30)


def menu_goster():
    """Ekrana uygulama menusunu yazdirir."""
    cizgi()
    print("1- Kayit ol")
    print("2- Giris yap")
    print("3- Cikis")
    cizgi()


menu_goster()

# Docstring okuma
print(menu_goster.__doc__)


# Fonksiyon icinden baska fonksiyon cagirma
def baslik_yazdir():
    cizgi()
    print("     OGRENCI SISTEMI")
    cizgi()


baslik_yazdir()


# Fonksiyon tanimlanmadan once cagrilamaz
# selamla()   -> NameError

def selamla():
    print("Selamlar!")


selamla()


# Bos fonksiyon tanimlama (ileride doldurulacaksa)
def yapilacak():
    pass


yapilacak()

# Fonksiyonu bir degiskene atama
yazdir = merhaba
yazdir()


# Fonksiyon icinde dongu kullanma
def sayilari_yazdir():
    for i in range(1, 6):
        print(i, end=" ")
    print()


sayilari_yazdir()
