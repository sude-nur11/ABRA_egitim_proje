# 14.4 Standart Kutuphane Modulleri
# Python ile birlikte gelen, kurulum gerektirmeyen moduller.
# Tam liste: https://docs.python.org/3/library/

# --- math: matematiksel islemler ---
import math

print("math:", math.sqrt(144), math.ceil(2.1), math.floor(2.9), math.gcd(24, 36))
print("      ", round(math.sin(math.radians(30)), 2), math.log10(1000), math.pi)

# --- random: rastgele sayilar ---
import random

print("random:", random.random(), random.randint(1, 6), random.uniform(1, 10))
liste = ["elma", "armut", "muz", "kiraz"]
print("        ", random.choice(liste), random.sample(liste, 2))
random.shuffle(liste)
print("        ", liste)

# --- datetime: tarih ve saat ---
from datetime import datetime, date, timedelta

simdi = datetime.now()
print("datetime:", simdi)
print("          ", simdi.strftime("%d.%m.%Y %H:%M:%S"))
print("          ", simdi.year, simdi.month, simdi.day)
dogum = date(2004, 5, 19)
print("          Yasanan gun:", (date.today() - dogum).days)
print("          30 gun sonra:", date.today() + timedelta(days=30))
print("          ", datetime.strptime("21/11/2026", "%d/%m/%Y"))

# --- time: zaman islemleri ---
import time

baslangic = time.time()
time.sleep(0.5)
print(f"time: gecen sure {time.time() - baslangic:.2f} sn")

# --- os: isletim sistemi islemleri ---
import os

print("os:", os.name, os.getcwd())
print("    Klasordeki dosyalar:", os.listdir(".")[:5])

# --- sys: Python yorumlayicisi ile ilgili bilgiler ---
import sys

print("sys:", sys.version.split()[0], sys.platform)

# --- json: JSON veri formatiyla calisma ---
import json

ogrenci = {"ad": "Sude", "dersler": ["Python", "C++"]}
metin = json.dumps(ogrenci)
print("json:", metin, type(metin))
print("      ", json.loads(metin)["dersler"])

# --- statistics: istatistik ---
import statistics

notlar = [70, 85, 90, 45, 60]
print("statistics:", statistics.mean(notlar), statistics.median(notlar))

# --- collections: ozel veri yapilari ---
from collections import Counter

print("collections:", Counter("programlama").most_common(3))
