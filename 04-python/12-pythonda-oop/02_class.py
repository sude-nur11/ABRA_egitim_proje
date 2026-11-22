# 12.2 Class (Sinif)
# class anahtar kelimesi ile tanimlanir. Sinif isimleri PascalCase yazilir.

class Person:
    # sinif nitelikleri (class attributes): tum nesneler icin ortaktir
    name = "isimsiz"
    year = 2000
    address = "belirtilmemis"


# Siniftan nesne (instance) olusturma
p1 = Person()
p2 = Person()

print(p1)
print(type(p1))
print(p1.name, p1.year, p1.address)
print(p2.name, p2.year, p2.address)

# Nesneye ozel deger atama
p1.name = "Sude"
p1.year = 2004
p2.name = "Ali"
print(p1.name, p1.year)
print(p2.name, p2.year)

# Siniftaki degeri degistirmek, kendi degeri olmayan nesneleri etkiler
Person.address = "Ankara"
print(p1.address, p2.address)

# Nesnelere sonradan yeni nitelik eklenebilir (onerilmez)
p1.email = "sude@ornek.com"
print(p1.email)
# print(p2.email)  -> AttributeError

# Farkli nesneler bellekte farkli yerlerde durur
print(p1 is p2, id(p1), id(p2))


# Bos sinif
class Bos:
    pass


b = Bos()
print(type(b))

# Nesnenin niteliklerini gorme
print(p1.__dict__)        # sadece nesneye ozel atanmis nitelikler
print(p2.__dict__)
print(Person.__dict__["year"])

# hasattr, getattr, setattr
print(hasattr(p1, "email"))
print(getattr(p2, "name"))
setattr(p2, "year", 1999)
print(p2.year)


class Kedi:
    tur = "memeli"
    ayak_sayisi = 4


k = Kedi()
print(f"Kedi bir {k.tur} hayvandir ve {k.ayak_sayisi} ayagi vardir.")
