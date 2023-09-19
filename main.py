from cliente import menuCliente
from utils import clear

## Main Function

def main():
    op = 0
    run = True
    clear()
    while(run == True):
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - Cliente")
        print("2 - Ordem")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        op = int(input("Digite a opção desejada: "))

        if(op == 1):
            clear()
            menuCliente()
        elif(op == 2):
            pass
        elif(op == 3):
            pass
        elif(op == 4):
            pass
        elif(op == 5):
            run = False
        else:
            clear()
            print("Opção inválida, tente novamente!")

main()