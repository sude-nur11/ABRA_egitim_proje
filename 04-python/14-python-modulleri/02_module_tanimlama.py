# 14.2 Module Tanimlama
# Ayni klasordeki mymodule.py dosyasini modul olarak kullaniyoruz.

# 1. Tum modulu import etme
import mymodule

print("mymodule.__name__:", mymodule.__name__)
print(mymodule.sehir)
print(mymodule.person["name"])
print(mymodule.numbers)
print(mymodule.merhaba("Sude"))
print(mymodule.topla(10, 20, 30))
print(mymodule.daire_alani(5))

p = mymodule.Person("Ayse", 1995)
print(p, "-", p.yas_hesapla(), "yasinda")

# 2. Takma ad ile
import mymodule as mm

print(mm.merhaba("Ali"))

# 3. Belirli ogeleri import etme
from mymodule import merhaba, Person, numbers

print(merhaba("Can"))
print(Person("Deniz", 2000))
print(numbers)

# 4. Modulde neler oldugunu gorme
ogeler = [oge for oge in dir(mymodule) if not oge.startswith("__")]
print("Moduldeki ogeler:", ogeler)

# Modul ilk import edildiginde bir kez calistirilir, sonraki importlarda tekrar
# calistirilmaz. Degisiklikleri yuklemek icin importlib.reload kullanilir.
import importlib

importlib.reload(mymodule)

# Moduldeki degerler degistirilebilir (ama dosya degismez)
mymodule.sehir = "Izmir"
print(mymodule.sehir)

# Modul bir klasordeyse (paket) su sekilde import edilir:
#   paket_adi/
#       __init__.py
#       modul1.py
#   from paket_adi import modul1
#   from paket_adi.modul1 import fonksiyon

# __name__ degerinin farki
print("Bu dosyanin __name__ degeri:", __name__)
print("mymodule dosyasinin __name__ degeri:", mymodule.__name__)
