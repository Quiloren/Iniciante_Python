carrinho_item = []
p = []

while True:
    print("=====Carrinho_de_Compras=====")
    print("1. Adicionar item ao carrinho ")
    print("2. Remover item do carrinho ")
    print("3. Itens no carrinho e total ")
    print("0. Encerrar compras")
    escolha = int(input("\nFaça sua escolha: "))

    if escolha == 1:
        item = input("\nDigite o produto: ")
        preco = float(input("\nDigite o preço do produto: "))
        carrinho_item.append(item)
        p.append(preco)
    elif escolha == 2:
        remover = input("Digite o nome do produto que deseja remover: ")
        remover_preco = float(input("Digite o preço do produto que deseja remover: "))
        if remover in carrinho_item:
            carrinho_item.remove(remover)
            print(f"O produto {remover} foi removido do carrinho")
        if remover_preco in p:
            p.remove(remover_preco)
        else:
            print(f"O produto {remover} não esta no carrinho")
    elif escolha == 3:
        juntos = list(zip(carrinho_item, p))
        for i, p1 in juntos:
            print(f"{i} preço:{p1}$")
        soma = sum(p)
        print(f"\nTotal deu: {soma:.2f}$")
    elif escolha == 0:
        break
    else:
        print("Opção invalida!")

