'''

'''
numero_partecipanti = int(input("quanti partecipanti al convegno ci sono? "))
lista_partecipanti = []
for n in range (numero_partecipanti):
    partecipante = (input("inserisci il nome del partecipante: "))
    lista_partecipanti.append(partecipante)
    partecipanti_inseriti = len(lista_partecipanti)
    print ("numero partecipanti inseriti: ",partecipanti_inseriti)

risposta= input("vuoi inviare la lettera al primo partecipante? ")
if risposta == "si":
    while partecipanti_inseriti > 0:
        print ("i partecipanti inseriti sono ", lista_partecipanti)
        print("bisogna inviare la lettera a: ",lista_partecipanti[0])
        lista_partecipanti.pop(0)
        partecipanti_inseriti = len(lista_partecipanti)
        print ("lettera inviata correttamente")
        print ("i partecipanti rimasti sono: ", lista_partecipanti)
        risposta = input("vuoi continuare? ")
        if risposta== "si":
            print("ok")
            #anche continue funziona
        else:
            print("ok")
            break
        if partecipanti_inseriti == 0:
            print ("i partecipanti sono terminati, non posso inviare la lettera")
            break
        else:
            print(" ")
            #anche continue funziona
else: 
    print("ok, la lettera non verra inviata")

#si può anche eliminare le linee 25-30 e inserire >1 nel ciclo while, 
# il risultato sarà che al posto di informare l'utente del fatto che i partecipanti sono finiti ci sarà scritto "ok"