x = 10

def incremento(z):
    global x
    x= x + z
    return x

print("prima del test la x è uguale a:", x)
print("Testo la funzione che restituisce:", incremento(5))
print("Dopo il test la x è uguale a:", x)