from utils import validaCPF

# Nome, CPF, RG, Data de Nascimento, CEP, Número residência.
def cadastrarCliente(clientes):
    cliente = {
        "Nome": "",
        "CPF": "",
        "RG": "",
        "Nascimento": "",
        "CEP": "",
        "Número": 0
    }
    
    while True:
        nome = input("Nome: ")
        cpf = validaCPF()
        rg = input("RG: ")
        dataNascimento = input("Data de Nascimento: ")
        cep = input("CEP: ")
        numeroResidencia = int(input("Número da residência: "))
        break

    return clientes.append(cliente)

def menuCliente():
    print("Menu Cliente")
    print("1 - Cadastrar Cliente")
    print("2 - Alterar Cliente")
    print("3 - Buscar Cliente")
    print("4 - Deletar Cliente")
    print("5 - Listar Clientes")
    print("6 - Voltar ao menu anterior")
    op = int(input("Digite a opção desejada: "))

    clientes = []

    if (op == 1):
        cadastrarCliente(clientes)
        print(clientes)
    elif (op == 2):
        pass
    elif (op == 3):
        pass
    elif (op == 4):
        pass
    elif (op == 5):
        pass
    elif (op == 6):
        return
    else:
        print("Opção inválida, tente novamente!")

