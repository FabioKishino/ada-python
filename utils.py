from datetime import datetime
from validate_docbr import CPF
import re
import os

def clear():
    os.system('cls')

def validaCPF(clienteCPF):
    cpf = CPF()
    clienteCPF = re.sub('[-.]', '', clienteCPF)
    
    while True:
        if cpf.validate(clienteCPF):
            clienteCPF_formatado = f'{clienteCPF[:3]}.{clienteCPF[3:6]}.{clienteCPF[6:9]}-{clienteCPF[9:]}'
            print(f'CPF {clienteCPF_formatado} válido')
            return clienteCPF
        else:
            clienteCPF = input("CPF inválido, digite novamente: ")


def validaRG(rg):
    padraoRG = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    while True:
        rg = re.sub('[-.]', '', rg)
        rg = f'{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}'
        
        if re.match(padraoRG, rg):
            return rg
        else:
            rg = input("RG inválido, digite novamente: ")

def validaDataNascimento(dataNascimento):
    while True:
        dataConvertida = datetime.strptime(dataNascimento, '%d/%m/%Y').date()
        dataAtual = datetime.now().date()

        if dataConvertida < dataAtual:
            return dataConvertida.strftime('%d/%m/%Y')
        else:
            dataNascimento = input("Data de nascimento inválida, digite novamente: ")