#importo modulo socket
import socket as so
#importo modulo os che serve per usare funzioni x comunicare con sistema operativo
import os

#creo variabili ip e porta x mettere in ascolto connessioni TCP
SRV_ADDR = "127.0.0.1"
SRV_PORT = 44445

#creo socket in ascolto usando funzione libreria socket
s = so.socket (so.AF_INET, so.SOCK_STREAM)

#configuro il socket creato all'indirizzo e alla porta specificata (binding)
s.bind ((SRV_ADDR, SRV_PORT))

#con il modulo s.liesrt configuro il socket per ascoltare sulla coppia indicata (ip : porta)
#indicando tra le parentesi il numero massimo di connessioni
s.listen (1)

#faccio un print per specificare che sta in attesa di connessioni
print("Server partito! In attesa di connessione...")

#Con il metodo accept accetto e spedisco la connessione con il client che accetta la connessione
connection, address = s.accept()

#faccio un altro print per confermare la connessione con l'indirizzo
print("Client connesso con l'indirizzo:", address)

#faccio partire lo scambio di dati con un ciclo while sempre vero
while True:                                      #ciclo infinito
    home_dir = os.path.expanduser('~')
    path = os.getcwd()
    if path.startswith(home_dir):                #sostituisci il percorso della home con '~'
        path = path.replace(home_dir,'~', 1)     #1 x sostituire solo la prima occorrenza
    connection.sendall (path.encode() + b"$ ")   #invio un finto prompt
    data = connection.recv(1024)                 #per ricevere i dati dal client
    if not data : break                          #do conferma che è arrivato a destinazione
    comando = data.decode('utf-8').rstrip("\n")  #stampo quello che mi invia il client codificato in utf-8
                                                 #nb: utf-8 e' la codifica del terminale
    if comando.startswith("cd "):
        os.chdir(comando.split(" ")[1])
    elif comando.startswith("exit"):             #chiudo connessione e ne apre un altra
        connection.close()
        connection,address = s.accept()
    elif comando.startswith("die"):
        break
    else:
        esegui = os.popen(comando).read().rstrip('\n')
        connection.sendall(esegui.encode() + "\n".encode())
    
connection.close()                  #chiudo la connessione
s.close()
