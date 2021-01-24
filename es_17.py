nazioni_lista = ["italia", "francia", "germania", "albania", "brasile", "cina", "croazia", "estonia", "georgia"]
capitali_lista = ["roma", "parigi", "berlino", "tirana", "brasilia", "pechino", "zagabria", "tallinn", "tiblisi" ] 

dictionary = {}


for i in range(len(nazioni_lista)):
    dictionary[capitali_lista[i]] = nazioni_lista[i]


capitale = input("inserisci capitale: ")
exist = False

for e in dictionary:
    if capitale == e:
        exist = True

if exist:
    print("la nazione e': ", dictionary[capitale])

else:
    print("errore")