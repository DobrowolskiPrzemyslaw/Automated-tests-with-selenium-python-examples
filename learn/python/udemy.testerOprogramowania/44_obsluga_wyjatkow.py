while True:
    try:
        print("Podaj pierwsza liczbe: ")
        prierwsza_liczba = int(input())
        print("Podaj drugą liczbe: ")
        druga_liczba = int(input())
        print(prierwsza_liczba + druga_liczba)
        break
    except ValueError:
        print("Podałeś błędną wartość")
        print("Spróbuj jeszcze raz")
        continue