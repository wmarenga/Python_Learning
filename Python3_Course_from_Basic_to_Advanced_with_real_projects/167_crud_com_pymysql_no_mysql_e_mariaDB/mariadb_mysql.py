import pymysql.cursors
from contextlib import contextmanager


# CRUD - CREATE, READ, UPDATE, DELETE


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()
        print('Conexão fechada')


# INSERE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'

#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55),
#         ]

#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# DELETA QUANTIDADE DETERMINADA DE REGISTROS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# DELETA REGISTRA ENTRE UM RANGE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         # Excluindo vários registros
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         # sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         # cursor.execute(sql, (10, 12))
#         # Excluindo um registro
#         # sql = 'DELETE FROM clientes WHERE id = %s'
#         # cursor.execute(sql, (6,))
#         conexao.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 5))
#         conexao.commit()


# ESTE SELECIONA OS DADOS DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        # cursor.execute(
        #     'SELECT nome, sobrenome FROM clientes ORDER BY id ASC LIMIT 100')
        # Abreviaturas não são boas práticas de programação
        # cursor.execute(
        #     'SELECT nome as n, sobrenome as sn FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()
        # print(resultado)
        for linha in resultado:
            print(linha)
            # print(linha['nome'], linha['sobrenome'])
            # print(linha['n'], linha['sn'])
