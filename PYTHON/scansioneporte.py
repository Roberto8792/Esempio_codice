import socket as so 

target = input("inserisci l'indirizzo da scandire: ")
prange = input("inserisci il range delle porte (es 5-200): ")
#uso split per ricavere un array per ricavare porta superiore e inferiore
rrange = prange.split("-")
lowport = int(rrange[0])
highport = 65535 #qui va la porta massimo
if len(rrange) > 1:
    highport = int(rrange[1])
print(f"scansisco il target {target} della porta {lowport} alla porta {highport}")
porte_chiuse = []
#faccio partire un ciclo for con il range porte da scandire
for port in range(lowport, highport+1):
    #avviamo una connessione tcp ipv4
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    #TESTIAMO IL 3WAy HANDSHAKE
    status = s.connect_ex((target,port))

    if (status == 0):
        #se 0 la connessione è avvenuta e quindi siamo contenti
        print(f"*** Porta {port} - Aperta ***")
    else:
        porte_chiuse.append(port)
    s.close()

    domanda = input("vuoi vedere le porte chiuse?")
    if domanda.upper().startswith("S"):
        #faccio il join di tutte le porte chiuse
        print("\nChiusa: ".join([str(n) for n in porte_chiuse]))
