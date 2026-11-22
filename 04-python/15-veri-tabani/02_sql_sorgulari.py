# 15.2 SQL Sorgulari
# CRUD islemleri: Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE)
# Once 01_veri_tabani_baglantisi.py calistirilarak tablo olusturulmalidir.

import sqlite3

baglanti = sqlite3.connect("okul.db")
imlec = baglanti.cursor()

# Ornegin her calistirmada ayni sonucu vermesi icin tabloyu temizleyelim
imlec.execute("DELETE FROM ogrenciler")

# --- INSERT: kayit ekleme ---
# Degerler ? yer tutuculari ile verilir (SQL injection saldirilarina karsi guvenli)
imlec.execute(
    "INSERT INTO ogrenciler (ad, soyad, dogum_yili, bolum, ortalama) VALUES (?, ?, ?, ?, ?)",
    ("Sude", "Toprak", 2004, "Bilgisayar", 3.45),
)

# Birden fazla kayit ekleme
ogrenciler = [
    ("Ali", "Yilmaz", 2002, "Elektrik", 2.80),
    ("Ayse", "Demir", 2003, "Bilgisayar", 3.10),
    ("Can", "Kaya", 2001, "Makine", 2.15),
    ("Deniz", "Ak", 2004, "Bilgisayar", 3.75),
]
imlec.executemany(
    "INSERT INTO ogrenciler (ad, soyad, dogum_yili, bolum, ortalama) VALUES (?, ?, ?, ?, ?)",
    ogrenciler,
)
baglanti.commit()
print("Eklenen son kaydin id'si:", imlec.lastrowid)

# --- SELECT: kayit okuma ---
print("\nTum ogrenciler:")
imlec.execute("SELECT * FROM ogrenciler")
for kayit in imlec.fetchall():
    print(kayit)

print("\nSadece ad ve ortalama (ortalamaya gore azalan):")
imlec.execute("SELECT ad, ortalama FROM ogrenciler ORDER BY ortalama DESC")
for ad, ortalama in imlec.fetchall():
    print(f"  {ad:<6} {ortalama}")

print("\nWHERE ile filtreleme (Bilgisayar bolumu, ortalama > 3):")
imlec.execute("SELECT ad, soyad FROM ogrenciler WHERE bolum = ? AND ortalama > ?",
              ("Bilgisayar", 3.0))
print(imlec.fetchall())

print("\nLIKE ile arama (adi 'A' ile baslayanlar):")
imlec.execute("SELECT ad FROM ogrenciler WHERE ad LIKE 'A%'")
print(imlec.fetchall())

print("\nfetchone ile tek kayit:")
imlec.execute("SELECT * FROM ogrenciler WHERE ad = ?", ("Sude",))
print(imlec.fetchone())

print("\nToplama fonksiyonlari ve GROUP BY:")
imlec.execute("SELECT COUNT(*), AVG(ortalama), MAX(ortalama) FROM ogrenciler")
print("  sayi, ortalama, en yuksek:", imlec.fetchone())
imlec.execute("SELECT bolum, COUNT(*) FROM ogrenciler GROUP BY bolum")
print("  bolumlere gore:", imlec.fetchall())

# --- UPDATE: kayit guncelleme ---
imlec.execute("UPDATE ogrenciler SET ortalama = ? WHERE ad = ?", (3.00, "Ali"))
baglanti.commit()
print("\nGuncellenen kayit sayisi:", imlec.rowcount)

# --- DELETE: kayit silme ---
imlec.execute("DELETE FROM ogrenciler WHERE ortalama < ?", (2.5,))
baglanti.commit()
print("Silinen kayit sayisi:", imlec.rowcount)

print("\nSon durum:")
imlec.execute("SELECT id, ad, soyad, ortalama FROM ogrenciler")
for kayit in imlec.fetchall():
    print(kayit)

baglanti.close()
