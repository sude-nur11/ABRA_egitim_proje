# 16.5 Veri Bilimi
# Veri bilimi; veriyi toplama, temizleme, analiz etme ve gorsellestirme surecidir.
# Kullanilan kutuphaneler:
#   NumPy      : hizli sayisal hesaplamalar ve diziler
#   Pandas     : tablo (DataFrame) seklinde veri analizi
#   Matplotlib : grafik cizme
#   Seaborn    : istatistiksel gorsellestirme
#   scikit-learn: makine ogrenmesi
#
# Kurulum: pip3 install numpy pandas matplotlib

try:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
except ImportError:
    print("Gerekli paketler kurulu degil. Kurmak icin: pip3 install numpy pandas matplotlib")
    raise SystemExit

# --- NumPy ---
notlar = np.array([70, 85, 90, 45, 60, 95, 78])
print("NumPy dizisi:", notlar)
print("Ortalama:", notlar.mean(), "| Std sapma:", round(notlar.std(), 2))
print("50 ustu:", notlar[notlar > 50])
print("10 puan eklenmis:", notlar + 10)

# --- Pandas ---
veri = {
    "ad": ["Sude", "Ali", "Ayse", "Can", "Deniz", "Ece"],
    "bolum": ["Bilgisayar", "Elektrik", "Bilgisayar", "Makine", "Bilgisayar", "Elektrik"],
    "vize": [70, 55, 80, 40, 90, 65],
    "final": [85, 60, 75, 50, 95, 70],
}
df = pd.DataFrame(veri)
df["ortalama"] = df["vize"] * 0.4 + df["final"] * 0.6
df["durum"] = np.where(df["ortalama"] >= 50, "gecti", "kaldi")

print("\nDataFrame:")
print(df)
print("\nIstatistikler:")
print(df[["vize", "final", "ortalama"]].describe().round(2))
print("\nBolumlere gore ortalama:")
print(df.groupby("bolum")["ortalama"].mean().round(2))
print("\nOrtalamasi 70 ustu olanlar:")
print(df[df["ortalama"] > 70][["ad", "ortalama"]])

# Veriyi CSV dosyasina kaydetme ve geri okuma
df.to_csv("ogrenci_notlari.csv", index=False)
print("\nCSV'den okunan ilk 2 satir:")
print(pd.read_csv("ogrenci_notlari.csv").head(2))

# --- Matplotlib ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.bar(df["ad"], df["ortalama"], color="steelblue")
ax1.axhline(50, color="red", linestyle="--", label="gecme notu")
ax1.set_title("Ogrenci Ortalamalari")
ax1.set_ylabel("Ortalama")
ax1.legend()

ax2.scatter(df["vize"], df["final"], color="darkorange")
ax2.set_title("Vize - Final Iliskisi")
ax2.set_xlabel("Vize")
ax2.set_ylabel("Final")

plt.tight_layout()
plt.savefig("grafik.png")
print("\nGrafik grafik.png dosyasina kaydedildi.")
plt.show()
