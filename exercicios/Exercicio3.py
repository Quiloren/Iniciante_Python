numeros = []

while True:
    n1 = int(input("Digite o primero numero: "))
    n2 = int(input("Digite o segundo numero: "))
    n3 = int(input("Digite o terceiro numero: "))
    
    numeros.append(n1)
    numeros.append(n2)
    numeros.append(n3)
    
    break

maior = max(numeros)

print(f"O maior numero é: {maior}")
