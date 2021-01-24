nazioni_lista = ["italia", "francia", "germania", "albania", "brasile", "cina", "croazia", "estonia", "georgia", "russia"]
capitali_lista = ["roma", "parigi", "berlino", "tirana", "brasilia", "pechino", "zagabria", "tallinn", "tiblisi", "mosca" ] 

dictionary = {}


for i in range(len(nazioni_lista)):
    dictionary[nazioni_lista[i]] = capitali_lista[i]


nazione = input("inserisci la nazione di cui vuoi conoscere la capitale: ")
exist = False

for e in dictionary:
    if nazione == e:
        exist = True

if exist:
    print("la capitale è: ", dictionary[nazione])

else:
    print("errore")