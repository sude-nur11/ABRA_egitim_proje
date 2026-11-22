# 5.5 String Metotlari
# dir(str) ile tum string metotlari gorulebilir.

metin = "  Python Programlama Dili  "
temiz = metin.strip()

# Buyuk/kucuk harf metotlari
print(temiz.upper())
print(temiz.lower())
print(temiz.title())
print(temiz.swapcase())
print("python dili".capitalize())

# Bosluk temizleme
print(f"[{metin.strip()}]")
print(f"[{metin.lstrip()}]")
print(f"[{metin.rstrip()}]")
print("***merhaba***".strip("*"))

# Arama metotlari
print(temiz.find("Program"))     # bulundugu indeks, yoksa -1
print(temiz.find("Java"))
print(temiz.index("Dili"))       # yoksa ValueError verir
print(temiz.count("a"))
print(temiz.startswith("Python"))
print(temiz.endswith("Dili"))

# Degistirme
print(temiz.replace("Dili", "Egitimi"))
print(temiz.replace("a", "@", 2))   # sadece ilk 2 tanesini degistir

# Bolme ve birlestirme
kelimeler = temiz.split()
print(kelimeler)
print("ad,soyad,yas".split(","))
print("-".join(kelimeler))
print(" ".join(["Merhaba", "Dunya"]))
print("satir1\nsatir2".splitlines())

# Kontrol metotlari (True / False dondurur)
print("12345".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print("   ".isspace())

# Hizalama metotlari
print("Python".center(20, "-"))
print("Python".ljust(10, "."), "|")
print("Python".rjust(10, "."), "|")
print("7".zfill(3))
