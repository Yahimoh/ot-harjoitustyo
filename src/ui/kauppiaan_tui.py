from services.merchant import Merchant

class KauppiaanTUI:

    def __init__(self):
        self._merchant = Merchant()

    def kauppiaan_nakyma_tui(self):
        self.kauppiaan_toiminta_tui()

    def kauppiaan_toiminnon_tulostus(self):
        print("")
        print("Valitse toiminnoista:")
        print("1: Näytä tuotteet")
        print("2: Lisää tuote")
        print("3: Muokkaa tuotetta")
        print("4: Poista tuote")
        print("0: Lopeta käyttö")

    def kauppiaan_toiminta_tui(self):
        while True:
            self.kauppiaan_toiminnon_tulostus()
            valinta = int(input("Valinta 1/2/3/4/0: "))

            if valinta == 1:
                self._merchant.nayta_tuotteet()
            if valinta == 2:
                self._merchant.lisaa_tuote()
            if valinta == 3:
                self._merchant.muokkaa_tuotetta()
            if valinta == 4:
                self._merchant.poista_tuote()
            if valinta == 0:
                print("Lopetetaan")
                break

            if valinta not in (0, 1, 2, 3, 4):
                print("Väärä valinta!")

            print("")