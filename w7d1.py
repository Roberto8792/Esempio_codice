#Scrivi una funzione che data in ingresso una lista A contenente n parole
#restituisce in output una lista di B di interi rappresenta che rappresentano la lunghezza delle parole contenute in A

#imposto la funzione metodo_uno che restituisce una lista di interi
#che rappresentano la lunghezza delle parole contenute in A
def metodo_uno(a: list[str]) -> list[int]:
    #creo una lista vuota b
    b= []
    #per ogni parola in a calcolo la lunghezza e la aggiungo a b
    for parola in a:
        #calcolo la lunghezza della parola
        lunghezza = len(parola)
        #aggiungo la lunghezza alla lista b
        b.append(lunghezza)
    #restituisco la lista b
    return b


#imposto la funzione metodo_due che restituisce una lista di interi
def metodo_due(a: list[str]) -> list[int]:
    #utilizzo una list comprehension per calcolare la lunghezza delle parole in a
    return [len(x) for x in a]    
#Creo una lista di parole
a = ["Ciao" , "sono", "Roberto" , "di", "Epicode"]
#assegno a b la lunghezza delle parole in a
b = metodo_due(a)

# le principali differenze tra le due funzioni sono:
# con il metodo_uno uso un ciclo for tradizionale con una lista temporanea (b) e l'uso esplicito di append()
# con il metodo_due uso una list comprehension che è più concisa e diretta.
# Entrambi i metodi producono la stessa lista di lunghezze, ma il secondo risulta piu leggibile e conciso.


#con assert verifico che i risultati delle due funzioni siano uguali
assert metodo_due(a) == metodo_uno(a) 
# Stampo i risultati delle due funzioni
print(a)
print(b)
