def cambia_globale():
    
    global x
    x = 1

x = 10

print("prima del test la x è uguale a:", x)
cambia_globale()
print("Dopo il test la x è uguale a:", x)