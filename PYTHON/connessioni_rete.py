#importo modulo socket
import socket as so

#creo variabili ip e porta x mettere in ascolto connessioni TCP
SRV_ADDR = "127.0.0.1"
SRV_PORT = 44444

#creo socket in ascolto usando funzione libreria socket
s = so.socket (so.AF_INET, so.SOCK_STREAM)

#configuro il socket creato all'indirizzo e alla porta specificata (binding)
s.bind ((SRV_ADDR, SRV_PORT))

#con il modulo s.liesrt configuro il socket per ascoltare sulla coppia indicata (ip : porta)
#indicando tra le parentesi il numero massimo di connessioni
s.liste (1)

#faccio un print per specificare che sta in attesa di connessioni
print("Server partito! In attesa di connessione...")

#Con il metodo accept accetto e spedisco la connessione con il client che accetta la connessione
connection, address = s.accept()

#faccio un altro print per confermare la connessione con l'indirizzo
print("Client connesso con l'indirizzo:", address)

#faccio partire lo scambio di dati con un ciclo while sempre vero
while True:                         #ciclo infinito
    data = connection.recv(1024)    #per ricevere i dati dal client
    if not data : break             #se il client chiude connessione esco dal loop
    connection.sandall (b"Letto\n") #risposta al clien con saluto
                                    #comando x inviare a tutti un msg a schermo
                                    #di conferma che è arrivato a destinazione
    print(data.decode('utf-8'))     #stampo l'invio del client codificato in utf-8
    
connection.close()                  #chiudo la connessione
    