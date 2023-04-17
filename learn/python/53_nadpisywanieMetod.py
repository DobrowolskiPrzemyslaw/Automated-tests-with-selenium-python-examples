class Zwierze:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def daj_glos(self):
        print("Zwierzę mówi: ")

class Pies(Zwierze):
    def __init__(self, imie, wiek, rasa):
        super().__init__(imie, wiek)
        self.rasa = rasa

    def daj_glos(self):
        super().daj_glos()
        print("Hau hau!")

zwierzak = Zwierze("bezimienny", 5)
zwierzak.daj_glos()

azor = Pies("Azor", 3, "kundel")
azor.daj_glos()