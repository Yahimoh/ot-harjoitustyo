from services.merchant import Merchant
#from ui.ui import UI
#import tkinter as tk


verkkokauppa = Merchant()

#paanakyma = tk.Tk()
#paanakyma.geometry("450x200")
#nakyma = UI()
#nakyma.start(paanakyma)

#paanakyma.mainloop()

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
