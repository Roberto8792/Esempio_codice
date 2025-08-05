x = int(input ("Inserisci un numero: "))

if (x < 10):
    print("Hai inserito un numero minore di 10")
elif x == 10:
    print("Hai inserito il numero 10")
else:
    print("Hai inserito un numero maggiore a 10")

if x is int:
    print("Il valore inserito è un intero")
else:
    print("Il valore inserito non è un intero")

x = input ("Dammi una frase: ").lower()

if ("ciao" in x) or ("hey" in x):
    print("Ciao, come stai?")
else:
    print("Perche non hai salutato?")
