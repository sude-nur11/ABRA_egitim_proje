# 10.4 Fonksiyona Parametre Gonderme
# Parametre: fonksiyon tanimlanirken yazilan degisken
# Arguman  : fonksiyon cagrilirken gonderilen deger

def selamla(isim):              # isim -> parametre
    print(f"Merhaba {isim}")


selamla("Sude")                 # "Sude" -> arguman
selamla("Ali")


def topla(a, b):
    return a + b


print(topla(3, 5))
print(topla(10, 20))
print(topla("Py", "thon"))      # + operatoru stringlerde de calisir


def dikdortgen(uzun, kisa):
    alan = uzun * kisa
    cevre = 2 * (uzun + kisa)
    return alan, cevre


alan, cevre = dikdortgen(8, 5)
print("Alan:", alan, "Cevre:", cevre)


# Parametre sayisi eksik veya fazla olursa hata olusur
try:
    topla(1)
except TypeError as hata:
    print("Hata:", hata)


# Liste parametresi
def listeyi_analiz_et(sayilar):
    return {
        "toplam": sum(sayilar),
        "ortalama": sum(sayilar) / len(sayilar),
        "en_buyuk": max(sayilar),
        "en_kucuk": min(sayilar),
    }


print(listeyi_analiz_et([4, 8, 15, 16, 23, 42]))


# Fonksiyona gonderilen liste fonksiyon icinde degisirse disarida da degisir
def eleman_ekle(liste, eleman):
    liste.append(eleman)


meyveler = ["elma"]
eleman_ekle(meyveler, "armut")
print(meyveler)


# Fonksiyon parametre olarak fonksiyon alabilir
def islem_yap(fonksiyon, x, y):
    return fonksiyon(x, y)


print(islem_yap(topla, 4, 6))
print(islem_yap(max, 4, 6))


# Kullanicidan alinan degerlerle
def us_al(taban, us):
    return taban ** us


t = int(input("Taban: "))
u = int(input("Us: "))
print(f"{t}^{u} = {us_al(t, u)}")
