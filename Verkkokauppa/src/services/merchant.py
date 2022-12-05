from entities.tuote import Tuote
from repositories.database import Database

class Merchant:

    def __init__(self):
        self.db = Database() # pylint: disable=invalid-name

    def start(self, kayttaja: str):
        if kayttaja == "asiakas":
            self.asiakkaan_toiminta()
        else:
            self.kauppiaan_toiminta()

    def asiakkaan_toiminta(self):
        print("")
        print("----------Tervetuloa verkkokaupan asiakkaaksi!----------")
        print("")

        while True:
            print("Valitse toiminnoista:")
            print("1: Katso saatavilla olevat tuotteet")
            print("2: Katso ostoskorin tuotteet")
            print("3: Lisää tuote ostoskoriin")
            print("4: Poista tuote ostoskorilta")
            print("5: Lopeta käyttö")
            valinta = int(input("Valinta 1/2/3/4/5: "))

            if valinta == 1:
                self.nayta_tuotteet()
            if valinta == 2:
                self.nayta_ostoskorin_tuotteet()
            if valinta == 3:
                self.lisaa_tuote_ostoskoriin()
            if valinta == 4:
                self.poista_tuote_ostoskorista()
            if valinta == 5:
                print("Lopetetaan")
                break

            if valinta not in (1, 2, 3, 4, 5):
                print("Väärä valinta!")

            print("")

    def kauppiaan_toiminta(self):
        print("")
        print("Kauppiaan näkymä: ")

        while True:
            print("Valitse toiminnoista:")
            print("1: Näytä tuotteet")
            print("2: Lisää tuote")
            print("3: Muokkaa tuotetta")
            print("4: Poista tuote")
            print("5: Lopeta käyttö")
            valinta = int(input("Valinta 1/2/3/4: "))

            if valinta == 1:
                self.nayta_tuotteet()
            if valinta == 2:
                self.lisaa_tuote()
            if valinta == 3:
                self.muokkaa_tuotetta()
            if valinta == 4:
                self.poista_tuote()
            if valinta == 5:
                print("Lopetetaan")
                break

            if valinta not in (1, 2, 3, 4, 5):
                print("Väärä valinta!")

            print("")

    def lisaa_tuote(self):
        nimi = input("Anna tuotteen nimi: ")
        hinta = float(input("Anna tuotteen hinta: "))

        tuote = Tuote(nimi, hinta)

        self.db.luo_tuote(tuote)
        print("------------------------------------------------------")

    def muokkaa_tuotetta(self):
        self.nayta_tuotteet()
        print("")

        muokattavan_tuotteem_id = int(input("Valitse muokattavan tuotteen id: "))
        valinta = int(input("Tee valinta, muokkaa tuotteen: 1 nimi, 2 hinta: "))

        if valinta == 1:
            uusi_nimi = input("Tuotteen uusi nimi: ")
            self.db.muokkaa_tuotteen_nimea(uusi_nimi, muokattavan_tuotteem_id)

        if valinta == 2:
            uusi_hinta = float(input("Tuotteen uusi hinta: "))
            self.db.muokkaa_tuotteen_hintaa(uusi_hinta, muokattavan_tuotteem_id)

        else:
            print("Väärä valinta")
            print("------------------------------------------------------")
            return

        print("------------------------------------------------------")

    def poista_tuote(self):
        self.nayta_tuotteet()
        print("")

        poistettavan_tuotteen_id = int(input("Valitse poistettavan tuotteen id: "))
        self.db.poista_tuote(poistettavan_tuotteen_id)
        print("------------------------------------------------------")


    def nayta_tuotteet(self):
        print("")
        self.db.nayta_tuotteet()

    def lisaa_tuote_ostoskoriin(self):
        self.nayta_tuotteet()
        print("")
        tuotteen_id = int(input("Valitse ostoskoriin lisättävän tuotteen id: "))
        self.db.lisaa_tuote_ostoskoriin(tuotteen_id)
        print("------------------------------------------------------")

        print("Ostoskorissa olevat tuotteet:")
        self.db.nayta_ostoskorin_tuotteet()
        print("------------------------------------------------------")

    def nayta_ostoskorin_tuotteet(self):
        print("")
        print("Ostoskorissa olevat tuotteet:")
        self.db.nayta_ostoskorin_tuotteet()
        print("------------------------------------------------------")

    def poista_tuote_ostoskorista(self):
        self.nayta_ostoskorin_tuotteet()
        nimi = input("Anna poistettavan tuotteen tarkka nimi: ")
        self.db.poista_tuote_ostoskorista(nimi)
        print("------------------------------------------------------")






