"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne
o valor da função2 executada.
"""


def funcao1(funcao2):
    return funcao2


def funcao2():
    variavel = 'Wellington'
    return variavel


funcao2 = funcao2()
print(funcao1(funcao2))
