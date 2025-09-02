numeros = []

while True:
    numero = input("Digite um Numero (ou digite sair):")
    
    if numero == "sair":
        break
    else:
        numero = int(numero)
        numeros.append(numero)

print("Numeros Digitados:", numeros)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print("\nO MAIOR NUMERO É:", maior, "\n O MENOR NUMERO É:", menor, "\nA MEDIA DOS NUMEROS É:", media)

