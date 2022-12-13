from services.merchant import Merchant
import tkinter as tk

class UI:

    def start(self, root):
        """Luokka, jonka avulla näytetään graafista näkymää.. HUOM: Alustava versio

        Attributes:
            root: Luokalle annettava muokattava ikkuna
        """

        root.title("Verkkokauppa")

        intro_label = tk.Label(root, text="Tervetuloa Verkkokauppaan!")
        intro_label.config(font=("Courier", 20))

        exit_button = tk.Button(root, text="Sulje", command=root.destroy)

        asiakas_button = tk.Button(root, text="Asiakas", command = self.asiakas_nakyma())

        kauppias_button = tk.Button(root, text="Kauppias")

        intro_label.pack(pady=(0, 30))
        asiakas_button.pack()
        kauppias_button.pack()
        exit_button.pack(pady=(50, 0))

    def asiakas_nakyma(self):
        """Luokka, jonka avulla näytetään graafista näkymää asiakkaalle.. HUOM: Alustava versio
        """

        asiakkaan_nakyma = tk.Tk()
        intro_label = tk.Label(asiakkaan_nakyma, text="Tervetuloa asiakkaan näkymään!")
        intro_label.pack(pady=(0, 30))

        asiakkaan_nakyma.mainloop()
