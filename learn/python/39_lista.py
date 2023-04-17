imiona = ['Bartek',"Tomek","Andrzej",1,2,34,5,53]
print(imiona[0])
print(imiona[1])
print(imiona[2])
print(imiona[3])
print(imiona[4])
print(imiona.index("Bartek"))

imiona.append("Wojtek")
imiona.insert(0,"Wojtek")
print(imiona)
print(len(imiona))
imiona.remove("Bartek")
print(imiona)
del imiona[0]
print(imiona)

pierwsza_lista = ["lampa","koc","krzeslo"]
druga_lista = ["auto","mlotek",1,2]
print(pierwsza_lista*3)
print(pierwsza_lista+druga_lista)