# 8.1 Kosullu Durum Nedir?
# Programin, bir kosulun dogru (True) ya da yanlis (False) olmasina gore
# farkli kodlari calistirmasidir. Python'da if, elif ve else ile yapilir.
#
# Genel yapi:
#   if kosul:
#       kosul True ise calisacak kodlar
#   elif baska_kosul:
#       ilk kosul False, bu kosul True ise calisacak kodlar
#   else:
#       hicbir kosul saglanmazsa calisacak kodlar
#
# Onemli: Python'da bloklar girinti (4 bosluk) ile belirlenir.

# Kosul ifadeleri bool deger uretir
yas = 20
print("yas >= 18 ->", yas >= 18)

# Bu bool degere gore karar verilir
if yas >= 18:
    print("Resitsiniz.")

# Kosul saglanmazsa if blogu atlanir
if yas < 18:
    print("Bu satir calismaz.")

print("if blogundan sonra program devam eder.")

# Girintinin onemi
sicaklik = 35
if sicaklik > 30:
    print("Hava cok sicak.")       # if blogunun icinde
    print("Bol su icin.")          # if blogunun icinde
print("Hava durumu kontrol edildi.")   # if blogunun disinda, her zaman calisir

# Truthy / Falsy degerler: kosul yerine dogrudan deger de yazilabilir
# 0, "", [], {}, None -> False; digerleri True kabul edilir
isim = ""
if isim:
    print("Isim girildi.")
if not isim:
    print("Isim bos birakildi.")

sepet = ["elma", "ekmek"]
if sepet:
    print("Sepette", len(sepet), "urun var.")

# Gercek hayattan bir akis ornegi: trafik isigi
isik = "kirmizi"
if isik == "yesil":
    print("Gecebilirsiniz.")
elif isik == "sari":
    print("Hazirlanin.")
else:
    print("Durun!")
