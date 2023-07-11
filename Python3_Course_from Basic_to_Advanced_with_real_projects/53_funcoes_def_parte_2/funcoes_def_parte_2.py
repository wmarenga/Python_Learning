"""
Funções (def) em Python - Parte 2:

# Exemplo 1

def funcao(var):
    return var
    print('Isso não será rxrcutado.')


variavel = funcao('Valor que eu quero.')
print(variavel)  # None (sem valor)

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

# Exemplo 2

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2
    else:
        return 'Conta inválida'


divide = divisao(8, 2)  # (n1=8, n2=2)
print(divide)

divide = divisao(8, 0)  # DivisionError
print(divide)
"""
# Exemplo 3


def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(var, type(var))

print(type(f))

var = dumb()('E colocar o meu valor aqui.')
print(var)
print(type(var))

# Verificando o id() da memória da variável
var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('Blaaaaaaa')
