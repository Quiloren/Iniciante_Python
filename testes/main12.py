numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite 10 numeros:"))
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Numeros Digitados:", numeros)

print("Numeros Pares:", pares ,"Numeros Impares:", impares)

