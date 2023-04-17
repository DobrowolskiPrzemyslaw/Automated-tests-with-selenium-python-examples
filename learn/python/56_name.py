def pogoda_krakow():
    return "Slonecznie"

def pogoda_szczecin():
    return "Pochmurno"

def pogoda_wroclaw():
    return "Upal"

# Wykona się tylko dla metod odpalanych w tym pliku
# jeśli zaimportujemy te metody to wywolaja sie tylko te z kolejnego pliku
if __name__ == '__main__':
    print(pogoda_krakow())
    print(pogoda_szczecin())
    print(pogoda_wroclaw())