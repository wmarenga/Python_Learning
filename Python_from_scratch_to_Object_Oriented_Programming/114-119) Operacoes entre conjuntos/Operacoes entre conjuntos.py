# Operacoes entre conjuntos

# Subtracao entre conjuntos:
# Tudo que esta em cj2 excluindo e nao pertence a cj1
cj1 = {1, 2, 3, 4, 5}
cj2 = {1, 3, 5, 7, 9}

print(cj2 - cj1)

# Uniao entre conjuntos
conjunto1 = {5, 10, 15, 20, 25}
conjunto2 = {1, 2, 3, 4, 5, 10}

uniao = conjunto1.union(conjunto2)

print(uniao)

# Intersecao entre dois conjuntos
conjunto1 = {5, 10, 15, 20, 25}
conjunto2 = {1, 2, 3, 4, 5, 10}

intersec = conjunto1.intersection(conjunto2)

print(intersec)

# Operadores logicos em conjuntos numericos
conjunto1 = {5, 10, 15, 20, 25}
conjunto2 = {1, 2, 3, 4, 5, 10}

# Avaliando a quantidade de elementos (criterio)
print(uniao == conjunto1)
print(uniao >= conjunto2)
