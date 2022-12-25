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

            try:
                valinta = int(input("Valinta 1/2: "))
            except ValueError:
                print("Valinta ei ollut numero, yritä uudestaan")
                continue

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
            try:
                kayttajatunnus = input("Käyttäjätunnus: ")
            except:
                print("")
                print("Vääränlainen syöte, yritä uudestaan")
                continue

            try:
                salasana = input("Salasana: ")
            except:
                print("")
                print("Vääränlainen syöte, yritä uudestaan")
                continue


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

            try:
                valinta = int(input("Valinta 1/2/3/4/5/6/0: "))
            except:
                print("")
                print("Vääränlainen valinta")
                print("Yritä uudestaan")
                continue

            if valinta == 1:
                self.nayta_tuotteet_tui()
            if valinta == 2:
                self.nayta_ostoskorin_tuotteet_tui(kayttaja_id)
            if valinta == 3:
                self.lisaa_tuote_ostoskoriin_tui(kayttaja_id)
            if valinta == 4:
                self._merchant.poista_tuote_ostoskorista(kayttaja_id)
            if valinta == 5:
                self._merchant.lisaa_saldoa_tilille(kayttaja_id)
            if valinta == 6:
                self._merchant.ostoskorin_maksu(kayttaja_id)
            if valinta == 0:
                print("Lopetetaan")
                break

    def nayta_tuotteet_tui(self):
        tuotteet = self._merchant.nayta_tuotteet()

        for tuote in tuotteet:
            print(f"{tuote[0]}: {tuote[1]}, {tuote[2]}€")


    def nayta_ostoskorin_tuotteet_tui(self, kayttaja_id):
        tuotteet = self._merchant.nayta_ostoskorin_tuotteet(kayttaja_id)

        print("")
        print("Ostoskorissa olevat tuotteet:")
        for tuote in tuotteet:
            print(tuote[0])

        print("------------------------------------------------------")


    def lisaa_tuote_ostoskoriin_tui(self, kayttaja_id):
        self.nayta_tuotteet_tui()

        tuotteen_id = int(input("Valitse ostoskoriin lisättävän tuotteen id: "))

        self._merchant.lisaa_tuote_ostoskoriin(kayttaja_id, tuotteen_id)

        print("Ostoskorissa olevat tuotteet:")
        self.nayta_ostoskorin_tuotteet_tui(kayttaja_id)
