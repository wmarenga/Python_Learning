"""
Dicionários em Python {chave: valor}:

As chaves em um dicionários têm que ser únicas.

Os dicionários são similares a lista, possuem (chave/ índice e valor),
contudo nos dicionários, nós podemos alterar os valores das chaves.
Nas listas a índexação é automática e não podemos alterar o índice.

Tipos de dados nas chaves:
- 'str': 'valor'
- 123: 'Outro valor'
- (1, 2, 3, 4): 'tupla'

# Exemplo:

d1 = {'chave1': 'valor da chave'}
print(d1)

# Adicionando uma nova chave

d1['nova chave'] = 'valor da nova chave'
print(d1)

# Acessando uma chave no dicionário
print(d1['chave1'])

# Outra maneira de criar um dicionário (com cast)

d2 = dict(nome='Wellington', idade='51', altura=1.70)
print(d2)

# chaves duplicadas
# Somente será criada a última chave, pois são duplicadas.
d1 = {'chave': 'valor', 'chave': 'abc', 'chave': 'valor real da chave'}
print(d1)

d2 = {'str': 'valor', 123: 'Outro valor', (1, 2, 3, 4): 'tupla'}
print(d2[(1, 2, 3, 4)])  # tupla

# print(d2['naoexiste'])  # KeyError

# Contornando este erro

if 'nao existe' in d2:
    print(d2['naoexiste'])
else:
    d2['naoexiste'] = 'Agora existe'

print(d2)

# Outra maneira de contornar com get():
# Desta maneira o código não pára de funcionar

d2 = {'str': 'valor', 123: 'Outro valor', (1, 2, 3, 4): 'tupla'}
print(d2.get('nomedachave'))  # None

if d2.get('nomedachave') is not None:
    print(d2.get('nomedachave'))
else:
    d2['nomedachave'] = 'Agora ela existe'

print(d2)

# Alterando uma chave existente

d2['str'] = 'Ruff'
print(d2)

# Outra maneira de alterar uma {chave: valor}
d2.update({'nova_chave': 'novo_valor'})
print(d2)

d2.update({'str': 'Renata'})
print(d2)

# Excluindo chave do dicionário
d2 = {'str': 'valor', 123: 'Outro valor', (1, 2, 3, 4): 'tupla'}
print(d2)

# del(d2['str'])
# print(d2)

print('str' in d2)  # Verificando pela chave
print('valor' in d2.keys())  # Verificando pela chave

print('valor' in d2.values())  # Verificando pelo valor

# Verificanco quantos pares de {chave: valor} existem
print(len(d2))

# Iterando sobre um dicionário

d2 = {'chave1': 'valor', 'chave2': 'Outro valor', 'chave3': 'tupla'}

# Acessando pelas chaves (keys)
for k in d2.keys():
    print(k)

# Acessando pelos valores (values)
for v in d2.values():
    print(v)

# Acessando pelo conjunto chave:valor (items)
# Retorna tuplas
for i in d2.items():
    print(i)
    print(i[0], i[1])  # chave e valor separadamente

d2 = {'chave1': 'valor', 'chave2': 'Outro valor', 'chave3': 'tupla'}

# Desempacotando dicionários
for k, v in d2.items():
    print(k, v)

# Criando uma lista com os elementos do dicionário (chave: valor)
lista = list()
for k, v in d2.items():
    lista.append(k)
    lista.append(v)

print(lista)

# Dicionários dentro de dicionários
clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira',
    }
}

# O primeiro for pega os valores externos, e o segundo for pega os
# dicionários internos.
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')  # \t é para dar um tab (recuo)

# Quando determinamos que uma variável recebe outra variável, ambas
# serão alteradas. Não criamos uma cópia e sim associamos/ apontando
# ambas ao mesmo espaço de memória.
d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
v = d3
print(v)
print(d3)

v[1] = 'Luiz'  # Estamos alterando v e d3.
print(v)
print(d3)

d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
# Criando uma shallow copy:
v = d3.copy()
v[1] = 'Oi'
print(d3)
print(v)

# Acessando um elemento de uma lista dentro de um valor do dicionário
print(v['d'][0])

# Alterando o valor
v['d'][0] = 'Joãozinho'
print(d3)
print(v)

# O deepcopy cria uma cópia independente

import copy

d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
v = copy.deepcopy(d3)

v[1] = 'Luiz'
v['d'][0] = 'Joãozinho'

print(d3)
print(v)

"""
# Fazendo cast em listas ou tuplas para um dicionário (por semelhança):
import os


def limpar():
    os.system('cls')


limpar()

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)

# Eliminando a última chave:valor de um dicionário (pop())
d2 = {
    1: 2,
    2: 3,
    4: 5,
}
# d2.pop(4)  # Eliminando a chave 4
# d2.popitem()  # Elimina o último ítem independente de qual seja.

# Concatenando 2 dicionários

d5 = {
    'a': 'b',
    'c': 'd',
}

print(d5)

d2.update(d5)  # Irá incluir d5 no d2 (concatenando os 2)
print(d2)
