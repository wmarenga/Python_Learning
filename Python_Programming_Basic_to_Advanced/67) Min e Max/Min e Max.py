"""
Min e Max:

max() => Retorna o maior valor em um iteravel ou o maior de dois ou mais elementos.
min() => Retorna o menor valor em um iteravel ou o menor de dois ou mais elementos.

# Exemplo (max)

# Lista
lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # 129

# Tupla
tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) # 129

# Set (conjunto)
conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto)) # 129

# Dicionario
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario)) # O dicionario passa o maior pela chave como default ('f')
print(max(dicionario.values())) # Quando inserimos .values(), estamos pedindo o maior valor dos valores ('129')

# Faca um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(f'O maior valor e: {max(val1, val2)}')

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print(max('Geek University'))

# Exemplo (min)

# Lista
lista = [1, 8, 4, 99, 34, 129]
print(min(lista)) # 129

# Tupla
tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla)) # 129

# Set (conjunto)
conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto)) # 129

# Dicionario
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario)) # O dicionario passa o maior pela chave como default ('f')
print(min(dicionario.values())) # Quando inserimos .values(), estamos pedindo o maior valor dos valores ('129')

# Faca um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(f'O menor valor e: {min(val1, val2)}')

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University')) # O menor valor e o espaco em branco

# Outros Exemplos:

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome))) # Ollivander
print(min(nomes, key=lambda nome: len(nome))) # Tim

# Obs: Pressionando a tecla Ctrl temos acesso ao help() da funcao ou parametro

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Black is Black", "tocou": 4},
    {"titulo": "Too old to rock'n roll, too young to die", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! E se quisermos imprimir somente o titulo da misica
print(f"A musica mais tocada e: {max(musicas, key=lambda musica: musica['tocou'])['titulo']}")
print(f"A musica mais tocada e: {min(musicas, key=lambda musica: musica['tocou'])['titulo']}")

# Como encontrar a nusica nais tocada e a menos tocada sem usar max, min e lambda

# Musica que tocou mais:
max = 0
for mus in musicas:
    if mus['tocou'] > max:
        max = mus['tocou']

for mus in musicas:
    if mus['tocou'] == max:
        print(f"A musica mais tocada foi: {mus['titulo']}")
    
# Musica que tocou menos:
min = len(musicas)
for mus in musicas:
    if mus['tocou'] < min:
        min = mus['tocou']

for mus in musicas:
    if mus['tocou'] == min:
        print(f"A musica menos tocada foi: {mus['titulo']}")

# Comparacao de quanto foi utilizacao da menoria, utilizada no codigo com lambda e com for
from sys import getsizeof

print(f"Exibe a lista toda, ordenada por musicas mais tocadas (com lambda): {getsizeof(max(musicas, key=lambda musica: musica['tocou']))} bytes da memoria.")
print(f"Exibe a lista toda, ordenada por musicas memos tocadas (com lambda): {getsizeof(min(musicas, key=lambda musica: musica['tocou']))} bytes da memoria.")

print(f"Exibindo somente o titulo da musica mais tocada (com lambda): {getsizeof(max(musicas, key=lambda musica: musica['tocou'])['titulo'])} bytes da memoria.")
print(f"Exibindo somente o titulo da musica menos tocada (com lambda): {getsizeof(min(musicas, key=lambda musica: musica['tocou'])['titulo'])} bytes da memoria.")

# Musica que tocou mais:
max = 0
for mus in musicas:
    if mus['tocou'] > max:
        max = mus['tocou']

for mus in musicas:
    if mus['tocou'] == max:
        print(f"Exibindo somente o titulo da musica mais tocada (com for): {getsizeof(mus['titulo'])} bytes da memoria.")

# Musica que tocou menos:
min = len(musicas)
for mus in musicas:
    if mus['tocou'] < min:
        min = mus['tocou']

for mus in musicas:
    if mus['tocou'] == min:
        print(f"Exibindo somente o titulo da musica menos tocada (com for): {getsizeof(mus['titulo'])} bytes da memoria.")
"""
