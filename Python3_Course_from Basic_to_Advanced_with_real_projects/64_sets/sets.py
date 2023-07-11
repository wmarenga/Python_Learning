"""
sets = conjuntos:

Os sets são similares a dicionários, porem não possuem chaves e índices.
Os sets assim como as tuplas são imutáveis.
Os sets não possuem ordenação.
Os sets não aceitam repetições de valores.

add                      => adiciona
update                   => atualização
clear                    => limpa
discard                  => Removendo elementos
set.union (|)            => une
intersection (&)         => todos os elementos presentes nos dois sets
difference (-)           => elementos apenas no set da esquerda (atenção a ordem dos sets)
symmetric_difference (^) => elementos que estão nos dois sets, mas não em ambos.

Exemplo:

s1 = {1, 2, 3, 4, 5}

print(s1)

# Podemos iterar sobre os valores com for, mas não diretamente (pelos índices)
for v in s1:
    print(v)

# Podemos adicionar em uma lista
lista = []
for v in s1:
    lista.append(v)
print(lista)

# Criando sets vazios com cast
s2 = set()

# Inserindo valores no set
s2.add(1)
s2.add(2)
# s2.add((1, 2, 3, 'Luiz'))
print(s2)

# Revovendo elementos
s2.discard(2)
print(s2)

# update
s1 = set()
s1.update('Python')
# Sem valores duplicado
s1.update([1, 2, 3, 4, 5], {5, 6, 7, 8}) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1)  # serão inseridade todas as letras isoladamente e sem ordem

# Eliminando elementos duplicados
l1 = [1, 2, 2, 1, 1, 3, 4, 4, 6, 6, 7, 8, 9, 9, 'Luiz', 'Luiz']
l1 = set(l1)
print(l1)

# Fazendo um cast para converter para lista novamente
l1 = list(l1)  # Os elementos poderão voltar fora de ordem.
print(l1)

# union (|)
s1 = {1, 2, 3, 4, 5}
s2 = {5, 5, 6, 7, 8, 9}  # adiciona sem repetições
s4 = {'a', 'b', 'c'}
# s3 = s1 | s2
s3 = s1.union(s2, s4)
print(s3)

# intersection (&)
s1 = {1, 2, 6, 4, 5, 'b'}
s2 = {5, 6, 7, 8, 9, 'a'}
s3 = {'a', 'b', 'c', 5, 6}
# s4 = s2.intersection(s1, s3)  # {5}
s4 = s1 & s2 & s3
print(s4)

# difference (-)
# Tudo que pertence ao primeiro set menos os elementos que estão
# nos dois sets.
s1 = {1, 2, 6, 4, 5, 'b'}
s2 = {5, 6, 7, 8, 9, 'a'}
s3 = {'a', 'b', 'c', 5, 6}

# s4 = s1 - s2
s4 = s1.difference(s2)
print(s4)

"""
# symmetric_difference (^)
# Tudo que não é igual em ambos
s1 = {1, 2, 6, 4, 5, 'b'}
s2 = {5, 6, 7, 8, 9, 'a'}
s3 = {'a', 'b', 'c', 5, 6}
s4 = s2 ^ s1
print(s4)
