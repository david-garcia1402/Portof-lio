#importar o banco de dados SQLite
import sqlite3 as lite

#criando a conexão SQLite
con = lite.connect('Dados.db') #nome do banco de dados

###OPERAÇÃO CRUD

#inserir os dados (CREATE)

def inserir_form(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, n_serie, imagem) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        cur.execute(query, i)

#atualizar os dados (UPDATE)
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE Inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, n_serie=?, imagem=? WHERE id=?'
        cur.execute(query, i)

#deletar os dados (DELETE)
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Inventario WHERE id = ?'
        cur.execute(query, i)

#ler os dados(READ)
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM Inventario'
        cur.execute(query)
        #ver os dados
        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


#ler os dados individualmente
def ver_individual_form(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = 'SELECT * FROM Inventario WHERE id=?'
        cur.execute(query, id)
        #ver os dados
        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual