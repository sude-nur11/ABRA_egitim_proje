# 16.3 Mobil Uygulama Gelistirme
# Python ile mobil uygulama gelistirmek icin kullanilan kutuphaneler:
#   Kivy    : Android, iOS, Windows, Linux ve macOS'ta calisan arayuzler
#   KivyMD  : Kivy icin Material Design bilesenleri
#   BeeWare : platformun kendi (native) arayuz bilesenlerini kullanir
#
# Kivy uygulamasini Android'e (APK) cevirmek icin Buildozer kullanilir:
#   pip3 install buildozer
#   buildozer init
#   buildozer -v android debug
#
# Bu ornek: Kivy ile basit bir sayac ve selamlama uygulamasi
# Kurulum: pip3 install kivy

try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    from kivy.uix.label import Label
    from kivy.uix.textinput import TextInput
except ImportError:
    print("Kivy kurulu degil. Kurmak icin: pip3 install kivy")
    raise SystemExit


class AnaEkran(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)
        self.sayac = 0

        self.baslik = Label(text="Python ile Mobil Uygulama", font_size=24)
        self.isim_girisi = TextInput(hint_text="Adinizi girin", multiline=False,
                                     size_hint_y=None, height=50)
        self.selam_butonu = Button(text="Selamla", size_hint_y=None, height=50)
        self.sayac_etiketi = Label(text="Sayac: 0", font_size=20)
        self.sayac_butonu = Button(text="Artir", size_hint_y=None, height=50)
        self.sifirla_butonu = Button(text="Sifirla", size_hint_y=None, height=50)

        self.selam_butonu.bind(on_press=self.selamla)
        self.sayac_butonu.bind(on_press=self.artir)
        self.sifirla_butonu.bind(on_press=self.sifirla)

        for bilesen in (self.baslik, self.isim_girisi, self.selam_butonu,
                        self.sayac_etiketi, self.sayac_butonu, self.sifirla_butonu):
            self.add_widget(bilesen)

    def selamla(self, buton):
        isim = self.isim_girisi.text.strip() or "misafir"
        self.baslik.text = f"Merhaba {isim}!"

    def artir(self, buton):
        self.sayac += 1
        self.sayac_etiketi.text = f"Sayac: {self.sayac}"

    def sifirla(self, buton):
        self.sayac = 0
        self.sayac_etiketi.text = "Sayac: 0"


class MobilUygulama(App):
    def build(self):
        self.title = "Ilk Mobil Uygulamam"
        return AnaEkran()


if __name__ == "__main__":
    MobilUygulama().run()
