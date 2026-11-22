# 13.1 Hata ve Hata Yonetimi Nedir?
# Program calisirken beklenmeyen bir durum olustugunda Python bir hata (exception)
# firlatir ve program durur. Hata yonetimi, bu hatalari yakalayip programin
# cokmeden calismaya devam etmesini saglamaktir.
#
# Uc tur hata vardir:
# 1. Syntax (yazim) hatalari  : kod calismadan once tespit edilir. Ornek: print("a"
# 2. Runtime (calisma) hatalari: kod calisirken olusur. Ornek: 10 / 0
# 3. Mantik hatalari           : program calisir ama yanlis sonuc uretir.

# Ornek: Hata yonetimi olmadan
# sayi = int(input("Sayi: "))   -> kullanici "abc" girerse program coker

# Ornek: Hata yonetimi ile
try:
    sayi = int("abc")
    print("Bu satir calismaz.")
except ValueError:
    print("Gecersiz sayi girildi, program cokmedi.")

print("Program devam ediyor...")

# Hatanin detaylarini gorme
try:
    sonuc = 10 / 0
except ZeroDivisionError as hata:
    print("Hata mesaji:", hata)
    print("Hata turu:", type(hata).__name__)


# Mantik hatasi ornegi: program calisir ama sonuc yanlistir
def ortalama_hatali(a, b):
    return a + b / 2           # parantez unutulmus


def ortalama_dogru(a, b):
    return (a + b) / 2


print("Hatali ortalama:", ortalama_hatali(10, 20))
print("Dogru ortalama:", ortalama_dogru(10, 20))

# Hatalar birer sinif (class) olarak tanimlidir ve bir hiyerarsiye sahiptir
print(ValueError.__mro__)
print(issubclass(ZeroDivisionError, ArithmeticError))
print(issubclass(ArithmeticError, Exception))

# Hata yonetimi kullanmadan once kontrol etmek de bir yontemdir
bolen = 0
if bolen != 0:
    print(10 / bolen)
else:
    print("Bolen sifir olamaz (if ile kontrol edildi).")

# Hata yonetimi anahtar kelimeleri:
# try     -> hata olusabilecek kod
# except  -> hata olusursa calisacak kod
# else    -> hata olusmazsa calisacak kod
# finally -> her durumda calisacak kod
# raise   -> bilerek hata firlatma
