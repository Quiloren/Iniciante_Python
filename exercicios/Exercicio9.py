crescente = []
qtd = 5
for i in range(qtd):
    n = int(input("Digite um numero: "))
    crescente.append(n)

crescente.sort(reverse = False)
print(crescente)