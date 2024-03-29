from repositories.database import Database

class Merchant:
    """Luokka, jonka avulla käsitellään verkkokaupan toiminnallisuudet

    Attributes:
        db: Verkkokaupan tietokanta
    """

    def __init__(self):
        """ Verkkokaupan konstruktori, joka luo verkkokaupan
        """
        self.db = Database() # pylint: disable=invalid-name

    def asiakkaan_sisaankirjautuminen(self, kayttajatunnus, salasana):
        """Metodi, joka kirjaa asiakkaan sisään ja palauttaa asiakkaan id

        Returns:
            -1 tai -2 jos asiakasta ei saada kirjattua sisään muuten palauttaa asiakkaan id-numeron
        """

        omistaja_id = self.db.kirjaudu_sisaan(kayttajatunnus, salasana)
        return omistaja_id

    def asiakkaan_rekisteroityminen(self, kayttajatunnus, salasana):
        """Metodi, joka rekisteröi ja kirjaa asiakasta sisään ja palauttaa asiakkaan id

        Returns:
            -1 jos asiakasta ei saada rekisteröityä sisään muuten palauttaa uuden asiakkaan id-numeron # pylint: disable=line-too-long
        """

        omistaja_id = self.db.luo_tunnus(kayttajatunnus, salasana)
        return omistaja_id

    def lisaa_tuote(self, tuote):
        """Metodi, joka auttaa kauppiasta lisäämään tuotteen tietokantaan
        """

        palautus = self.db.luo_tuote(tuote)


        return palautus

    def muokkaa_tuotetta(self, onko_nimi, muokattava, tuotteen_id):
        """Metodi, joka auttaa kauppiasta muokkaamaan tuotetta tietokannassa
        """

        if onko_nimi is True:
            self.db.muokkaa_tuotteen_nimea(muokattava, tuotteen_id)
        else:
            self.db.muokkaa_tuotteen_hintaa(muokattava, tuotteen_id)



    def poista_tuote(self, poistettavan_tuotteen_id):
        """Metodi, joka auttaa kauppiasta poistamaan tuotetta tietokannassa
        """
        self.db.poista_tuote(poistettavan_tuotteen_id)



    def nayta_tuotteet(self):
        """Metodi, joka näyttää kaikki kauppiaan lisäämät tuotteet tietokannassa
        """

        print("")
        tuotteet = self.db.nayta_tuotteet()

        return tuotteet


    def lisaa_tuote_ostoskoriin(self, omistaja_id, tuotteen_id):

        self.db.lisaa_tuote_ostoskoriin(tuotteen_id, omistaja_id)
        print("------------------------------------------------------")

    def nayta_ostoskorin_tuotteet(self, omistaja_id):
        ostoskorin_tuotteet = self.db.nayta_ostoskorin_tuotteet(omistaja_id)

        return ostoskorin_tuotteet

    def poista_tuote_ostoskorista(self, omistaja_id):
        self.nayta_ostoskorin_tuotteet(omistaja_id)
        nimi = input("Anna poistettavan tuotteen tarkka nimi: ")
        self.db.poista_tuote_ostoskorista(nimi, omistaja_id)
        print("------------------------------------------------------")

    def lisaa_saldoa_tilille(self, omistaja_id):
        saldo = float(input("Anna talletettava saldo: "))

        if saldo > 0:
            nykyinen_saldo = self.db.talleta_rahaa_tilille(omistaja_id, saldo)
            print(f"Talletus onnistui! Nykyinen saldo: {nykyinen_saldo}€")

    def ostoskorin_summa(self, omistaja_id):
        summa = self.db.hanki_ostoskorin_summa(omistaja_id)
        return summa


    def ostoskorin_maksu(self, omistaja_id):
        print("")
        summa = self.ostoskorin_summa(omistaja_id)
        print(f"Ostoskorin summa: {summa}")

        print("Maksetaanko ostokset?")
        print("1: Maksa ostokset")
        print("2: Jatka kaupan käyttöä")
        valinta = int(input("Valinta 1/2: "))

        if valinta == 1:
            nykyinen_saldo = self.db.talleta_rahaa_tilille(omistaja_id, 0)
            if nykyinen_saldo - summa >= 0:
                miinustettava_saldo = 0
                miinustettava_saldo = miinustettava_saldo - summa
                uusi_saldo = self.db.talleta_rahaa_tilille(omistaja_id, miinustettava_saldo)
                self.db.tyhjenna_ostoskori(omistaja_id)

                print(f"Ostoskorin maksu onnistui! Nykyinen saldo: {uusi_saldo}")
            else:
                print("Saldolla ei tarpeeksi katetta! Yritä uudelleen lisäämällä tilille saldoa tai poistamalla tuotteita ostoskorista") # pylint: disable=line-too-long
        elif valinta == 2:
            print("Jatketaan kaupan käyttöä")
        else:
            print("Väärä valinta.")
