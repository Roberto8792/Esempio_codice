#ho importato la libreria math per calcolare il perimetro del cerchio utilizzando la costante pi greco
import math

#imposto la funzione scelta_utente che non accetta parametri e restituisce un intero. la funziona viene inserita col comando def
#La funzione scelta_utente accetta una lista di scelte possibili come parametro
def scelta_utente(scelte_possibili:list[int]) -> int:
    
    #chiedo all'utente di scegliere tra le opzioni disponibili per calcolare il perimetro e l'area
    print ("Dimmi che vuoi tra")
    if 1 in scelte_possibili:
        print ("\t1 Perimetro e area del quadrato ")

    if 2 in scelte_possibili:
        print ("\t2 Perimetro e area del cerchio")

    if 3 in scelte_possibili:
        print ("\t3 Perimetro e area del rettangolo")

    #imposto ok a falso per verificare la scelta dell'utente
    ok=False
    #quando ok è falso, chiedo all'utente di inserire un'opzione numerica
    while not ok:
    #converto l'input dell'utente in un int e lo assegno alla variabile opzione
        try:
            opzione : int = int(input("Scegli: "))
            # conferma se l'opzione scelta è valida
            if opzione in scelte_possibili:
                ok = True
            # altrimenti stampo un messaggio di errore
            else:
                print("La tua scelta ((opzione)) non va bene!")
            # chiedo di nuovo all'utente di inserire un'opzione numerica  
        except ValueError:
            print("Per favore, inserisci un opzione numerico.")
    #ritorno a opzione scelta dall'utente
    return opzione
    
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

# inizializzo le variabili perimetro e area a 0.0
    perimetro:float = 0.0
    area:float = 0.0


# imposto una lista di scelte possibili per l'utente
scelte_possibili = [1, 2, 3]
# con while len(scelte_possibili) > 0, continuo a chiedere all'utente di scegliere un'opzione finché ci sono opzioni disponibili
# e successivamente rimuovo l'opzione scelta dall'utente dalla lista delle scelte possibili
while len(scelte_possibili) > 0:
    opzione = scelta_utente(scelte_possibili)
    scelte_possibili.remove(opzione)

    #inizio a calcolare il perimetro e l'area del quadrato
    if opzione == 1:
        perimetro = 4 * valore
        area = valore * valore

    #calcolo il perimetro e l'area del cerchio
    elif opzione == 2:
        perimetro = 2 * math.pi * valore
        area = valore * valore * math.pi

    #calcolo il perimetro e l'area del rettangolo
    elif opzione == 3:
        perimetro = 3 * valore
        area = valore * valore / 2
    #altrimenti, se l'opzione non è valida, stampo un messaggio di errore
    else:
        raise Exception("Opzione non valida")
    
    # assegno il valore del perimetro e dell'area alla variabile valore
    valore = area


    # stampo il perimetro calcolato con due decimali
    print(f"{perimetro:.2f} è il perimetro ")
    print(f"{area:.2f} è l'area ")





