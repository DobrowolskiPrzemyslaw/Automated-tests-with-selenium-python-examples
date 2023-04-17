file = open("nowy.txt", "w")
file.write("To jest jakis tekst")
file.close()

# file = open("nowy.txt","w")          #kasuje poprzednia wartosc w pliku i zapisuje nowa
# file.write("To jest jakis tekst 2")
# file.close()

file = open("nowy.txt", "a")            # APPEND - dopisanie
file.write("To jest jakis tekst 2")
file.close()