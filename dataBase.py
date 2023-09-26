import pyodbc
from utils import clear

def retornaCursorDataBase():
    connection = pyodbc.connect(retornaStringConexaoDataBase())
    cursor = connection.cursor()
    return cursor, connection

def retornaStringConexaoDataBase():
  return(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-D5INV8A;"
    "DATABASE=exxonmobil;"
    "Trusted_Connection=yes;"
  )

def selectDataBase():
    cursor, connection = retornaCursorDataBase()
    cursor.execute("select * from cliente;")
    clientes = cursor.fetchall()
    
    for cliente in clientes:
        print("\n")
        print("Cliente ID: "           + str(cliente[0]))
        print("Nome: "                 + str(cliente[1]))
        print("CPF: "                  + str(cliente[2]))
        print("RG: "                   + str(cliente[3]))
        print("Data de Nascimento: "   + str(cliente[4]))
        print("CEP: "                  + str(cliente[5]))
        print("Logradouro: "           + str(cliente[6]))
        print("Complemento: "          + str(cliente[7]))
        print("Bairro: "               + str(cliente[8]))
        print("Cidade: "               + str(cliente[9]))
        print("Estado: "               + str(cliente[10]))
        print("Número da residência: " + str(cliente[11]))
        print("\n")
    
    x = input("Aperte ENTER para voltar ao menu cliente...")
    clear()
    connection.commit()
  
def insertDataBase(cliente):
    cursor, connection = retornaCursorDataBase()
    insertQuery = '''
    INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, complemento, bairro, cidade, estado, numero_residencia)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    values = (cliente['Nome'], 
              cliente['CPF'], 
              cliente['RG'], 
              cliente['Nascimento'], 
              cliente['CEP']['CEP'], 
              cliente['CEP']['Logradouro'], 
              cliente['Complemento'], 
              cliente['CEP']['Bairro'], 
              cliente['CEP']['Cidade'], 
              cliente['CEP']['Estado'], 
              cliente['Número'])
    cursor.execute(insertQuery, values)
    connection.commit()

def deleteDataBase(cpf):
    cursor, connection = retornaCursorDataBase()
    deleteQuery = "DELETE FROM cliente WHERE cpf = '" + cpf +"';"
    cursor.execute(deleteQuery)
    connection.commit()

def selectClienteDataBase(cpf):
    clear()
    cursor, connection = retornaCursorDataBase()
    selectQuery = "SELECT * FROM cliente WHERE cpf = '" + cpf + "';"
    cursor.execute(selectQuery)
    cliente = cursor.fetchall()
    if len(cliente) == 0:
        print("Cliente não encontrado")
    else:
        for i in cliente:
            print("Cliente ID: "           + str(i[0]))
            print("Nome: "                 + str(i[1]))
            print("CPF: "                  + str(i[2]))
            print("RG: "                   + str(i[3]))
            print("Data de Nascimento: "   + str(i[4]))
            print("CEP: "                  + str(i[5]))
            print("Logradouro: "           + str(i[6]))
            print("Complemento: "          + str(i[7]))
            print("Bairro: "               + str(i[8]))
            print("Cidade: "               + str(i[9]))
            print("Estado: "               + str(i[10]))
            print("Número da residência: " + str(i[11]))


            print("\n")
            x = input("Aperte ENTER para voltar ao menu cliente...")
            clear()

    connection.commit()

def updateDataBase(cliente):
    cursor, connection = retornaCursorDataBase()
    updateQuery = '''
    UPDATE cliente 
    SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ? 
    WHERE cpf = cpf;
    '''
    values = (cliente['Nome'], cliente['CPF'], cliente['RG'], cliente['Nascimento'], cliente['CEP'], cliente['Número'])
    cursor.execute(updateQuery)
    connection.commit()
