""" 
Sorterd: 

Obs: Nao confunda, apesar do nome, com a funcao sort() que ja estudamos em listas.
O sort() so funciona em listas.

Podemos utilizar o sorted() com qualquer iteravel.

Como o proprio nome ja diz, sorted() serve para ordenar.

Obs: O sorted(), sempre retorna uma lista com os elementos do iteravel ordenados.

Exemplo:

lista = [4, 7, 3, 8, 1, 4, 2]
lista.sort()
print(lista)

tupla = (4, 7, 3, 8, 1, 4, 2)
tupla.sort() 
print(tupla) # AttributeError

# Exemplo:

# Lista
numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros)) # Ordenar do menor para o maior e retorna uma lista
print(numeros) # A lista original permaneceu intacta

# Tupla
numeros = (6, 1, 8, 2)
print(numeros)
print(sorted(numeros)) # Ordenar do menor para o maior e retorna uma lista
print(numeros) # A tupla original permaneceu intacta

# Set
numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros)) # Ordenar do menor para o maior e retorna uma lista
print(numeros) # O set original permaneceu intacta

# Adicionando parametros ao sorted():

# Exemplo:

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos converter o resultado para outro iteravel

# Convertendo para uma tupla
numeros = [6, 1, 8, 2]
print(numeros)
print(tuple(sorted(numeros, reverse=True))) # Ordena do maior para o menor

# Convertendo para um set
numeros = [6, 1, 8, 2]
print(numeros)
print(set(sorted(numeros, reverse=True))) # Ordena do maior para o menor

# Podemos utilizar o serted() para coisas mais complexas. 

usuarios = [
{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
{'username': 'carla', 'tweets': ['Eu amo meu gato']},
{'username': 'jeff', 'tweets': []},
{'username': 'bob123', 'tweets': []},
{'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'vou sair hoje']},
{'username': 'gal', 'tweets': []},
]

#print(usuarios)
#print(sorted(usuarios)) # TypeError: '<' not supported between instances of 'dict' and 'dict'

# Quando estivermos trabalhando com dicionarios, temos que inserir o parametro key=.

#print(sorted(usuarios, key=len)) # Ordena pela qunatidade de caracteres da chave.

# Ordenar pelo nome de usuario:
# Atencao! A letras maiusculas sao ordenadas primeiro.
#print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Poderiamos ordenar pelo 'tweets' tambem
#print(sorted(usuarios, key=lambda usuario: usuario["tweets"])) # As lista vazias serao as primeiras

# Poderiamos ordenar pelo 'username' tambem do maior para o menor
#print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True)) # As lista vazias serao as primeiras

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
# Ultimo Exemplo:

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Black is Black", "tocou": 4},
    {"titulo": "Too old to rock'n roll, too young to die", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
"""
