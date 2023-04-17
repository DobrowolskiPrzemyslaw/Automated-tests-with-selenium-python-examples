dziennik = {1:"Kowaliski",2:"Lewandowska"}

print(dziennik.get(0))
print(dziennik.get(1))

dziennik[3]="Mucha"
print(dziennik)

for key in dziennik.keys():
    print(key)

for value in dziennik.values():
    print(value)

# aktualizacja
dziennik[2]="Kalinowski"
print(dziennik)