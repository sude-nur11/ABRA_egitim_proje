# 14.5 Pip ile Harici Paket Kurulumu
# pip, Python paket yoneticisidir. https://pypi.org adresindeki paketleri kurar.
#
# Terminal komutlari:
#   pip3 --version                  -> pip surumu
#   pip3 install requests           -> paket kurma
#   pip3 install requests==2.31.0   -> belirli surumu kurma
#   pip3 install --upgrade requests -> paketi guncelleme
#   pip3 uninstall requests         -> paketi kaldirma
#   pip3 list                       -> kurulu paketleri listeleme
#   pip3 show requests              -> paket bilgisi
#   pip3 freeze > requirements.txt  -> kurulu paketleri dosyaya yazma
#   pip3 install -r requirements.txt-> dosyadaki paketleri kurma
#
# Sanal ortam (virtual environment): her proje icin ayri paketler
#   python3 -m venv venv
#   source venv/bin/activate        (Windows: venv\Scripts\activate)
#   deactivate

import importlib.util
import subprocess
import sys


def paket_kurulu_mu(paket_adi):
    return importlib.util.find_spec(paket_adi) is not None


# Bazi paketlerin kurulu olup olmadigini kontrol etme
for paket in ["requests", "numpy", "pandas", "math"]:
    durum = "kurulu" if paket_kurulu_mu(paket) else "kurulu degil"
    print(f"{paket:<10}: {durum}")

# Kurulu paketleri Python icinden listeleme
sonuc = subprocess.run([sys.executable, "-m", "pip", "list"],
                       capture_output=True, text=True)
satirlar = sonuc.stdout.splitlines()
print(f"\nKurulu paket sayisi: {max(len(satirlar) - 2, 0)}")
for satir in satirlar[:7]:
    print(satir)

# requests paketi ile ornek kullanim (kurulu ise)
if paket_kurulu_mu("requests"):
    import requests

    try:
        cevap = requests.get("https://api.github.com", timeout=5)
        print("\nGitHub API durum kodu:", cevap.status_code)
        print("Ornek alanlar:", list(cevap.json().keys())[:3])
    except requests.RequestException as hata:
        print("Istek basarisiz:", hata)
else:
    print("\nrequests kurulu degil. Kurmak icin: pip3 install requests")

# Paket yoksa ImportError ile kontrol etme
try:
    import olmayan_paket  # noqa: F401
except ImportError:
    print("olmayan_paket bulunamadi. pip3 install olmayan_paket ile kurulmali.")
