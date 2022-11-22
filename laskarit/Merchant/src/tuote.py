
class Tuote:
    def __init__(self, nimi : str, hinta : float):
        self.nimi = nimi
        self.hinta = hinta

    def get_nimi(self):
        return self.nimi

    def get_hinta(self):
        return self.hinta

    def update_nimi(self, uusi_nimi: str):
        self.nimi = uusi_nimi

    def update_hinta(self, uusi_hinta : int):
        self.hinta = uusi_hinta

    def __str__(self):
        return self.nimi + ": " + str(self.hinta) + "€"