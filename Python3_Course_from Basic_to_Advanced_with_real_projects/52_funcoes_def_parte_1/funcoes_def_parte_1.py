"""
Funções (def) em Python - Parte 1:

# Exemplo normal

def saudacao(msg, nome):
    return msg, nome


print(saudacao('Olá', 'Wellington'))

# Utilizando valor padrão


def saudacao(msg='Olá', nome='Usuário'):
    return msg, nome


print(saudacao())

# Podemos inverter quando os parâmetros forem nomeados
print(saudacao(nome='Zezinho', msg='Hi'))
"""
# Exemplo usando replace()


def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('i', 'o')
    return f'{msg} {nome}'


print(saudacao(nome='Zezinho', msg='Hi'))
