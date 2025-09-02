import random

while True:
    print("\n1. Iniciar \n2. Sair")

    menu = input("Faça sua escolha:").lower()

    if menu == "Iniciar":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        resposta = int(input(f"Quanto é : \n{num1} + {num2}?"))
        if resposta == (num1 + num2):
            print("Acertou! Vamos para proxima soma.")
        else:
            print(f"Errou! A resposta correta era {num1 + num2}.")
            break
    elif menu == "sair":
        break
    else:
        print("ERRO")

