# 16.4 Desktop (Masaustu) Uygulama Gelistirme
# Python ile masaustu uygulama gelistirmek icin kullanilan kutuphaneler:
#   Tkinter : Python ile birlikte gelir, kurulum gerektirmez
#   PyQt5/6 : profesyonel ve gelismis arayuzler (Qt Designer ile surukle-birak tasarim)
#   PySide6 : Qt'nin resmi Python baglantisi
#
# Bu ornek: Tkinter ile yapilacaklar listesi (To-Do) uygulamasi
# Ubuntu'da gerekirse: sudo apt install python3-tk

import tkinter as tk
from tkinter import messagebox


class YapilacaklarUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Yapilacaklar Listesi")
        self.pencere.geometry("350x400")

        tk.Label(pencere, text="Yapilacaklar", font=("Arial", 16, "bold")).pack(pady=10)

        self.giris = tk.Entry(pencere, width=30, font=("Arial", 12))
        self.giris.pack(pady=5)
        self.giris.bind("<Return>", lambda olay: self.ekle())

        buton_cercevesi = tk.Frame(pencere)
        buton_cercevesi.pack(pady=5)
        tk.Button(buton_cercevesi, text="Ekle", width=10, command=self.ekle).pack(side=tk.LEFT, padx=5)
        tk.Button(buton_cercevesi, text="Sil", width=10, command=self.sil).pack(side=tk.LEFT, padx=5)
        tk.Button(buton_cercevesi, text="Temizle", width=10, command=self.temizle).pack(side=tk.LEFT, padx=5)

        self.liste = tk.Listbox(pencere, width=40, height=12, font=("Arial", 11))
        self.liste.pack(pady=10)

        self.durum = tk.Label(pencere, text="0 gorev")
        self.durum.pack()

    def durumu_guncelle(self):
        self.durum.config(text=f"{self.liste.size()} gorev")

    def ekle(self):
        gorev = self.giris.get().strip()
        if not gorev:
            messagebox.showwarning("Uyari", "Bos gorev eklenemez.")
            return
        self.liste.insert(tk.END, gorev)
        self.giris.delete(0, tk.END)
        self.durumu_guncelle()

    def sil(self):
        secili = self.liste.curselection()
        if not secili:
            messagebox.showinfo("Bilgi", "Silmek icin bir gorev secin.")
            return
        self.liste.delete(secili[0])
        self.durumu_guncelle()

    def temizle(self):
        if messagebox.askyesno("Onay", "Tum gorevler silinsin mi?"):
            self.liste.delete(0, tk.END)
            self.durumu_guncelle()


if __name__ == "__main__":
    pencere = tk.Tk()
    YapilacaklarUygulamasi(pencere)
    pencere.mainloop()
