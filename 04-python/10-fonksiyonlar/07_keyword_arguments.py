# 10.7 Keyword Arguments (Isimli Argumanlar)
# Argumanlar parametre isimleriyle gonderilirse sira onemli olmaz.

def bilgi_yazdir(ad, soyad, yas, sehir):
    print(f"{ad} {soyad}, {yas} yasinda, {sehir}")


# Sirali (positional) argumanlar
bilgi_yazdir("Sude", "Toprak", 22, "Ankara")

# Isimli (keyword) argumanlar
bilgi_yazdir(sehir="Izmir", yas=30, soyad="Yilmaz", ad="Ali")

# Karisik kullanim: once sirali, sonra isimli
bilgi_yazdir("Ayse", "Demir", sehir="Bursa", yas=25)

# Isimliden sonra sirali arguman yazilamaz
# bilgi_yazdir(ad="Can", "Kaya", 20, "Rize")   -> SyntaxError

# Ayni parametreye iki kez deger verilemez
try:
    bilgi_yazdir("Can", ad="Can", soyad="Kaya", yas=20, sehir="Rize")
except TypeError as hata:
    print("Hata:", hata)


# Default parametreler ile birlikte kullanim
def mail_gonder(alici, konu="Konu yok", mesaj="", oncelik="normal"):
    print(f"Alici: {alici} | Konu: {konu} | Oncelik: {oncelik}")
    print(f"Mesaj: {mesaj or '(bos)'}")


mail_gonder("sude@ornek.com")
mail_gonder("ali@ornek.com", oncelik="yuksek")
mail_gonder("ayse@ornek.com", mesaj="Toplanti saat 3'te", konu="Toplanti")


# Sadece isimli gonderilebilen parametreler (* isaretinden sonrakiler)
def baglan(sunucu, *, port=80, guvenli=False):
    protokol = "https" if guvenli else "http"
    print(f"{protokol}://{sunucu}:{port}")


baglan("ornek.com")
baglan("ornek.com", port=443, guvenli=True)
try:
    baglan("ornek.com", 443)
except TypeError as hata:
    print("Hata:", hata)

# Hazir fonksiyonlarda keyword argument kullanimi
sayilar = [5, 2, 9, 1]
print(sorted(sayilar, reverse=True))
print(sorted(["elma", "Kiraz", "armut"], key=str.lower))
print("a", "b", sep=" | ")
