"""
Entendendo Iterators e Iterables:

Iterator =>
    - Um objeto que pode ser iterado;
    - Um objeto que retorna um dado, sendo um elemento por vez quando
    uma função next() é chamada.

Iterable => Dados são interáveis
    - Um objeto que irá retornar um iterator quando a função iter()
    for chamada.

nome = 'Geek'  # É um Iterable mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # É um Iterable mas não é um iterator.

print(nome)
print(numeros)

# print(next(nome))  # TypeError: 'str' object is not an iterator
# print(next(numeros))  # TypeError: 'list' object is not an iterator

# Tornando um Iterator em Iterable
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # G
print(next(it1))  # e
print(next(it1))  # e
print(next(it1))  # k
print(next(it1))  # StopIteration

print(next(it2))  # 1
print(next(it2))  # 2
print(next(it2))  # 3
print(next(it2))  # 4
print(next(it2))  # 5
print(next(it2))  # 6
print(next(it2))  # StopIteration

"""

nome = 'Geek'

for indice, letra in enumerate(nome):
    print(f'Este é o {indice+1}º iterável: {letra}')
