from tkinter import ttk, constants

class AsiakkaanUI:
    def __init__(self, root, show_kauppiaan_ui):
        self._root = root
        self._frame = None
        self._show_kauppiaan_ui = show_kauppiaan_ui

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Terve asiakas!")

        button = ttk.Button(
            master=self._root,
            text="Kauppias",
            command=self._show_kauppiaan_ui
        )

        label.pack()
        button.pack()

    def tulostus(self):
        print("Asiakas tulostettu!")