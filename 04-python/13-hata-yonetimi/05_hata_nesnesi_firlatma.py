# 13.5 Hata Nesnesi Firlatma (raise)
# Bir kosul saglanmadiginda bilerek hata olusturmak icin raise kullanilir.

# 1. Temel kullanim
x = 10
try:
    if x > 5:
        raise Exception("x 5'ten buyuk bir deger olamaz.")
except Exception as hata:
    print("Hata:", hata)


# 2. Fonksiyonlarda parametre kontrolu
def yas_kontrol(yas):
    if not isinstance(yas, int):
        raise TypeError("Yas tam sayi olmalidir.")
    if yas < 0:
        raise ValueError("Yas negatif olamaz.")
    return f"Yas: {yas}"


for deger in [25, -3, "yirmi"]:
    try:
        print(yas_kontrol(deger))
    except (TypeError, ValueError) as hata:
        print(f"{type(hata).__name__}: {hata}")


# 3. Parola kontrolu
def parola_kontrol(parola):
    import re
    if len(parola) < 8:
        raise ValueError("Parola en az 8 karakter olmalidir.")
    if not re.search("[a-z]", parola):
        raise ValueError("Parola kucuk harf icermelidir.")
    if not re.search("[A-Z]", parola):
        raise ValueError("Parola buyuk harf icermelidir.")
    if not re.search("[0-9]", parola):
        raise ValueError("Parola rakam icermelidir.")
    print("Gecerli parola.")


for p in ["abc", "abcdefgh", "Abcdefgh", "Abcdefg1"]:
    try:
        parola_kontrol(p)
    except ValueError as hata:
        print(f"{p}: {hata}")


# 4. Kendi hata sinifimizi olusturma (Exception sinifindan turetilir)
class YetersizBakiyeHatasi(Exception):
    def __init__(self, bakiye, miktar):
        self.bakiye = bakiye
        self.miktar = miktar
        super().__init__(f"Bakiye yetersiz. Bakiye: {bakiye}, istenen: {miktar}")


def para_cek(bakiye, miktar):
    if miktar > bakiye:
        raise YetersizBakiyeHatasi(bakiye, miktar)
    return bakiye - miktar


try:
    para_cek(500, 800)
except YetersizBakiyeHatasi as hata:
    print(hata)
    print("Eksik tutar:", hata.miktar - hata.bakiye)

# 5. Yakalanan hatayi tekrar firlatma
try:
    try:
        int("abc")
    except ValueError:
        print("Hata loglandi, tekrar firlatiliyor...")
        raise
except ValueError as hata:
    print("Dis blokta yakalandi:", hata)
