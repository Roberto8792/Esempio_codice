x = int(input ("Calcolo del fattoriale: "))
num = 1
fattoriale = x

while num < x:
    fattoriale *= num
    num += 1

print(f"{x}! = {fattoriale}")
