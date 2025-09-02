#O usuário digita um número, e o programa mostra a tabuada desse número de 1 a 10.

numero = int(input("digite um numero:"))

for i in range(1,11):
    resultado = numero * i

    print(f"{numero} X {i} = {resultado}")
    