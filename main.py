import json

ARQUIVO = "dados.json"


def carregar_dados():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


def calcular_irrigacao(umidade, ph, nutrientes):
    if umidade < 50 and 5 <= ph <= 7 and nutrientes >= 2:
        return "LIGADA"
    return "DESLIGADA"


def cadastrar():
    nome = input("Nome da plantação: ")
    umidade = float(input("Umidade (%): "))
    ph = float(input("pH: "))
    nutrientes = int(input("Nutrientes OK (0 a 3): "))

    irrigacao = calcular_irrigacao(umidade, ph, nutrientes)

    registro = {
        "nome": nome,
        "umidade": umidade,
        "ph": ph,
        "nutrientes": nutrientes,
        "irrigacao": irrigacao
    }

    dados = carregar_dados()
    dados.append(registro)
    salvar_dados(dados)

    print("\nRegistro salvo com sucesso!\n")


def listar():
    dados = carregar_dados()

    if not dados:
        print("\nNenhum dado cadastrado.\n")
        return

    print("\n===== HISTÓRICO =====\n")
    for d in dados:
        print(f"Plantação: {d['nome']}")
        print(f"Umidade: {d['umidade']}%")
        print(f"pH: {d['ph']}")
        print(f"Nutrientes OK: {d['nutrientes']}")
        print(f"Irrigação: {d['irrigacao']}")
        print("------------------------")


def menu():
    while True:
        print("\n=== SISTEMA DE IRRIGAÇÃO ===")
        print("1 - Cadastrar leitura")
        print("2 - Ver histórico")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
