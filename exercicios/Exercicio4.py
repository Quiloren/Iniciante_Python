n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = n1 + n2 + n3 + n4 / 3

if media >= 7:
    print(f"APROVADO, sua nota foi: {media}")
else:
    print(f"Reprovado, sua nota foi: {media}")

