from validate_docbr import CPF

def validaCPF():
    clienteCPF = input("CPF: ")
    cpf = CPF()

    while True:
        if cpf.validate(clienteCPF):
            return clienteCPF
        else:
            clienteCPF = input("CPF inválido, digite novamente: ")