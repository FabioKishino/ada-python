from dataBase import *
from utils import *

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
            clear()
            try:
                updateDataBase(input("Digite o CPF do cliente que deseja alterar: "))
            except:
                print("Erro ao alterar cliente, tente novamente!")
        
        elif (op == 3):
            clear()
            try:
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
            try:
                selectDataBase()
            except:
                print("Erro ao listar clientes, tente novamente!")
        
        elif (op == 6):
            clear()
            return
        
        else:
            clear()
            print("Opção inválida, tente novamente!")

