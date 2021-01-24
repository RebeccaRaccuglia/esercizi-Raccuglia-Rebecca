nazioni_lista = ["italia", "francia", "germania", "albania", "brasile", "cina", "croazia", "estonia", "georgia", "russia"]
capitali_lista = ["roma", "parigi", "berlino", "tirana", "brasilia", "pechino", "zagabria", "tallinn", "tiblisi", "mosca" ] 
nazione = input("Inserisci il nome della nazione del cui vuoi conoscere la capitale: ")
if nazione in nazioni_lista:
    indice = nazioni_lista.index(nazione) 
    print("La capitale di questa nazione e' ", capitali_lista[indice])
else:
    print("La nazione non e' presente nella lista fornita")