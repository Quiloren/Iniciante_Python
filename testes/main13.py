

numeros = []

while True:
    print("\n1. Digitar um numero \n2. Ver os números digitados \n3. Sair")
    
    escolha = input("Faça sua escolha:")
    
    if escolha == "1":
        numero = int(input("Digite um número:"))
        numeros.append(numero)
        pass

    elif escolha == "2":
        print("\nNúmeros digitados:", numeros)
        pass

    elif escolha == "3":
        break
    
    else:
        print("\nOpçao invalida, tente novamente.")

