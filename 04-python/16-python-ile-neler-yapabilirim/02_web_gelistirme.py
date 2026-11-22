# 16.2 Web Gelistirme
# Python ile web gelistirmede en cok kullanilan frameworkler:
#   Django : buyuk projeler icin, admin paneli, ORM gibi her seyi hazir sunar
#   Flask  : hafif ve esnek, kucuk/orta projeler ve API'ler icin
#   FastAPI: modern, hizli REST API gelistirme
#
# Bu ornekte Flask kullanildi. Kurulum: pip3 install flask
# Calistirma: python3 02_web_gelistirme.py  ->  tarayicida http://127.0.0.1:5000

try:
    from flask import Flask, jsonify, request
except ImportError:
    print("Flask kurulu degil. Kurmak icin: pip3 install flask")
    raise SystemExit

app = Flask(__name__)

# Ornek veri (normalde veri tabanindan gelir)
urunler = [
    {"id": 1, "ad": "Laptop", "fiyat": 25000},
    {"id": 2, "ad": "Telefon", "fiyat": 18000},
    {"id": 3, "ad": "Kulaklik", "fiyat": 1500},
]


@app.route("/")
def anasayfa():
    liste = "".join(f"<li>{u['ad']} - {u['fiyat']} TL</li>" for u in urunler)
    return f"""
        <h1>Python ile Web Gelistirme</h1>
        <p>Flask ile olusturulmus basit bir web sayfasi.</p>
        <ul>{liste}</ul>
        <a href="/api/urunler">JSON API</a>
    """


@app.route("/merhaba/<isim>")
def merhaba(isim):
    return f"<h2>Merhaba {isim}!</h2>"


# REST API: tum urunler
@app.route("/api/urunler", methods=["GET"])
def urun_listesi():
    return jsonify(urunler)


# REST API: tek urun
@app.route("/api/urunler/<int:urun_id>", methods=["GET"])
def urun_getir(urun_id):
    for urun in urunler:
        if urun["id"] == urun_id:
            return jsonify(urun)
    return jsonify({"hata": "Urun bulunamadi"}), 404


# REST API: yeni urun ekleme (POST)
@app.route("/api/urunler", methods=["POST"])
def urun_ekle():
    veri = request.get_json()
    yeni = {"id": len(urunler) + 1, "ad": veri["ad"], "fiyat": veri["fiyat"]}
    urunler.append(yeni)
    return jsonify(yeni), 201


if __name__ == "__main__":
    app.run(debug=True)
