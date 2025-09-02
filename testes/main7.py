#O usuário digita 3 notas, e o programa calcula a média e diz se ele foi aprovado (>= 6).

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
resultado = (nota1 + nota2 + nota3) / 3

if resultado >= 6:
    print(f"Aprovado, sua nota foi: {resultado}")
else:
    print(f"Reprovado, sua nota foi: {resultado}")
