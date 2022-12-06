from services.merchant import Merchant


verkkokauppa = Merchant()

while True:
    print("----------Tervetuloa verkkokauppaan!----------")
    print("")
    print("Oletko asiakas vai kauppias?")
    print("1: Asiakas")
    print("2: Kauppias")
    valinta = int(input("Valinta 1/2: "))

    if valinta not in (1, 2):
        continue

    if valinta == 1:
        verkkokauppa.start("asiakas")
        break

    if valinta == 2:
        verkkokauppa.start("kauppias")
        break
