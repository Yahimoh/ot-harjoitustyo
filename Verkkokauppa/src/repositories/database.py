import sqlite3
from entities.tuote import Tuote

class Database:

    def __init__(self):
        #os.remove("tuotteet.db")

        self.db = sqlite3.connect("tuotteet.db") # pylint: disable=invalid-name
        self.db.isolation_level = None

        self.luo_taulut()

    def luo_taulut(self):
        tuotteet = self.db.execute("SELECT T.nimi FROM Tuote T").fetchall()
        if not tuotteet:
            self.db.execute("CREATE TABLE Tuote (id INTEGER PRIMARY KEY, nimi TEXT, hinta FLOAT)")
            self.db.execute("CREATE TABLE Ostoskori (id INTEGER PRIMARY KEY, tuote_id INTEGER REFERENCES  Tuote)") # pylint: disable=line-too-long


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

    def lisaa_tuote_ostoskoriin(self, tuote_id):
        self.db.execute("INSERT INTO Ostoskori (tuote_id) VALUES (?)", [tuote_id])

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

    def nayta_ostoskorin_tuotteet(self):
        ostoskorin_tuotteet = self.db.execute("SELECT T.nimi From Tuote T, Ostoskori O WHERE T.id = O.tuote_id").fetchall() # pylint: disable=line-too-long

        for tuote in ostoskorin_tuotteet:
            print(tuote[0])

    def poista_tuote_ostoskorista(self, nimi):
        query = self.db.execute("SELECT id FROM Tuote T WHERE T.nimi =? ", [nimi]).fetchone()
        tuote_id = query[0]

        self.db.execute("DELETE FROM Ostoskori WHERE tuote_id =?", [tuote_id])

    def muokkaa_tuotteen_nimea(self, uusi_nimi, tuote_id):
        self.db.execute("UPDATE Tuote SET nimi =? WHERE id =? ", [uusi_nimi, tuote_id])

    def muokkaa_tuotteen_hintaa(self, uusi_hinta, tuote_id):
        self.db.execute("UPDATE Tuote SET hinta =? WHERE id =? ", [uusi_hinta, tuote_id])
