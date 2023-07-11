"""
A função map não retorna uma lista e sim um iterator do tipo map.
Para resolver isso, devemos fazer um cast para torná-la uma lista.

# Exemplo com lambda e list comprehension

from dados import produtos, pessoas, lista

# Com lambda
nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))

# Resolvendo da mesma forma com list comprehension
nova_lista2 = [x * 2 for x in lista]
print(nova_lista2)

# Exemplo com dicionário

for p in produtos:
    print(p)

# Definindo uma funcao que aumenta preço


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


# pegando somente os preços do dicionário

novos_produtos = map(aumenta_preco, produtos)
# precos = map(lambda p: p['preco'], produtos)

for produto in novos_produtos:
    print(produto)

from dados import produtos, pessoas, lista


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


# nomes = map(lambda p: p['nome'], pessoas)
# Aumentamos as idades em 20%
nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
"""
# Utilizando mais argumentos dentro da função com map()
# Sim, mas tu precisaria de uma função no meio do caminho...
# Tipo, uma função que retorna outra.

produtos = [
    {'nome': 'P0', 'preco': 10.23},
    {'nome': 'P1', 'preco': 14.65},
    {'nome': 'P2', 'preco': 18.56},
    {'nome': 'P3', 'preco': 22.23},
    {'nome': 'P4', 'preco': 71.87},
    {'nome': 'P5', 'preco': 70.03},
    {'nome': 'P6', 'preco': 55.12},
    {'nome': 'P7', 'preco': 14.56},
    {'nome': 'P8', 'preco': 76.65},
    {'nome': 'P9', 'preco': 51.32},
]


def aumenta_preco(produto, porcentagem):
    produto['preco'] = produto['preco'] * (1 + (porcentagem/100))
    return produto


novos_produtos = map(lambda produto: aumenta_preco(produto, 10), produtos)
print(list(novos_produtos))

# Se o lambda ficar confuso:

produtos = [
    {'nome': 'P0', 'preco': 10.23},
    {'nome': 'P1', 'preco': 14.65},
    {'nome': 'P2', 'preco': 18.56},
    {'nome': 'P3', 'preco': 22.23},
    {'nome': 'P4', 'preco': 71.87},
    {'nome': 'P5', 'preco': 70.03},
    {'nome': 'P6', 'preco': 55.12},
    {'nome': 'P7', 'preco': 14.56},
    {'nome': 'P8', 'preco': 76.65},
    {'nome': 'P9', 'preco': 51.32},
]


def aumenta_preco(produto, porcentagem):
    produto['preco'] = produto['preco'] * (1 + (porcentagem/100))
    return produto


def funcao_do_map(produto):
    return aumenta_preco(produto, 10)


novos_produtos = map(funcao_do_map, produtos)
print(list(novos_produtos))
