from services.merchant import Merchant
from tkinter import ttk, constants
from ui.asiakkaan_ui import AsiakkaanUI
from ui.kauppiaan_ui import KauppiaanUI

class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self.show_asiakkaan_ui()

    def show_asiakkaan_ui(self):
        self.hide_current_view()

        self._current_view = AsiakkaanUI(
            self._root,
            self.show_kauppiaan_ui()
        )
        self._current_view.pack()

    def show_kauppiaan_ui(self):
        self.hide_current_view()

        self._current_view = KauppiaanUI(
            self._root,
        )
        self._current_view.pack()

    def all_that(self):
        """Luokka, jonka avulla näytetään graafista näkymää.. HUOM: Alustava versio

                Attributes:
                    root: Luokalle annettava muokattava ikkuna
                """

        self._root.title("Verkkokauppa")

        intro_label = ttk.Label(master=self._root, text="Tervetuloa Verkkokauppaan!")
        intro_label.config(font=("Courier", 20))

        asiakas_button = ttk.Button(master=self._root, text="Asiakas", command=self.show_asiakkaan_ui())
        kauppias_button = ttk.Button(master=self._root, text="Kauppias", command=self.show_kauppiaan_ui())
        exit_button = ttk.Button(master=self._root, text="Sulje", command=self._root.destroy)

        intro_label.pack(pady=(0, 30))
        asiakas_button.pack()
        kauppias_button.pack()
        exit_button.pack(pady=(50, 0))

    def hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
