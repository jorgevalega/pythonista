# SQL - Structured Query Language (Linguagem estruturada de busca)
# db.sqlite3

import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    # Criar uma conexao com o banco de dados
    sql = conexao.cursor()
    # Rodar Comando SQL
    sql.execute('CREATE TABLE IF NOT EXISTS banda(nome TEXT, estilo TEXT, membros INTEGER);')
        
    # Exemplo de inserir dados
    sql.execute('INSERT INTO banda(nome, estilo, membros) VALUES ("Banda 1", "Rock", 3)')
    # Exemplo de usar dados da minha aplicação em um comando SQL
    nome = input('Digite o nome da banda')
    estilo = input('Digite o estilo da banda')
    quantidade_integrantes = int(input('Digite a quantidade de integrantes da banda'))

    sql.execute('INSERT INTO banda values(?,?,?)', [nome,estilo,quantidade_integrantes])

    conexao.commit()

    # Exibir dados no console python (terminal)
    bandas = sql.execute('SELECT * FROM banda;')
    for banda in bandas:
        print(banda)



