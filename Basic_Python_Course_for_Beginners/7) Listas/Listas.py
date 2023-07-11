'''
Listas:

Listas são conjuntos de dados que podem conter dados de diferentes tipos. Elas possuem valores indexados a
partir de zero.

lista_a = [5, 6, 7, 8, 9]
print(type(lista_a))

Acessando dados de uma lista:
print(lista_a[0])

Podemos imserir qualquer tipo de elemento a uma lista (str, float, int, complex, etc)
lista_a = [5, 6, 'Python', 8, 9]

Uma lista dentro de outra lista
lista_a = [5, 6, ['Python',2], 8, 9]

Acessando uma lista dentro de outra lista
lista_a[2][0]
print(lista_a)

lista_b = ['c','a','e']
lista_c = lista_b + lista_b

print(lista_c)

lista_d = lista_c * 4
print(lista_d)

Acho o comprimento de uma lista (quantos elementos temos em uma lista)
print(len(lista_c))

Como selecionar um intervalo de elementos em uma lista
lista_d = ['c', 'a', 'e', 'c', 'a', 'e']
Todos os 2 elementos iniciais
lista_d[:2]

Todos os elementos apos o indice 2
lista_d[2:]
Este processo se chama slicing. 

'''