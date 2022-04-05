
class Verkkokauppa:
    def __init__(self):

        kayttaja = input("Terve! Oletko kauppias vai asiakas? ")

        if kayttaja == "asiakas":
            print("Asiakkaan näkymä")
        else:
            print("Kauppiaan näkymä")

verkkokauppa = Verkkokauppa()
