"""
Listas em Python:
- Fatiamento;
- append, insert, pop, del, clear, extend, +;
- min, max;
- range.
texto = 'valor'
lista = [1, 2, 3, 4, 'Luiz Otávio', True, 10.5, Class()]

# Índices 0       1      2    3    4     5
# Negat  -6      -5     -4   -3   -2    -1
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
# Um ítem de uma lista suporta vários valores, enquanto que os
# índices de uma string somente suportam um valor.
# print(lista[1])
# print(lista[-5])

# Índices 0123456789
# Negat(-)10987654321
string = 'ABacanaCDE'
# print(string[1])
# print(string[-10])

# Alterando um índice de uma string
lista[5] = 'Qualquer outra coisa'
# print(lista)

# Exibindo um intervalo de ítens de uma lista
# print(lista[0:3])
# print(lista[:4])  # por padrão o start é zero
# print(lista[2:])  # do índice 2 até o final
# print(lista[2::2])  # do índice 2 até o final de 2 em 2.
print(lista[:-1:2])  # do último ítem até o início de 2 em 2.
print(lista[::-1])  # Invertendo a lista

l1 = [1, 2, 3]
l2 = [4, 5, 6]

# Usando +:

# l3 = l1 + l2  # concatenando as listas l1 e l2
# print(l1)
# print(l2)
# print(l3)

# Usando extend (extendendo a l1 com a lista l2)

l1.extend(l2)
print(l1)
print(l2)

# Usando append (insere um novo valor ao final da lista)
l2.append('b')
print(l1)
print(l2)

# Usando insert para adicionar valores em qualquer lugar da lista
l2.insert(0, 'banana')
print(l2)

# Excluindo elementos do final de uma lista (pop())

l2 = [4, 5, 6]
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)

# Excluindo valores com del
#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)

del (l2[3:5])  # excluindo por fatiamento [4, 5]
print(l2)

l2.insert(0, 'Banana')
print(l2)

del(l2[0])
print(l2)

"""
# Exibir o maior valor da lista com max

#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2))
print(min(l2))

# Criando lista mais facilmente com (range() e list())
l3 = list(range(1, 10))  # [1, 2, 3, 4, 5 ,6 ,7 ,8, 9]
l3 = list(range(0, 100, 8))  # Com intervalos

for valor in l3:
    print(valor, end=', ')

# Acumulando 8 ao próximo número
soma = 0
acumulado = list()
for valor in l3:
    soma += valor
    acumulado.append(soma)

print(acumulado)

# Verificar os tipos de cada elemento de uma lista

l4 = ['String', True, 10, -20.5]

for elem in l4:
    print(f'O seu elemento é {elem} e o seu tipo é {type(elem)}.')
