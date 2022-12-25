from services.merchant import Merchant
from ui.asiakkaan_tui import AsiakkaanTUI
from ui.kauppiaan_tui import KauppiaanTUI

class TUI:
    def __init__(self):
        self._asiakkaan_tui = AsiakkaanTUI()
        self._kauppiaan_tui = KauppiaanTUI()
        self._valinta = 0

    def start(self):
        self.intro()

        if self._valinta == 1:
            self._asiakkaan_tui.asiakkaan_nakyma_tui()
        else:
            self._kauppiaan_tui.kauppiaan_nakyma_tui()




    def intro(self):
        print("----------Tervetuloa verkkokauppaan!----------")
        print("")
        print("Oletko asiakas vai kauppias?")
        print("1: Asiakas")
        print("2: Kauppias")

        while True:
            try:
                valinta = int(input("Valinta 1/2: "))
            except:
                print("")
                print("Valinta ei ollut numero, yritä uudestaan")
                continue
            if valinta not in (1, 2):
                print("Väärä valinta!")
                print("Yritä uudelleen.")
                print("")
                continue

            self._valinta = valinta
            break




