
class Verkkokauppa:

    def __init__(self, kayttaja: str):
        self.nakyma = ""

        if kayttaja == "asiakas":
            self.nakyma = "Asiakkaan näkymä"
        else:
            self.nakyma = "Kauppiaan näkymä"

    def __str__(self):
        return self.nakyma


verkkokauppa = Verkkokauppa("asiakas")
print(verkkokauppa)
