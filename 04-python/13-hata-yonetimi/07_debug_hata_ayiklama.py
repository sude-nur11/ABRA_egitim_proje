# 13.7 Debug - Hata Ayiklama
# Debug, programdaki hatalari (bug) bulup duzeltme surecidir.
#
# VS Code ile debug:
#   1. Satir numarasinin solu tiklanarak breakpoint (kirmizi nokta) eklenir.
#   2. F5 ile "Python Debugger" secilerek program debug modunda baslatilir.
#   3. Program breakpoint'te durur. Sol panelde degiskenlerin degerleri gorulur.
#   4. F10 (Step Over)  : bir sonraki satira gec
#      F11 (Step Into)  : fonksiyonun icine gir
#      Shift+F11        : fonksiyondan cik
#      F5 (Continue)    : bir sonraki breakpoint'e kadar devam et
#   5. "Watch" panelinden istenilen ifade izlenebilir.
#
# Komut satirindan debug: python3 -m pdb dosya_adi.py
# Kod icinden debug: breakpoint() fonksiyonu yazilan satirda program durur.


# Ornek: Icinde hata bulunan fonksiyon
def ortalama_hesapla_hatali(notlar):
    toplam = 0
    for i in range(1, len(notlar)):      # HATA: ilk eleman (indeks 0) atlaniyor
        toplam += notlar[i]
    return toplam / len(notlar)


notlar = [80, 90, 100]
print("Hatali ortalama:", ortalama_hesapla_hatali(notlar))    # 63.33 (beklenen 90)


# 1. Yontem: print ile debug (degiskenlerin degerlerini ekrana yazdirma)
def ortalama_print_debug(notlar):
    toplam = 0
    for i in range(1, len(notlar)):
        print(f"  [DEBUG] i={i}, eleman={notlar[i]}, toplam={toplam}")
        toplam += notlar[i]
    return toplam / len(notlar)


ortalama_print_debug(notlar)       # cikti incelenince indeks 0'in hic gelmedigi gorulur


# 2. Yontem: breakpoint() ile durdurma (asagidaki satirin yorumunu kaldirip deneyin)
def ortalama_breakpoint(notlar):
    toplam = 0
    for not_ in notlar:
        # breakpoint()    # pdb komutlari: n (sonraki), p toplam (yazdir), c (devam), q (cik)
        toplam += not_
    return toplam / len(notlar)


# 3. Yontem: assert ile varsayimlari kontrol etme
def ortalama_dogru(notlar):
    assert len(notlar) > 0, "Not listesi bos olamaz"
    toplam = 0
    for not_ in notlar:
        toplam += not_
    return toplam / len(notlar)


print("Dogru ortalama:", ortalama_dogru(notlar))
print("Breakpoint ornegi:", ortalama_breakpoint(notlar))
try:
    ortalama_dogru([])
except AssertionError as hata:
    print("AssertionError:", hata)

# 4. Yontem: traceback ile hatanin hangi satirda olustugunu gorme
import traceback

try:
    ortalama_dogru(["80", 90])
except TypeError:
    traceback.print_exc()
