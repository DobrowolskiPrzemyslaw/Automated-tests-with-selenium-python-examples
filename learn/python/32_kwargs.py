
def dziennik(klasa,**kwargs):
    print('Klasa ' + klasa)
    for nazwiska in kwargs.keys():
        print(nazwiska)
    print(kwargs.get('Kowalski'))

dziennik('3c', Kowalski='1',Nowak='2',Wisniewski='3')