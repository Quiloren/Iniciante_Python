#O usuário digita dois números e escolhe uma operação (+, -, *, /).

Num1 = int(input("Digite um Numero:"))
Num2 = int(input("Digite outro Numero:"))
Operacao = input("Digite um Operador (+,-,*,/):")

if Operacao == "+":
    print(f"O Resultado É:", Num1 + Num2)

elif Operacao == "-":
    print(f"O Resultado É:", Num1 - Num2)

elif Operacao == "*":
    print(f"O Resultado É:", Num1 * Num2)

elif Operacao == "/":
    if Num2 != 0:
        print(f"O Resultado É:", Num1 / Num2)
    else:
        print("Erro: Não é possivel dividir por zero!")
        
else:
    print(f"ERRO")