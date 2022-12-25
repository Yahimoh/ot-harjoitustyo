from services.merchant import Merchant
from entities.tuote import Tuote

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

            try:
                valinta = int(input("Valinta 1/2/3/4/0: "))
            except:
                print("")
                print("Vääränlainen valinta")
                print("Yritä uudestaan")
                continue

            if valinta == 1:
                self.nayta_tuotteet_tui()
            if valinta == 2:
                self.lisaa_tuote_tui()
            if valinta == 3:
                self.muokkaa_tuotetta_tui()
            if valinta == 4:
                self.poista_tuote_tui()
            if valinta == 0:
                print("Lopetetaan")
                break

            if valinta not in (0, 1, 2, 3, 4):
                print("Väärä valinta!")


            print("")

    def lisaa_tuote_tui(self):
        print("")
        nimi = input("Anna tuotteen nimi: ")
        hinta = float(input("Anna tuotteen hinta: "))
        tuote = Tuote(nimi, hinta)

        palautus = self._merchant.lisaa_tuote(tuote)

        if palautus == 1:
            print("Tuote luotu onnistuneesti!")
        else:
            print("Tuote on jo olemassa.")
        print("------------------------------------------------------")

    def muokkaa_tuotetta_tui(self):
        self.nayta_tuotteet_tui()
        print("")

        try:
            muokattavan_tuotteen_id = int(input("Valitse muokattavan tuotteen id: "))
        except:
            print("Väärä valinta")
            print("------------------------------------------------------")
            return

        try:
            valinta = int(input("Tee valinta, muokkaa tuotteen: 1 nimi, 2 hinta: "))
        except:
            print("Väärä valinta")
            print("------------------------------------------------------")
            return

        if valinta == 1:
            uusi_nimi = input("Tuotteen uusi nimi: ")
            self._merchant.muokkaa_tuotetta(True, uusi_nimi, muokattavan_tuotteen_id)

        if valinta == 2:
            uusi_hinta = float(input("Tuotteen uusi hinta: "))
            self._merchant.muokkaa_tuotetta(False,  uusi_hinta, muokattavan_tuotteen_id)

        print("------------------------------------------------------")

    def poista_tuote_tui(self):
        self.nayta_tuotteet_tui()

        try:
            poistettavan_tuotteen_id = int(input("Valitse poistettavan tuotteen id: "))
        except:
            print("Väärä valinta")
            print("------------------------------------------------------")
            return

        self._merchant.poista_tuote(poistettavan_tuotteen_id)

        print("------------------------------------------------------")

    def nayta_tuotteet_tui(self):
        tuotteet = self._merchant.nayta_tuotteet()

        for tuote in tuotteet:
            print(f"{tuote[0]}: {tuote[1]}, {tuote[2]}€")
