from cliente import menuCliente

## Main Function

def main():
    op = 0
    run = True
    while(run == True):
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - Cliente")
        print("2 - Ordem")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        op = int(input("Digite a opção desejada: "))

        if(op == 1):
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
            print("Opção inválida, tente novamente!")


main()