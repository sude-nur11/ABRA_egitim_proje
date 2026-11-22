# 14.1 Module Nedir?
# Modul; icinde fonksiyon, sinif ve degiskenler bulunan bir Python dosyasidir (.py).
# Kodu parcalara ayirmayi, tekrar kullanmayi ve duzenli tutmayi saglar.
#
# Modul turleri:
# 1. Standart kutuphane modulleri: Python ile birlikte gelir (math, random, os, datetime ...)
# 2. Harici (3. parti) moduller   : pip ile kurulur (requests, numpy, pandas ...)
# 3. Kendi yazdigimiz moduller     : kendi .py dosyalarimiz

# 1. Modulun tamamini import etme
import math

print(math.sqrt(49))
print(math.pi)
print(math.factorial(5))

# 2. Takma ad (alias) ile import etme
import math as m

print(m.pow(2, 8))

# 3. Moduldeki belirli ogeleri import etme (modul adi yazmadan kullanilir)
from math import sqrt, ceil, floor

print(sqrt(81), ceil(4.2), floor(4.8))

# 4. Belirli bir ogeyi takma ad ile import etme
from math import factorial as fakt

print(fakt(6))

# 5. Moduldeki her seyi import etme (isim cakismasina yol acabilecegi icin onerilmez)
from random import *

print(randint(1, 10))

# Modulun icindekileri listeleme
print(dir(math))

# Bir fonksiyonun aciklamasini okuma
print(math.sqrt.__doc__)
# help(math) -> modulun tum dokumantasyonu

# Modulun dosya konumu ve adi
import os

print(os.__name__)
print(os.__file__)

# Isim cakismasi ornegi: kendi fonksiyonumuz modul fonksiyonunu ezebilir
def sqrt(x):
    return "kendi sqrt fonksiyonum"


print(sqrt(9))          # artik kendi fonksiyonumuz calisir
print(math.sqrt(9))     # modul adi ile kullanmak bu sorunu onler

# Python'un modulleri aradigi klasorler
import sys

for yol in sys.path[:3]:
    print("Arama yolu:", yol)
