
class Tuote:
    """Luokka, joka on perusta tuotteen luomiselle

    Attributes:
            nimi: Luotavalle tuotteelle nimi
            hinta: Luotavalle tuotteelle hinta
    """

    def __init__(self, nimi: str, hinta: float):
        """Tuotteen konstruktori joka luo uuden tuotteen

        Attributes:
                nimi: Luotavalle tuotteelle nimi
                hinta: Luotavalle tuotteelle hinta
        """

        self.nimi = nimi
        self.hinta = hinta

    def get_nimi(self):
        """Metodi, joka palauttaa tuotteen nimen
        """

        return self.nimi

    def get_hinta(self):
        """Metodi, joka palauttaa tuotteen hinnan
        """

        return self.hinta

    def update_nimi(self, uusi_nimi: str):
        """Metodi, joka päivittää tuotteen nimen
        Attributes:
                uusi_nimi: Tuotteen uusi nimi
        """

        self.nimi = uusi_nimi

    def update_hinta(self, uusi_hinta: int):
        """Metodi, joka päivittää tuotteen hinnan
        Attributes:
                uusi_hinta: Tuotteen uusi hinta
        """

        self.hinta = uusi_hinta

    def __str__(self):
        return self.nimi + ": " + str(self.hinta) + "€"
