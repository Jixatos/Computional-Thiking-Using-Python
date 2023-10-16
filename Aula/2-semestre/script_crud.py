import cx_Oracle # (DRIVER)
#import oracledb (DRIVER)

#Create connection
def getConnection():
    try:
        connection = cx_Oracle.connect(user="RMXXXXXX", password="DDMMAA", host="oracle.fiap.com.br", port="1521", service_name="orcl")
        print(f'Conexão: {connection.version}')
    except Exception as e:
        print('Erro ao obter uma conexão', e)
    return connection

def select():
    try:
        connection = getConnection
        cursor = connection.cursor()
        sql_querry = "SELECT * FROM <tabela>"
        cursor.execute(sql_querry)
        for result in cursor:
            print(result)
        connection.commit()
    except Exception as e:
        print(f'Something went wrong - select: {e}')
    finally: 
        close_connection(connection)

def insert():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        sql_query = "INSERT INTO <tabela> VALUES ('<valor>', '<valor>', '<valor>')"
        cursor.execute(sql_query)
        connection.commit()
    except Exception as e:
        print(f'Something went wrong - insert: {e}')
    finally:
        close_connection(connection)

def update():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        sql_query = "UPDATE <tabela> SET <'valores'> WHERE <PK> = <PK>"
        cursor.execute(sql_query)
        connection.commit()
    except Exception as e:
        print(f'Something went wrong - update: {e}')
    finally:
        close_connection(connection)

def delete():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        sql_query = "DELTE FROM <tabela> WHERE <'values'>"
        cursor.execute(sql_query)
        connection.commit()
    except Exception as e:
        print(f'Something went wrong - delete: {e}')
    finally:
        close_connection(connection)

def close_connection(connection):
    try:
        connection.close()
        print(f'Connection Closed')
    except Exception as e:
        print(f'Something went wrong: {e}')

#Principal
print(f'Obtendo do dados do BD')