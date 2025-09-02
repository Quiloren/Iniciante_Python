import random
contador = 0
while True:
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    resultado = num1 + num2
    
    resposta = int(input(f"Quanto é {num1} + {num2} = "))
    if resposta == resultado:
        contador += 1
        print(f"\nParabens \nSeu placar é: {contador}")
    else:
        print(f"\nVoce errou \nSeu placar foi:{contador}")
        break
