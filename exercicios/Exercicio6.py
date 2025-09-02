import random

n = random.randint(1,100)
tentativas = 0


while True:
    resposta = int(input('Digite sua resposta: '))

    if resposta > n:
        print('O NUMERO É MENOR')
        tentativas += 1
    elif resposta < n:
        print('O NUMERO É MAIOR')
        tentativas += 1
    else:
        print(f"ACERTOU, voce tentou {tentativas} ")
        break