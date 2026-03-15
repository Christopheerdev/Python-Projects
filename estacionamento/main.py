estoque = {}

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))

    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade

    print("Produto adicionado com sucesso!\n")


def remover_produto():
    nome = input("Produto para remover: ")

    if nome in estoque:
        del estoque[nome]
        print("Produto removido.\n")
    else:
        print("Produto não encontrado.\n")


def atualizar_quantidade():
    nome = input("Produto: ")

    if nome in estoque:
        quantidade = int(input("Nova quantidade: "))
        estoque[nome] = quantidade
        print("Quantidade atualizada.\n")
    else:
        print("Produto não encontrado.\n")


def mostrar_estoque():
    if len(estoque) == 0:
        print("Estoque vazio.\n")
    else:
        print("\n--- ESTOQUE ---")
        for produto, quantidade in estoque.items():
            print(f"{produto} : {quantidade}")
        print()


while True:

    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Mostrar estoque")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()

    elif opcao == "2":
        remover_produto()

    elif opcao == "3":
        atualizar_quantidade()

    elif opcao == "4":
        mostrar_estoque()

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.\n")
