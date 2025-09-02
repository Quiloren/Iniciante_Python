numero = []

for i in range(5):
    numeros = int(input("Digite 5 numeros:"))
    numero.append(numeros)

    print("Numeros digitados:", numero)

soma = sum(numero)

print("O Resultado da soma dos 5 numeros é:", soma)

