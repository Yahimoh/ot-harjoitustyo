class Merchant:

    def start(self, kayttaja : str):
        if kayttaja == "asiakas":
            self.asiakkaan_toiminta()
        else:
            self.kauppiaan_toiminta()



    def asiakkaan_toiminta(self):
        print("")
        print("Tervetuloa verkkokaupan asiakkaaksi!")
        print("")

        while True:
            print("Valitse toiminnoista:")
            print("1: Lisää tuote ostoskoriin")
            print("2: Poista tuote ostoskorilta")
            valinta = int(input("Valinta 1/2: "))

            if valinta == 1:
                print("Toiminta tuotteen lisäykselle ostoskoriin")
                break
            elif valinta == 2:
                print("Toiminta tuotteen poistamiselle ostoskorilta")
                break
            else:
                print("Väärä valinta!")
                print("")
                continue

    def kauppiaan_toiminta(self):
        print("")
        print("Kauppiaan näkymä: ")
        print("")

        while True:
            print("Valitse toiminnoista:")
            print("1: Lisää tuote")
            print("2: Muokkaa tuotetta")
            print("3: Poista tuote")
            valinta = int(input("Valinta 1/2/3: "))

            if valinta == 1:
                print("Toiminta tuotteen lisäykselle")
                break
            elif valinta == 2:
                print("Toiminta tuotteen muokkaukselle")
                break
            elif valinta == 3:
                print("Toiminta tuotteen poistamiselle")
                break
            else:
                print("Väärä valinta!")
                print("")
                continue
