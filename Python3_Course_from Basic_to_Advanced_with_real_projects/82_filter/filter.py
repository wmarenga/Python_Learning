"""
Assim como map, a função filter não retorna uma lista e sim um
iterator do tipo map. Para resolver isso, devemos fazer um cast
para torná-la uma lista.

# Exemplo

from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

# Exemplo com list comprehension

nova_lista2 = [x for x in lista if x > 5]
print(list(nova_lista2))

# Exemplo

nova_lista3 = filter(lambda p: p['preco'] > 20, produtos)
for produto in nova_lista3:
    print(produto)

# Exemplo mais complexo


def filtra(produto):
    if produto['preco'] > 50:
        produto['eh_caro'] = True
    return True


nova_lista4 = filter(filtra, produtos)

for produto in nova_lista4:
    print(produto)

"""

# Exemplo filtro em pessoas (maiores de idade)


def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True


nova_lista5 = filter(filtra, pessoas)

for produto in nova_lista5:
    print(produto)
