#O programa escolhe um número secreto entre 1 e 10, e o usuário tenta adivinhar até acertar.

import random

numero_secreto = random.randint(1, 100)

chute = 0

while chute != numero_secreto:
    chute = int(input("Digite um numero:"))
    
    if chute < numero_secreto:
        print("Tente um número MAIOR")
    elif chute > numero_secreto:
        print("Tente um número MENOR")

print("Parabéns, voce acertou!")
