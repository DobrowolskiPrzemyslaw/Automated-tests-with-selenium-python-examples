class Pies:
    gatunek = 'pies domowy'

    def __init__(self, rasa, imie, wiek):
        print("Wewnatrz metody init")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        print("hau hau")

    def zaprezentuj_psa(self):
        print("Rasa to " + self.rasa)
        print("Imie to " + self.imie)
        print("Wiek to " + str(self.wiek))

reksio = Pies('kundelek', 'Reksio', 2)
reksio.szczekaj()
reksio.zaprezentuj_psa()