'''
Métodos para dicionários:

Método                    Descrição

items()            Retorna os itens do dicionário
keys()             Retorna as chaves do dicionário
values()           Retorna as chaves do dicionário
pop(key)           Remove a chave especificada e retorna o valor do item
copy()             Retorna uma cópia
clear()            Remove os itens
get(key)           Retornas a váriável em key

Disponível em: https://link.springer.com/chapter/10.1007%2F978-1-4471-6642-9_12

Criacao de um dicionario vazio
alg_romanos = {}

alg_romanos = {'I':1 , 'II':2,'III':3, 'IV':4}

Acessando um elemento do dicionario 
alg_romanos['II']

Retiramos o elemento pela chave 'II' e retorna o valor do elemento'
II = alg_romanos.pop('II')
print(II)

Retorna as chaves do dicionario (iteravel, pois podemos criar listas, Tuplas e usar em um loop com o output gerado)
alg_romanos = {'I':1 , 'II':2,'III':3, 'IV':4}
print(alg_romanos.keys())
saida: dict_keys(['I', 'II', 'III', 'IV'])

Retorna os elementos do dicionario (iteravel, pois podemos criar listas, Tuplas e usar em um loop com o output gerado)
alg_romanos = {'I':1 , 'II':2,'III':3, 'IV':4}
print(alg_romanos.values())
saida: dict_values([1, 2, 3, 4])

O items() retorna um dicionario com chaves e valores
alg_romanos = {'I':1 , 'II':2,'III':3, 'IV':4}
print(alg_romanos.items())
saida: dict_items([('I', 1), ('II', 2), ('III', 3), ('IV', 4)])

Retorna uma lista, onde cada elemento e uma Tupla
alg_romanos = {'I':1 , 'II':2,'III':3, 'IV':4}
print(list(alg_romanos.items()))
saida: [('I', 1), ('II', 2), ('III', 3), ('IV', 4)]

Acessando elemento dentro da lista e dentro da Tupla
alg_romanos = {'I':1 , 'II':2,'III':3, 'IV':4}
print(list(alg_romanos.items())[0][1])

'''