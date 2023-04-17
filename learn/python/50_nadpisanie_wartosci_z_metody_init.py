class Pies:
    gatunek = 'pies domowy'

    def __init__(self, rasa, imie, wiek):
        print("Wewnatrz metody init")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek


reksio = Pies('kundelek', 'Reksio', 2)
print(reksio.rasa)
print(reksio.imie)
print(reksio.wiek)
print(reksio.gatunek)
print(Pies.gatunek)

# Napisanie wartosci dla stworzonego wczesniej obiektu
reksio.wiek = 3
print(reksio.wiek)
reksio.gatunek = "ptak"
print(reksio.gatunek)