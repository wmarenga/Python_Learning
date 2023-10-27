"""
Dictionary Comprehension:

# Exemplo 1:
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

# d1 = dict(lista) com cast
d1 = {x: y for x, y in lista}  # sem cast
print(d1)

d2 = {x: y * 2 for x, y in lista}
print(d2)

# Exemplo 2:
lista = [
    ('chave1', 2),
    ('chave2', 9)
]
d1 = dict(lista)  # com cast
d3 = {x: y * 2 for x, y in lista}
print(d3)

# Exemplo 3:
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]
d4 = {x.upper(): y.upper() * 2 for x, y in lista}
print(d4)

"""
# Exemplo 4
import random

d5 = {x: y for x in range(5) for y in random.choice('asdfgbvbnnhh')}
print(d5)

# Exemplo 5:
d6 = {f'chave_{x}': x ** 2 for x in range(5)}
print(d6)
