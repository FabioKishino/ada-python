from datetime import datetime
from validate_docbr import CPF
import re
import os
import requests

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

def validaDataNascimento():
    while True:
        dataNascimento = input("Digite a data de nascimento (ex: dd/mm/yyyy): ")
        try:    
            dataConvertida = datetime.strptime(dataNascimento, '%d/%m/%Y').date()
            dataAtual = datetime.now().date()

            if dataConvertida < dataAtual:
                return dataConvertida.strftime('%d/%m/%Y')
            else:
                print("Data inválida. A sua data de nascimento deve ser menor que a data atual ")
        except ValueError as e:
            print("Data de nascimento inválida. Voce recebeu o erro: " + str(e) + " digite novamente! ")
            
def buscarCEP(cep):
  url = f'https://viacep.com.br/ws/{cep}/json/'
  response = requests.get(url, verify=False)

  if response.status_code == 200:
    data = response.json()

    endereco = {
      "CEP": data['cep'],
      "Logradouro": data['logradouro'],
      "Bairro": data['bairro'],
      "Cidade": data['localidade'],
      "Estado": data['uf']
    }

    return endereco