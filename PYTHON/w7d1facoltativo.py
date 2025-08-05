# Scrivi una funzione generatrice di password. 
# La funzione deve generare una stringa alfanumerica di 8 caratteri qualora 
# l'utente voglia una password semplice, o di 20 caratteri ascii qualora 
# desideri una password più complicata.

#importo le librerie necessarie. 
#string per gestire le stringhe e random per generare numeri casuali

import string
import random

# Definisco i set di caratteri da utilizzare per la generazione delle password
# ALFANUMERICI contiene lettere minuscole, maiuscole e numeri
# TUTTI_ASCII contiene anche i caratteri speciali
ALFANUMERICI = string.ascii_lowercase + string.ascii_uppercase + string.digits
TUTTI_ASCII = ALFANUMERICI + string.punctuation

# Definisco la funzione che genera la password
# La funzione accetta due parametri: la lunghezza della password e il set di caratteri da utilizzare
def generate_password(lenght: int, charset: str) -> str:
    # Creo una lista vuota per la password
    password = []
    # Utilizzo un ciclo for per aggiungere caratteri casuali alla password
     # per il numero di volte specificato da 'lenght'
    for i in range(0,lenght):
        # Scegli un carattere casuale dal set di caratteri
        letter = random.choice(charset)
        # Aggiungo il carattere scelto alla lista della password
        password.append(letter)
    # Unisco i caratteri della lista in una stringa e la restituisco
    return ''.join(password)

# Chiedo all'utente se vuole una password semplice o complicata 
# in base alla sua scelta genero la password con la lunghezza e il set di caratteri appropriati
scelta = input("Vuoi una password semplice (8 caratteri) o complicata (20 caratteri)? (s/c): ")

# apro un ciclo if per verificare la scelta dell'utente
if scelta.lower() ==  "c":
    # Se l'utente sceglie una password complicata, genero una password di 20 caratteri usando tutti i caratteri ASCII
    password = generate_password(20, TUTTI_ASCII)

# con un elif verifico se l'utente vuole una password semplice
elif scelta.lower() == "s":
    # Se l'utente sceglie una password semplice, genero una password di 8 caratteri usando solo caratteri alfanumerici
    password = generate_password(8, ALFANUMERICI)

# altrimenti con else genero una password semplice di 1 solo carattere alfanumerico
# Questo caso gestisce eventuali input non validi o non specificati in quanto una password di 1 carattere non è una scelta comune
else:
    password = generate_password(1, ALFANUMERICI)

# Stampo la password generata
print(password)
