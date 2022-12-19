from tkinter import ttk, constants

class KauppiaanUI:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Terve kauppias!")

        button = ttk.Button(
            master=self._root,
            text="Kauppias",
            command=self.tulostus()
        )

        label.pack()
        button.pack()

    def tulostus(self):
        print("Asiakas!")