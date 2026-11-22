# 13.3 Exception Handling (Hata Yakalama)
# try - except - else - finally

# 1. Temel kullanim
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print("x / y =", x / y)
except ZeroDivisionError:
    print("y icin 0 girilemez.")
except ValueError:
    print("x ve y icin sayisal deger girmelisiniz.")

# 2. Birden fazla hatayi tek except'te yakalama
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print("x / y =", x / y)
except (ZeroDivisionError, ValueError) as hata:
    print("Hatali bilgi girdiniz.")
    print("Hata:", hata)

# 3. Tum hatalari yakalama (hangi hatanin olustugunu bilmeyiz, dikkatli kullanilmali)
try:
    liste = [1, 2, 3]
    print(liste[int(input("Indeks: "))])
except Exception as hata:
    print(f"Bir hata olustu: {type(hata).__name__} - {hata}")

# 4. else: hata olusmazsa calisir
# 5. finally: hata olussa da olusmasa da her zaman calisir
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        sonuc = x / y
    except Exception as hata:
        print("Hatali giris:", hata)
    else:
        print("Sonuc:", sonuc)
        break
    finally:
        print("try-except bloku sonlandi.")

# 6. finally ile kaynaklari serbest birakma
dosya = None
try:
    dosya = open("ornek_dosya.txt", "w", encoding="utf-8")
    dosya.write("deneme")
    print(10 / 0)                     # hata olusturalim
except ZeroDivisionError:
    print("Sifira bolme hatasi yakalandi.")
finally:
    if dosya:
        dosya.close()
    print("Dosya kapatildi mi:", dosya.closed)

# 7. Ic ice try blogu
try:
    try:
        int("abc")
    except ValueError:
        print("Ic blokta ValueError yakalandi.")
        print(undefined_name)        # yeni bir hata
except NameError:
    print("Dis blokta NameError yakalandi.")
