palavras = input("Digite uma palavra: ")
contador = 0
for letra in palavras:
    if letra in "aeiouAEIOU":
        contador += 1
print("Total de vogais:", contador)
