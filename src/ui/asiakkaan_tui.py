from services.merchant import Merchant

class AsiakkaanTUI:
    def __init__(self):
        self._merchant = Merchant()
        self._asiakkaan_id = 0

    def asiakkaan_nakyma_tui(self):
        self.asiakkaan_authentikointi()
        self.asiakkaan_toiminta_tui(self._asiakkaan_id)


    def asiakkaan_authentikointi(self):
        while True:
            print("")
            print("1: Kirjaudu sisään")
            print("2: Rekisteröidy")

            valinta = int(input("Valinta 1/2: "))

            if valinta not in (1, 2):
                print("Väärä valinta!")
                print("Yritä uudestaan!")
                continue

            if valinta == 1:
                self.asiakkaan_sisaankirjautumisen_tui()
                break

            self.asiakkaan_rekisteroityminen_tui()
            break


    def asiakkaan_sisaankirjautumisen_tui(self):
        while True:
            print("")
            print("Kirjaudu sisään: ")
            kayttajatunnus = input("Käyttäjätunnus: ")
            salasana = input("Salasana: ")

            omistaja_id = self._merchant.asiakkaan_sisaankirjautuminen(kayttajatunnus, salasana)

            if omistaja_id == -1:
                print("")
                print("Väärä käyttäjätunnus!")
                print("Yritä uudestaan.")
                continue
            elif omistaja_id == -2:
                print("")
                print("Väärä salasana!")
                print("Yritä uudestaan.")
                continue

            print("Kirjauduttu sisään! ")
            self._asiakkaan_id = omistaja_id
            break

    def asiakkaan_rekisteroityminen_tui(self):
        while True:
            print("")
            print("Rekisteröidy asiakkaaksi!")
            kayttajatunnus = input("Käyttäjätunnus: ")
            salasana = input("Salasana: ")

            omistaja_id = self._merchant.asiakkaan_rekisteroityminen(kayttajatunnus, salasana)

            if omistaja_id == -1:
                print("Käyttäjätunnus olemassa, yritä toista tunnusta!")
                continue

            print("Käyttäjätunnus luotu!")
            self._asiakkaan_id = omistaja_id
            break

    def asiakkaan_toiminnan_tulostus(self):
        print("")
        print("Valitse toiminnoista:")
        print("1: Katso saatavilla olevat tuotteet")
        print("2: Katso ostoskorin tuotteet")
        print("3: Lisää tuote ostoskoriin")
        print("4: Poista tuote ostoskorilta")
        print("5: Lisää saldoa tilille")
        print("6: Maksa ostokset")
        print("0: Lopeta käyttö")

    def asiakkaan_toiminta_tui(self, kayttaja_id):
        while True:
            self.asiakkaan_toiminnan_tulostus()
            valinta = int(input("Valinta 1/2/3/4/5/6/0: "))

            if valinta == 1:
                self._merchant.nayta_tuotteet()
            if valinta == 2:
                self._merchant.nayta_ostoskorin_tuotteet(kayttaja_id)
            if valinta == 3:
                self._merchant.lisaa_tuote_ostoskoriin(kayttaja_id)
            if valinta == 4:
                self._merchant.poista_tuote_ostoskorista(kayttaja_id)
            if valinta == 5:
                self._merchant.lisaa_saldoa_tilille(kayttaja_id)
            if valinta == 6:
                self._merchant.ostoskorin_maksu(kayttaja_id)
            if valinta == 0:
                print("Lopetetaan")
                break