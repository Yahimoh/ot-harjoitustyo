from merchant import Merchant

verkkokauppa = Merchant()

while True:
    print("Tervetuloa verkkokauppaan!")
    print("")
    print("Oletko asiakas vai kauppias?")
    print("1: Asiakas")
    print("2: Kauppias")
    valinta = int(input("Valinta 1/2: "))

    if valinta != 1 and valinta != 2:
        continue

    if valinta == 1:
        verkkokauppa.asiakkaan_toiminta()
        break

    if valinta == 2:
        verkkokauppa.kauppiaan_toiminta()
        break