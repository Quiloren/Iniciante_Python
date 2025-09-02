#O usuário digita 5 números, e o programa mostra o maior e o menor deles

numero = []

for i in range(5):
    numeros = float(input("Digite 5 numeros:"))
    numero.append(numeros)

print("Lista digitada:", numero)

maior = max(numero)
menor = min(numero)

print(f"O MAIOR NUMERO É {maior} E O MENOR NUMERO É {menor}")
