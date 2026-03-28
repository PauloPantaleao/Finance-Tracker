import sqlite3
def inicializar_banco():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS salario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor REAL NOT NULL)''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS despesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL)''')
    conexao.commit()
    conexao.close()
def get_despesas():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT * FROM despesas''')
    resultados = cursor.fetchall()
    conexao.close()
    return resultados
def get_salario():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
    SELECT valor FROM salario WHERE id = 1''')
    salario = cursor.fetchone()
    conexao.close()
    if salario is None:
        return 0.0
    else:
        return salario[0]
def set_salario(novo):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO salario (id, valor) VALUES (1, ?)''', (novo, ))
    conexao.commit()
    conexao.close()
def adicionar_despesas(desc, valor):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO despesas (descricao, valor) VALUES (?, ?)''', (desc, valor))
    conexao.commit()
    conexao.close()
def remover_despesa(id):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    cursor.execute('''
    DELETE FROM despesas WHERE id = ?''', (id, ))
    conexao.commit()
    conexao.close()