numero = []
qtd = 1
for i in range(qtd):
    n = int(input("Digite um numero: "))
    numero.append(n)

numero.sort(reverse = True)
print(numero)