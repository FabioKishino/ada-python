from utils import *

# Nome, CPF, RG, Data de Nascimento, CEP, Número residência.
def cadastrarCliente():
    cliente = {
        "Nome": input("Nome: "),
        "CPF": validaCPF(input("CPF: ")),
        "RG": validaRG(input("RG: ")),
        "Nascimento": validaDataNascimento(input("Data de Nascimento: ")),
        "CEP": input("CEP: "),
        "Número": int(input("Número da residência: "))
    }

    return cliente

def menuCliente():
    clientes = []

    while True:
        print("Menu Cliente")
        print("1 - Cadastrar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Buscar Cliente")
        print("4 - Deletar Cliente")
        print("5 - Listar Clientes")
        print("6 - Voltar ao menu anterior")
        op = int(input("Digite a opção desejada: "))

        if (op == 1):
            clear()
            cliente = cadastrarCliente()
            clientes.append(cliente)
        elif (op == 2):
            pass
        elif (op == 3):
            pass
        elif (op == 4):
            pass
        elif (op == 5):
            print(clientes)
        elif (op == 6):
            clear()
            return
        else:
            clear()
            print("Opção inválida, tente novamente!")

