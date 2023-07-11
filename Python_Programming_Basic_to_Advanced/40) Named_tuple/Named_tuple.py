"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap tupla

tupla = (1, 2, 3)
print(tupla[1])

Named Tupla (uma tupla nomeada) -> São tuplas diferenciadas, onde especificamos um nome para a mesma e também parâmetros.

# Importando

from collections import namedtuple

# precisamos definir o nome e parâmetros.

# Forma 1 (Declaração Named Tuple - com espaco):

cachorro = namedtuple('cachorro', 'idade raca nome')  # Separados por espaço.

# Forma 2 (Declaração Named Tuple - com virgula):
cachorro = namedtuple('cachorro', 'idade, raca, nome')


# Forma 3 (Declaração Named Tuple - com lista):
# Separados por colchetes, criando uma lista.
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando Named Tuple
ray = cachorro(idade=2, raca='Chow-chow', nome='ray')
print(ray)

# Acessando os dados:

# Forma 1:
print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# Forma 2 (Orientada a objeto):
print(ray.idade)  # idade
print(ray.raca)  # raça
print(ray.nome)  # nome

# Informar o valor e mostrar o índice.
print(ray.index('Chow-chow'))

# Contar quantas ocorrências do valor existem na tupla.
print(ray.count('Chow-chow'))
"""
