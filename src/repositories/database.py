import sqlite3
from entities.tuote import Tuote

class Database:

    def __init__(self):


        self.db = sqlite3.connect("backend.db") # pylint: disable=invalid-name
        self.db.isolation_level = None

    def luo_taulut(self):
        try:
            self.db.execute("CREATE TABLE Tuote (id INTEGER PRIMARY KEY, nimi TEXT, hinta FLOAT)")
            self.db.execute("CREATE TABLE Ostoskori (id INTEGER PRIMARY KEY, omistaja_id INTEGER REFERENCES Tunnukset, tuote_id INTEGER REFERENCES  Tuote)")  # pylint: disable=line-too-long
            self.db.execute("CREATE TABLE Tunnukset (id INTEGER PRIMARY KEY, kayttajatunnus TEXT, salasana TEXT, saldo FLOAT)") # pylint: disable=line-too-long
        except: # pylint: disable=bare-except
            print("")




    def luo_tuote(self, tuote: Tuote):
        tuotteet = self.tuotteiden_nimet()

        if tuote.nimi in tuotteet:
            return -1

        self.db.execute("INSERT INTO Tuote (nimi, hinta) VALUES (?, ?)", [tuote.nimi, tuote.hinta])

        return 1

    def poista_tuote(self, tuote_id):
        self.db.execute("DELETE FROM Tuote WHERE id =?", [tuote_id])

    def lisaa_tuote_ostoskoriin(self, tuote_id, omistaja_id):
        self.db.execute("INSERT INTO Ostoskori (tuote_id, omistaja_id) VALUES (?, ?)", [tuote_id, omistaja_id])

    def nayta_tuotteet(self):
        tuotteet = self.db.execute("SELECT T.id, T.nimi, T.hinta FROM Tuote T").fetchall()
        return tuotteet


    def tuotteiden_nimet(self):
        tuotteet = self.db.execute("SELECT T.nimi FROM Tuote T").fetchall()

        nimet = []

        for tuote in tuotteet:
            nimet.append(tuote[0])

        return nimet

    def nayta_ostoskorin_tuotteet(self, omistaja_id):
        ostoskorin_tuotteet = self.db.execute("SELECT T.nimi From Tuote T, Ostoskori O WHERE T.id = O.tuote_id AND O.omistaja_id =?", [omistaja_id]).fetchall() # pylint: disable=line-too-long
        return ostoskorin_tuotteet

    def poista_tuote_ostoskorista(self, nimi, omistaja_id):
        query = self.db.execute("SELECT id FROM Tuote T WHERE T.nimi =? ", [nimi]).fetchone()
        tuote_id = query[0]

        self.db.execute("DELETE FROM Ostoskori WHERE tuote_id =? AND omistaja_id =? ", [tuote_id, omistaja_id])

    def muokkaa_tuotteen_nimea(self, uusi_nimi, tuote_id):
        self.db.execute("UPDATE Tuote SET nimi =? WHERE id =? ", [uusi_nimi, tuote_id])

    def muokkaa_tuotteen_hintaa(self, uusi_hinta, tuote_id):
        self.db.execute("UPDATE Tuote SET hinta =? WHERE id =? ", [uusi_hinta, tuote_id])

    def kaikki_kayttajatunnukset(self):
        kayttajatunnukset = self.db.execute("SELECT T.kayttajatunnus FROM Tunnukset T").fetchall()

        hiotut_kayttajatunnukset = []

        for tunnus in kayttajatunnukset:
            hiotut_kayttajatunnukset.append(tunnus[0])

        return hiotut_kayttajatunnukset

    def luo_tunnus(self, kayttajatunnus, salasana):
        if kayttajatunnus in self.kaikki_kayttajatunnukset():
            return -1

        self.db.execute("INSERT INTO Tunnukset (kayttajatunnus, salasana, saldo) VALUES (?, ?, 0.0)", [kayttajatunnus, salasana])
        omistaja_id = self.db.execute("SELECT T.id FROM Tunnukset T WHERE T.kayttajatunnus =?", [kayttajatunnus]).fetchone()
        return omistaja_id[0]

    def kirjaudu_sisaan(self, kayttajatunnus, salasana):
        if kayttajatunnus not in self.kaikki_kayttajatunnukset():
            return -1

        salasana_query = self.db.execute("SELECT T.salasana FROM Tunnukset T WHERE T.kayttajatunnus =?", [kayttajatunnus]).fetchone()
        kayttajatunnuksen_salasana = salasana_query[0]

        if kayttajatunnuksen_salasana == salasana:
            omistaja_id = self.db.execute("SELECT T.id FROM Tunnukset T WHERE T.kayttajatunnus =?", [kayttajatunnus]).fetchone()
            return omistaja_id[0]

        return -2

    def talleta_rahaa_tilille(self, kayttaja_id, saldo):
        tilin_saldo = self.db.execute("SELECT T.saldo FROM Tunnukset T WHERE T.id =? ", [kayttaja_id]).fetchone()
        nykyinen_saldo = tilin_saldo[0]

        paivitettava_saldo = saldo + nykyinen_saldo
        self.db.execute("UPDATE Tunnukset SET saldo =? WHERE id =?", [paivitettava_saldo, kayttaja_id])

        uusi_saldo = self.db.execute("SELECT saldo FROM Tunnukset WHERE id =? ", [kayttaja_id]).fetchone()
        nykyinen_uusi_saldo = uusi_saldo[0]

        return nykyinen_uusi_saldo

    def hanki_ostoskorin_summa(self, kayttaja_id):
        alustava_summa = self.db.execute("SELECT SUM(T.hinta) FROM Tuote T, Ostoskori O WHERE O.tuote_id = T.id AND O.omistaja_id =? ", [kayttaja_id]).fetchone() # pylint: disable=line-too-long
        ostoskorin_summa = alustava_summa[0]

        if ostoskorin_summa is None:
            ostoskorin_summa = 0

        return ostoskorin_summa

    def tyhjenna_ostoskori(self, kayttaja_id):
        self.db.execute("DELETE FROM Ostoskori WHERE omistaja_id =? ", [kayttaja_id])
