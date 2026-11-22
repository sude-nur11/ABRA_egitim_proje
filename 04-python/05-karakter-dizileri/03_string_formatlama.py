# 5.3 String Formatlama

ad = "Sude"
yas = 22
ortalama = 3.4567
bakiye = 1234567.891

# 1. Birlestirme ile (sayilar str'ye cevrilmeli)
print("Adim " + ad + ", yasim " + str(yas))

# 2. % operatoru (eski yontem)
print("Adim %s, yasim %d" % (ad, yas))
print("Ortalamam %.2f" % ortalama)

# 3. format() metodu
print("Adim {}, yasim {}".format(ad, yas))
print("Adim {0}, yasim {1}. {0} bir ogrencidir.".format(ad, yas))
print("Adim {isim}, yasim {y}".format(isim=ad, y=yas))
print("Ortalama: {:.2f}".format(ortalama))

# 4. f-string (Python 3.6+, onerilen yontem)
print(f"Adim {ad}, yasim {yas}")
print(f"5 yil sonra {yas + 5} yasinda olacagim")
print(f"Adimin buyuk hali: {ad.upper()}")
print(f"Ortalama: {ortalama:.1f}")

# Sayi bicimlendirme
print(f"Bakiye: {bakiye:,.2f} TL")      # binlik ayirici
print(f"Yuzde: {0.8567:.1%}")           # yuzde formati
print(f"Sira no: {7:03d}")              # basa sifir ekleme
print(f"Ikilik: {10:b}, Onaltilik: {255:x}")

# Hizalama: < sola, > saga, ^ ortaya
print(f"|{ad:<10}|")
print(f"|{ad:>10}|")
print(f"|{ad:^10}|")
print(f"|{ad:*^10}|")                   # bosluklari * ile doldurma

# Tablo seklinde cikti
urunler = [("Kalem", 15.5), ("Defter", 42.0), ("Silgi", 7.25)]
print(f"{'Urun':<10}{'Fiyat':>10}")
print("-" * 20)
for urun, fiyat in urunler:
    print(f"{urun:<10}{fiyat:>10.2f}")
