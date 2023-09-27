from dataBase import *
from utils import *

# Nome, CPF, RG, Data de Nascimento, CEP, Número residência.
def cadastrarCliente():
    cliente = {
        "Nome": input("Nome: "),
        "CPF": validaCPF(input("CPF: ")),
        "RG": validaRG(input("RG: ")),
        "Nascimento": validaDataNascimento(),
        "CEP": buscarCEP(input("CEP: ")),
        "Complemento": input("Complemento: "),
        "Número": int(input("Número da residência: "))
    }

    return cliente

def menuCliente():
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
            try:
                cliente = cadastrarCliente()
                insertDataBase(cliente)
            except:
                print("Erro ao cadastrar cliente, tente novamente!")
        elif (op == 2):
            updateDataBase(input("Digite o CPF do cliente que deseja alterar: "))
        elif (op == 3):
            try:
                clear()
                selectClienteDataBase(input("Digite o CPF do cliente que deseja buscar: "))
            except:
                print("Erro ao buscar cliente, tente novamente!")
        elif (op == 4):
            clear()
            try:        
                deleteDataBase(input("Digite o CPF do cliente que deseja deletar: "))
            except:
                print("Erro ao deletar cliente, tente novamente!")
        elif (op == 5):
            clear()
            selectDataBase()
        elif (op == 6):
            clear()
            return
        else:
            clear()
            print("Opção inválida, tente novamente!")

