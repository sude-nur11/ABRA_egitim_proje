# 7.7 Mantiksal Operatorler: and, or, not

# and: tum kosullar True ise True doner
# or : kosullardan en az biri True ise True doner
# not: sonucu tersine cevirir

x = 6

print("x > 5 and x < 10:", x > 5 and x < 10)
print("x > 5 and x < 3 :", x > 5 and x < 3)
print("x > 5 or x < 3  :", x > 5 or x < 3)
print("x > 8 or x < 3  :", x > 8 or x < 3)
print("not x > 5       :", not x > 5)
print("not(x > 5 and x < 10):", not (x > 5 and x < 10))

# Dogruluk tablosu
print("\n  A      B     | and    or")
for A in (True, False):
    for B in (True, False):
        print(f"{A!s:6} {B!s:6} | {A and B!s:6} {A or B}")

# Gercek hayat ornekleri
yas = 20
ehliyet_var = True
print("\nArac kullanabilir mi:", yas >= 18 and ehliyet_var)

hava_yagmurlu = False
semsiye_var = False
print("Islanir mi:", hava_yagmurlu and not semsiye_var)

gun = "Cumartesi"
print("Hafta sonu mu:", gun == "Cumartesi" or gun == "Pazar")

# Kisa devre (short-circuit) degerlendirme
# and: ilk deger False ise ikinciye bakmaz; or: ilk deger True ise ikinciye bakmaz
sayi = 0
print(sayi != 0 and 10 / sayi > 1)     # 10/0 hic calistirilmaz, hata vermez

# and / or aslinda son degerlendirilen degeri dondurur
print(0 or "varsayilan")
print("dolu" or "varsayilan")
print(5 and 10)
print(0 and 10)

isim = ""
print("Merhaba", isim or "misafir")
