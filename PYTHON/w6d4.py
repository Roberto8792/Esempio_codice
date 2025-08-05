#ho importato la libreria math per calcolare il perimetro del cerchio utilizzando la costante pi greco
import math
# imposto ok a falso
ok=False
#quando ok è falso, chiedo all'utente di inserire un valore numerico
while not ok:
    #converto l'input dell'utente in un float e lo assegno alla variabile valore
    try:
        valore : float = float(input("Inserisci un valore: "))
        ok = True
        #controllo se il valore è numerico altrimenti stampo un messaggio di errore
    except ValueError:
        print("Per favore, inserisci un valore numerico.")

#chiedo all'utente di scegliere tra le opzioni disponibili per calcolare il perimetro
print ("Dimmi che vuoi tra")
print ("\t1 Perimetro del quadrato ")
print ("\t2 Perimetro del cerchio")
print ("\t3 Perimetro del rettangolo")

# imposto ok a falso per verificare la scelta dell'utente
ok=False
#quando ok è falso, chiedo all'utente di inserire un'opzione numerica
while not ok:
    #converto l'input dell'utente in un float e lo assegno alla variabile opzione
    try:
        opzione : float = float(input("Scegli: "))
        # conferma se l'opzione scelta è valida
        if opzione in [1, 2, 3]:
            ok = True
            # altrimenti stampo un messaggio di errore
        else:
            print("La tua scelta ((opzione)) non va bene!")
            # chiedo di nuovo all'utente di inserire un'opzione numerica  
    except ValueError:
        print("Per favore, inserisci un opzione numerico.")
# inizializzo la variabile perimetro a 0.0
perimetro:float = 0.0

#inizio a calcolare il perimetro del quadrato
if opzione == 1:
    perimetro = 4 * valore

#calcolo l'area del cerchio
elif opzione == 2:
    import math
    perimetro = 2 * math.pi * valore

#calcolo l'area del rettangolo
elif opzione == 3:
     perimetro = 3 * valore
#altrimenti, se l'opzione non è valida, stampo un messaggio di errore
else:
    raise Exception("Opzione non valida")
# stampo il perimetro calcolato con due decimali
print(f"{perimetro:.2f} è il perimetro scelto")




