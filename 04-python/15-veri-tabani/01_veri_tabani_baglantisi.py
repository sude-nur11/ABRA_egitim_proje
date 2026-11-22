# 15.1 Veri Tabani Baglantisi
# SQLite: Python ile birlikte gelen, sunucu gerektirmeyen, dosya tabanli bir veri tabanidir.
# sqlite3 modulu ile kullanilir. (MySQL icin: pip3 install mysql-connector-python)
#
# Temel adimlar:
#   1. connect()  -> veri tabanina baglan (dosya yoksa olusturulur)
#   2. cursor()   -> SQL komutlarini calistiracak imlec olustur
#   3. execute()  -> SQL komutunu calistir
#   4. commit()   -> degisiklikleri kaydet
#   5. close()    -> baglantiyi kapat

import sqlite3

# 1. Baglanti
baglanti = sqlite3.connect("okul.db")
print("Veri tabanina baglanildi.")
print("SQLite surumu:", sqlite3.sqlite_version)

# 2. Imlec
imlec = baglanti.cursor()

# 3. Tablo olusturma
imlec.execute("""
    CREATE TABLE IF NOT EXISTS ogrenciler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        soyad TEXT NOT NULL,
        dogum_yili INTEGER,
        bolum TEXT,
        ortalama REAL DEFAULT 0
    )
""")

imlec.execute("""
    CREATE TABLE IF NOT EXISTS dersler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT UNIQUE NOT NULL,
        kredi INTEGER
    )
""")

# 4. Kaydetme
baglanti.commit()

# Veri tabanindaki tablolari listeleme
imlec.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tablolar:", [t[0] for t in imlec.fetchall()])

# Tablonun sutunlarini gorme
imlec.execute("PRAGMA table_info(ogrenciler)")
for sutun in imlec.fetchall():
    print(f"  sutun: {sutun[1]:<12} tip: {sutun[2]}")

# 5. Baglantiyi kapatma
baglanti.close()
print("Baglanti kapatildi.")

# with ile baglanti: blok sonunda commit (hata varsa rollback) otomatik yapilir
with sqlite3.connect("okul.db") as baglanti:
    imlec = baglanti.cursor()
    imlec.execute("SELECT COUNT(*) FROM ogrenciler")
    print("Ogrenci sayisi:", imlec.fetchone()[0])

# Hatali SQL komutu yakalama
try:
    with sqlite3.connect("okul.db") as baglanti:
        baglanti.execute("SELECT * FROM olmayan_tablo")
except sqlite3.OperationalError as hata:
    print("Veri tabani hatasi:", hata)
