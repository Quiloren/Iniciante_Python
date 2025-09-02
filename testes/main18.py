while True:
    print("\n===Menu=== \n1. Calculadora \n2. Sair")
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
        operacao = input("escolha uma operação(+, -, *, /): ")
        
        if operacao == "+":
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif operacao == "-":
            resul = num1 - num2
            print(f"{num1} - {num2} = {resul}")
        elif operacao == "*":
            result = num1 * num2 
            print(f"{num1} X {num2} = {result}")
        elif operacao == "/":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida!")
            resulta = num1 / num2
            print(f"{num1} / {num2} = {resulta}")
    elif escolha == "2":
        break
    else:
        print("Opção inválida, tente novamente!")

