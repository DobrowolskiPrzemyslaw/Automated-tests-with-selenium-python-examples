imie = 'Bartek'
nazwisko = 'Jurczyk'
def przedstaw_sie():
    nazwisko = 'Kowalski'
    print(imie)
    print(nazwisko)

print(imie)
print(nazwisko)

przedstaw_sie()
print(nazwisko)   # wywolanie metody nie nadpisało wartosci zmiennej globalnej