# 16.1 Python ile Neler Yapabilirim?
#
# Alan                         | Populer kutuphaneler
# -----------------------------+------------------------------------------
# Web gelistirme               | Django, Flask, FastAPI
# Mobil uygulama               | Kivy, BeeWare
# Masaustu (desktop) uygulama  | Tkinter, PyQt, PySide
# Veri bilimi / analizi        | NumPy, Pandas, Matplotlib, Seaborn
# Yapay zeka / makine ogrenmesi| scikit-learn, TensorFlow, PyTorch
# Otomasyon / web kazima       | requests, BeautifulSoup, Selenium
# Goruntu isleme               | OpenCV, Pillow
# Oyun gelistirme              | Pygame
# Gomulu sistemler / IoT       | MicroPython, RPi.GPIO
# Drone / robotik              | DroneKit, pymavlink, ROS
#
# Asagida sadece standart kutuphane kullanilarak birkac alandan kucuk ornekler var.

import json
import os
import random
import statistics
from collections import Counter
from datetime import datetime

# 1. Otomasyon: klasordeki dosyalari uzantilarina gore sayma
uzantilar = Counter(os.path.splitext(f)[1] or "(uzantisiz)"
                    for f in os.listdir(".") if os.path.isfile(f))
print("1- Otomasyon - dosya uzantilari:", dict(uzantilar))

# 2. Veri analizi: haftalik sicaklik verisinin analizi
sicakliklar = {"Pzt": 12, "Sal": 15, "Car": 14, "Per": 18, "Cum": 21, "Cmt": 19, "Paz": 16}
degerler = list(sicakliklar.values())
print("2- Veri analizi - ortalama:", round(statistics.mean(degerler), 1),
      "| medyan:", statistics.median(degerler),
      "| en sicak gun:", max(sicakliklar, key=sicakliklar.get))

# 3. Basit metin tabanli grafik
print("3- Grafik:")
for gun, derece in sicakliklar.items():
    print(f"   {gun} | {'#' * derece} {derece}")

# 4. Web / API: veriyi JSON formatina cevirme (web servislerinin ortak dili)
api_cevabi = json.dumps({"zaman": datetime.now().isoformat(timespec="seconds"),
                         "sicakliklar": sicakliklar}, indent=2)
print("4- JSON ciktisi:\n", api_cevabi)

# 5. Oyun: zar atma simulasyonu
atislar = [random.randint(1, 6) for _ in range(600)]
print("5- 600 zar atisinin dagilimi:", sorted(Counter(atislar).items()))

# 6. Guvenlik: rastgele guclu parola uretme
import secrets
import string

karakterler = string.ascii_letters + string.digits + "!?*-_"
parola = "".join(secrets.choice(karakterler) for _ in range(12))
print("6- Uretilen parola:", parola)
