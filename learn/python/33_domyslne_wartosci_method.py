def dziennik(klasa='1C',**kwargs):
    print('Klasa ' + klasa)
    for nazwiska in kwargs.keys():
        print(nazwiska)
    print(kwargs.get('Kowalski'))

dziennik(Kowalski='1',Nowak='2',Wisniewski='3')
dziennik('3C', Kowalski='1',Nowak='2',Wisniewski='3')