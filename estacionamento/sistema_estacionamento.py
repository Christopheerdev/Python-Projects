from datetime import datetime

# ============================
#   CLASSES (POO)
# ============================

class Veiculo:
    def __init__(self, placa):
        self.placa = placa

    def exibir(self):
        return f"Placa: {self.placa}"


class Morador(Veiculo):
    def tipo(self):
        return "Morador"


class Inquilino(Veiculo):
    def tipo(self):
        return "Inquilino"


class Visitante(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.entrada = datetime.now()
        self.saida = None
        self.valor = None

    def registrar_saida(self, diaria):
        self.saida = datetime.now()
        self.valor = diaria

    def tipo(self):
        return "Visitante"

    def exibir(self):
        return f"""
Placa: {self.placa}
Entrada: {self.entrada}
Saída: {self.saida}
Valor: {self.valor}
"""


# ============================
#   SISTEMA
# ============================

veiculos = []
DIARIA = 20.0


# ------------------------------------------
# Buscar veículo
# ------------------------------------------
def buscar_veiculo(placa):
    for v in veiculos:
        if v.placa == placa:
            return v
    return None


# ------------------------------------------
# Cadastrar placa
# ------------------------------------------
def cadastrar_placa():
    print("\n--- Cadastro de Placas ---")
    placa = input("Digite a placa: ").upper()

    if buscar_veiculo(placa):
        print("❗ A placa já está cadastrada.")
        return

    print("\nSelecione a categoria:")
    print("1 - Morador")
    print("2 - Inquilino (mensal)")
    print("3 - Visitante (diária)")

    op = input("Escolha: ")

    if op == "1":
        veiculos.append(Morador(placa))
        print("✔ Cadastrado como MORADOR.")

    elif op == "2":
        veiculos.append(Inquilino(placa))
        print("✔ Cadastrado como INQUILINO.")

    elif op == "3":
        v = Visitante(placa)
        veiculos.append(v)
        print("✔ Visitante registrado!")
        print(f"Entrada: {v.entrada}")

    else:
        print("❗ Opção inválida.")


# ------------------------------------------
# Registrar saída
# ------------------------------------------
def registrar_saida():
    print("\n--- Registrar Saída ---")
    placa = input("Digite a placa: ").upper()

    v = buscar_veiculo(placa)

    if not v:
        print("❗ Veículo não encontrado.")
        return

    if isinstance(v, Visitante):
        v.registrar_saida(DIARIA)
        print("\n✔ Saída registrada!")
        print(v.exibir())
    else:
        print("❗ Apenas visitantes possuem saída registrada.")


# ------------------------------------------
# Consultar placa
# ------------------------------------------
def consultar_placa():
    print("\n--- Consulta de Placa ---")
    placa = input("Digite a placa: ").upper()

    v = buscar_veiculo(placa)

    if not v:
        print("❗ Placa não encontrada.")
        return

    print(f"\nCategoria: {v.tipo()}")

    if isinstance(v, Visitante):
        print(v.exibir())
    else:
        print(v.exibir())


# ------------------------------------------
# Listar visitantes
# ------------------------------------------
def listar_visitantes():
    print("\n--- Histórico de Visitantes ---")

    encontrou = False

    for v in veiculos:
        if isinstance(v, Visitante):
            print(v.exibir())
            encontrou = True

    if not encontrou:
        print("Nenhum visitante cadastrado.")


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


# ============================
# EXECUÇÃO
# ============================

menu()
