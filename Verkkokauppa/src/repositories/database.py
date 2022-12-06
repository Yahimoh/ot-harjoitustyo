import sqlite3
from entities.tuote import Tuote

class Database:

    def __init__(self):


        self.db = sqlite3.connect("backend.db") # pylint: disable=invalid-name
        self.db.isolation_level = None

        self.luo_taulut()

    def luo_taulut(self):
        try:
            self.db.execute("CREATE TABLE Tuote (id INTEGER PRIMARY KEY, nimi TEXT, hinta FLOAT)")
            self.db.execute("CREATE TABLE Ostoskori (id INTEGER PRIMARY KEY, omistaja_id INTEGER REFERENCES Tunnukset, tuote_id INTEGER REFERENCES  Tuote)")  # pylint: disable=line-too-long
            self.db.execute("CREATE TABLE Tunnukset (id INTEGER PRIMARY KEY, kayttajatunnus TEXT, salasana TEXT)")
        except:
            print("Taulut ovat jo luotu")




    def luo_tuote(self, tuote: Tuote):
        tuotteet = self.tuotteiden_nimet()

        if tuote.nimi in tuotteet:
            print("Tuote on jo olemassa.")
            return

        self.db.execute("INSERT INTO Tuote (nimi, hinta) VALUES (?, ?)", [tuote.nimi, tuote.hinta])
        #tuote_id = self.db.execute("SELECT T.id FROM Tuote T WHERE T.nimi =? ", [tuote.nimi]).fetchone() # pylint: disable=line-too-long
        #self.lisaa_tuote_tuotteisiin(tuote_id)

    def poista_tuote(self, tuote_id):
        self.db.execute("DELETE FROM Tuote WHERE id =?", [tuote_id])

    def lisaa_tuote_ostoskoriin(self, tuote_id, omistaja_id):
        self.db.execute("INSERT INTO Ostoskori (tuote_id, omistaja_id) VALUES (?, ?)", [tuote_id, omistaja_id])

    def nayta_tuotteet(self):
        tuotteet = self.db.execute("SELECT T.id, T.nimi, T.hinta FROM Tuote T").fetchall()

        for tuote in tuotteet:
            print(f"{tuote[0]}: {tuote[1]}, {tuote[2]}€")

    def tuotteiden_nimet(self):
        tuotteet = self.db.execute("SELECT T.nimi FROM Tuote T").fetchall()

        nimet = []

        for tuote in tuotteet:
            nimet.append(tuote[0])

        return nimet

    def nayta_ostoskorin_tuotteet(self, omistaja_id):
        ostoskorin_tuotteet = self.db.execute("SELECT T.nimi From Tuote T, Ostoskori O WHERE T.id = O.tuote_id AND O.omistaja_id =?", [omistaja_id]).fetchall() # pylint: disable=line-too-long

        for tuote in ostoskorin_tuotteet:
            print(tuote[0])

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
            print("Kayttajatunnus on jo olemassa")
            return -1

        self.db.execute("INSERT INTO Tunnukset (kayttajatunnus, salasana) VALUES (?, ?)", [kayttajatunnus, salasana])
        omistaja_id = self.db.execute("SELECT T.id FROM Tunnukset T WHERE T.kayttajatunnus =?", [kayttajatunnus]).fetchone()
        return omistaja_id[0]

    def kirjaudu_sisaan(self, kayttajatunnus, salasana):
        if kayttajatunnus not in self.kaikki_kayttajatunnukset():
            print("Väärä käyttäjätunnus!")
            return -1

        salasana_query = self.db.execute("SELECT T.salasana FROM Tunnukset T WHERE T.kayttajatunnus =?", [kayttajatunnus]).fetchone()
        kayttajatunnuksen_salasana = salasana_query[0]

        if kayttajatunnuksen_salasana == salasana:
            omistaja_id = self.db.execute("SELECT T.id FROM Tunnukset T WHERE T.kayttajatunnus =?", [kayttajatunnus]).fetchone()
            print("Kirjauduttu sisään!")
            return omistaja_id[0]

        print("Väärä salasana!")
        return -1
