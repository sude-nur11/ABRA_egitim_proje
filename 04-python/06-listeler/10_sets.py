# 6.10 Sets (Kumeler)
# Set; sirasiz, indekslenemeyen ve TEKRAR ETMEYEN elemanlardan olusur. {} ile tanimlanir.

meyveler = {"elma", "armut", "muz", "elma"}
print(meyveler)                  # tekrar eden "elma" bir kez gorunur
print(len(meyveler))

bos_kume = set()                 # {} bos sozluk olusturur!
print(type(bos_kume), type({}))

# Sirasiz oldugu icin indeksle erisilemez
# meyveler[0]  -> TypeError
for meyve in meyveler:
    print(meyve)
print("muz" in meyveler)

# Eleman ekleme
meyveler.add("kiraz")
meyveler.update(["kivi", "cilek"])
print(meyveler)

# Eleman silme
meyveler.remove("kivi")          # yoksa KeyError verir
meyveler.discard("ananas")       # yoksa hata vermez
rastgele = meyveler.pop()        # rastgele bir eleman siler
print("pop:", rastgele, meyveler)

# Listedeki tekrarlari temizleme
sayilar = [1, 2, 2, 3, 3, 3, 4]
print(list(set(sayilar)))

# Kume islemleri
python_bilenler = {"Sude", "Ali", "Ayse", "Can"}
cpp_bilenler = {"Ali", "Can", "Deniz"}

print("Birlesim:", python_bilenler | cpp_bilenler)
print("Kesisim:", python_bilenler & cpp_bilenler)
print("Sadece Python:", python_bilenler - cpp_bilenler)
print("Sadece birini bilen:", python_bilenler ^ cpp_bilenler)

print(python_bilenler.union(cpp_bilenler))
print(python_bilenler.intersection(cpp_bilenler))
print(python_bilenler.difference(cpp_bilenler))

# Alt kume / ust kume
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b), b.issuperset(a), a.isdisjoint({5, 6}))

# frozenset: degistirilemeyen kume
sabit = frozenset([1, 2, 3])
print(sabit)
