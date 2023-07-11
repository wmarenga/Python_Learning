""" 
Dictionary Comprehension:

Pense no seguinte:

Se quisermos criar uma lista, fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla, fazemos:

lista = (1, 2, 3, 4)
lista = 1, 2, 3, 4

Se quisermos criar um set (conjunto), fazemos:

lista = {1, 2, 3, 4}

Se quisermos criar um dicionario, fazemos:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxy

Dictionary Comprehencion
{chave: valor for valor in iteravel}

List Comprehencion
{valor for valor in iteravel}

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# Exemplos

numeros = [1, 2, 3, 4, 5] # Podemos usar tuplas e sets tambem

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)

# Por nao termos repeticao de chaves em dicionarios, os numeros repetidos sarao ignorados
numeros = [1, 2, 3, 4, 5, 1, 2] # Podemos usar tuplas e sets tambem

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)

#Outro Exemplo:
chaves = 'abcde'
valores = [1, 2, 3, 4 ,5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com logica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
"""
