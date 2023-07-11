from dados import produtos, pessoas, lista
from functools import reduce

# Exemplo acumulando todos os valores da lista
acumula = 0
for item in lista:
    acumula += item

print(acumula)

# Exemplo com lambda
# Reduce(função acumulador(ac), item da lista(i): i + ac, lista, start)
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

# Exemplo com dicionário
soma_precos = reduce(lambda ac, p: round(p['preco'] + ac, 2), produtos, 0)
print(soma_precos)
print(round(soma_precos / len(produtos), 2))  # média dos preços

# Exemplo com idades

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades)
print(soma_idades / len(pessoas))  # média de idades
