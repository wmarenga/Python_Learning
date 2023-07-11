"""
Módulo Collections: Ordered Dict

https://docs.python.org/pt-br/3.8/library/collections.html#collections.OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Em um dicionario, a ordem de insercao dos elementos nao e garantida.
for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

OrderedDict -> É um dicionário. que nos garante a ordem de inserção dos elementos.

# Fazendo o import:

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict.

from collections import OrderedDict

# Dicionário comum

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

# True -> já que a ordem dos elementos não importa para o dicionário.
print(dict1 == dict2)

# Ordered Dict.

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

# False -> já que a ordem do elementos importa para o OrderedDict.
print(odict1 == odict2)
"""
