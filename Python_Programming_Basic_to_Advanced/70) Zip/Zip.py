""" 
ZIP:
zip() = Cria um iteravel (Zip Object) que agrega elemento de cada um dos iteraveis passados como 
        entrada em pares.

# Exemplos:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla ou Dicionario.

print(list(zip1)) # Gera uma lista contendo tupla dentro 
# forma pares: [(lista1[0], lista2[0]...listan[0]), (lista1[1], lista2[1]...listan[1]),(lista1[2], lista2[2]...listan[2])]
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1)) # Aparece vazio, pois ja foi convertido para uma lista, para exibir nos temos que inserir o zip novamente.
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1)) # Aparece vazio, pois ja foi convertido para uma lista, para exibir nos temos que inserir o zip novamente.
zip1 = zip(lista1, lista2) # (chave: valor)
print(dict(zip1)) # Aparece vazio, pois ja foi convertido para uma lista, para exibir nos temos que inserir o zip novamente.

# Obs: O zip() utiliza como parametro o menor tamanho em iteraveis. Isso significa que se estiver
# trabalhando com iteraveis de tamanhos diferentes, ira parar quando os elementos do menor iteravel acabar.
lista3 = [7, 8, 9, 10 ,11]
zip2 = zip(lista1, lista2, lista3)
print(list(zip2)) # O zip somente pega os 3 primeiros elementos da lista3.

# Podemos utilizar diferentes iteraveis com zip()

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8 ,9 ,10]
dicionario = {'a': 11,'b': 12,'c': 13,'d': 14,'e': 15,}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1),(1, 2),(2, 3),(3, 4),(4, 5)]
print(list(zip(*dados))) # Desempacotamento dos valores 
# [(0, 1, 2, 3 ,4), (1, 2, 3, 4 ,5)] => [(elementos do index 0 das tuplas), (elementos do index 1 das tuplas)]

# exemplos mais complexos:

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

ger_zip = list(zip(alunos, prova1, prova2))
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)} # Dictionary COmprehension

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
# zip(prova1, prova2) => Cria uma lista com tuplas das provas 1 e 2 [(80, 98), (91, 89), (78, 53)]
# map(lambda nota: max(nota), zip(prova1, prova2) => Pega a maior nota em cada tupla [98, 91, 78]
# dict(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))) => Cria um dicionario com alunos e a maior nota da prova
print(dict(final))

"""
