from datetime import datetime

# ============================
#   SISTEMA DE ESTACIONAMENTO
# ============================

moradores = {}
inquilinos = {}
visitantes = {}  # Armazena entrada, saída e valor da diária

DIARIA = 20.00  # preço fixo da diária


# ------------------------------------------
# Função: Verifica categoria da placa
# ------------------------------------------
def verificar_placa(placa):
    if placa in moradores:
        return "morador"
    elif placa in inquilinos:
        return "inquilino"
    elif placa in visitantes:
        return "visitante"
    else:
        return None


# ------------------------------------------
# Função: Cadastrar nova placa
# ------------------------------------------
def cadastrar_placa():
    print("\n--- Cadastro de Placas ---")
    placa = input("Digite a placa: ").upper()

    if verificar_placa(placa):
        print("❗ A placa já está cadastrada.")
        return

    print("\nSelecione a categoria:")
    print("1 - Morador")
    print("2 - Inquilino (mensal)")
    print("3 - Visitante (diária)")

    op = input("Escolha: ")

    if op == "1":
        moradores[placa] = True
        print("✔ Cadastrado como MORADOR.")

    elif op == "2":
        inquilinos[placa] = True
        print("✔ Cadastrado como INQUILINO.")

    elif op == "3":
        visitantes[placa] = {
            "entrada": datetime.now(),
            "saida": None,
            "valor": None
        }
        print("✔ Visitante registrado com horário de entrada.")
        print(f"Entrada: {visitantes[placa]['entrada']}")

    else:
        print("❗ Opção inválida.")


# ------------------------------------------
# Registrar saída de visitante
# ------------------------------------------
def registrar_saida():
    print("\n--- Registrar Saída ---")
    placa = input("Digite a placa do visitante: ").upper()

    if placa not in visitantes:
        print("❗ Visitante não encontrado.")
        return

    visitantes[placa]["saida"] = datetime.now()
    visitantes[placa]["valor"] = DIARIA

    print("\n✔ Saída registrada!")
    print(f"Entrada: {visitantes[placa]['entrada']}")
    print(f"Saída:   {visitantes[placa]['saida']}")
    print(f"Valor da diária: R$ {DIARIA:.2f}")


# ------------------------------------------
# Consultar placa
# ------------------------------------------
def consultar_placa():
    print("\n--- Consulta de Placas ---")
    placa = input("Digite a placa: ").upper()

    categoria = verificar_placa(placa)

    if not categoria:
        print("❗ Placa não encontrada.")
        return

    print(f"\nCategoria: {categoria.upper()}")

    if categoria == "visitante":
        dados = visitantes[placa]
        print(f"Entrada: {dados['entrada']}")
        print(f"Saída:   {dados['saida']}")
        print(f"Valor:   {dados['valor']}")


# ------------------------------------------
# Histórico completo de visitantes
# ------------------------------------------
def listar_visitantes():
    print("\n--- Histórico de Visitantes ---")

    if not visitantes:
        print("Nenhum visitante cadastrado.")
        return

    for placa, dados in visitantes.items():
        print("\nPlaca:", placa)
        print("Entrada:", dados["entrada"])
        print("Saída:", dados["saida"])
        print("Valor pago:", dados["valor"])


# ------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------
def menu():
    while True:
        print("\n=========== ESTACIONAMENTO ===========")
        print("1 - Cadastrar placa")
        print("2 - Registrar saída de visitante")
        print("3 - Consultar placa")
        print("4 - Histórico de visitantes")
        print("5 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_placa()
        elif op == "2":
            registrar_saida()
        elif op == "3":
            consultar_placa()
        elif op == "4":
            listar_visitantes()
        elif op == "5":
            print("Encerrando sistema...")
            break
        else:
            print("❗ Opção inválida.")


menu()
