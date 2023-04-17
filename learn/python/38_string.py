imie = 'Bartek'
nazwisko = 'Kowalski'
adres = """
        Kwiatowa 28c/1
        Warszawa 00-001 
        """
print(nazwisko)

print('Czytam ksiązke "Wladca pierscieni"')
print("\\Czytam \t ksiazke \n \"Wladca Pierscieni\"")

print("male litery".upper())
print("male litery".lower())
print(imie.lower())
print(nazwisko.lower())

for char in "Bartek":
    print(char)

print(imie[0])
print(imie[0:4])
print(imie.index("a"))
print("Ala" not in "Ala ma kota")

print(" ".join(["Ala", "ma", "kota"]))
print("Ala,ma,kota,i,pasa".split(","))
print(imie.startswith("Ba"))
print(imie.endswith("tek"))