import sqlite3

# criando o arquivo database vazio
conexao = sqlite3.connect('161_sqlite_usando_o_modulo_sqlite3/basededados.db')
cursor = conexao.cursor()

# Criando uma tabela na base de dados se a mesma não existir
# Criamos um campo ID inteiro que será incrementado automaticamente
# Outro campo nome em formato texto e peso em formato float = REAL (SQL)
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# Comando para inserir registro na tabela
# Temos que inserir valores com aspas duplas, quando for texto
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Wellington", 75.5)')

# Corrigindo uma insegurança (comando acima) com SQL Injection
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# Envia o comando em formato de dicionário
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Joãozinho', 'peso': 25})

# Poderia também omitir (nome, peso) da tabela clientes, enviando somente os valores
# Contudo é primordial enviar também o id
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Daniel', 'peso': 113})

# Comando para executar na base de dados
# conexao.commit()

# Alterando dados da tabela
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'nome': 'Joana', 'id': 2})

# Excluindo dados da tabela (MUITA ATENÇÃO AO EXECUTAR ESTE COMANDO EM db REAIS)
# cursor.execute('DELETE FROM clientes WHERE id=:id',
#                {'id': 2})

# É muito importante executar na base de dados para alterá-la
conexao.commit()

# Mostrar todos os valores da tabela (* = tudo)
# cursor.execute('SELECT * FROM clientes')

# Podemos iterar sobre os valores
# for linha in cursor.fetchall():
#    identificador, nome, peso = linha
#    print(identificador, nome, peso)

# Selecionar mais minunciosa
# Mostrar todos os valores da tabela (* = tudo)
# cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')
# Boa prática
cursor.execute(
    'SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 50})

for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

# É muito importante fechar a conexão e o cursor
cursor.close()
conexao.close()
