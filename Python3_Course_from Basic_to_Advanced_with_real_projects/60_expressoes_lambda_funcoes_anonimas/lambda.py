"""
Expressões lambda (Funções Anônimas):

Esta função é muito útil quando precisamos passar uma função para
outra função como parâmetros ou método de uma classe.

# Exemplo 1:

def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print(var)


# a = lambda x, y: x * y


print(a(2, 2))

# Exemplo 2:

lista = [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8]]
lista.sort()  # Não altera pois temos uma lista dentro de outra lista.
print(lista)


# Ordena pelo preço do produto
def func(item):
    return item[1]  # Ordena pelo valor do produto.


lista.sort(key=func)  # Crescente
print(lista)
lista.sort(key=func, reverse=True)  # Decrescente
print(lista)
"""
# Exemplo 2:

lista = [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8]]

# Exemplo com lambda

lista.sort(key=lambda item: item[1])  # Crescente
lista.sort(key=lambda item: item[1], reverse=True)  # Decrescente
print(lista)

# Outra forma de ordenar listas sem alterar a lista

print(sorted(lista, key=lambda i: i[1]))  # Crescente
print(sorted(lista, key=lambda i: i[1], reverse=True))  # Decrescente

# Para ordenar pelo nome do produto (alterando o índice)

print(sorted(lista, key=lambda i: i[0]))  # Crescente
print(sorted(lista, key=lambda i: i[0], reverse=True))  # Decrescente

print(lista)
