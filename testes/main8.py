#Crie uma lista de compras onde o usuário pode ir adicionando itens até digitar "sair".

lista_compras = []

while True:
    item = input("Digite um item (ou 'sair' para terminar): ")

    if item == "sair":
        break
    else:
        lista_compras.append(item)

print("\nSua lista de compras:")

for item in lista_compras:
    print (item)