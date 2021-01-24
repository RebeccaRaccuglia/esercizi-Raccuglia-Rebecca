numero_nazioni = int(input("Quante nazioni vuoi inserire? "))
capitali_lista = []
nazioni_lista = []
contatore = 0
while True:
    nazione = input("Inserisci il nome della nazione: ")
    nazioni_lista.append(nazione)
    capitale = input("Inserisci il nome della capitale: ")
    capitali_lista.append(capitale)
    contatore += 1
    if contatore == numero_nazioni:
        break
nazione = input("Inserisci il nome della nazione del cui vuoi conoscere la capitale: ")
if nazione in nazioni_lista:
    indice = nazioni_lista.index(nazione) 
    print("La capitale di questa nazione e'", capitali_lista[indice])
else:
    print("La nazione non e' presente nella lista fornita")