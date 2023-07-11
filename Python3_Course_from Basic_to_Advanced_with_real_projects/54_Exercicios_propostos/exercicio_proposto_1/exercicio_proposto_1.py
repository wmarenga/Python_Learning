"""
Crie uma função que exibe uma saudação com os parâmetros saudação
e nome.
"""


def saudacao(saudacao='Olá', nome='Usuário'):
    return f'{saudacao} {nome.capitalize()}! Bem vindo ao sistema.'


print(saudacao('Hello', 'Wellington'))
