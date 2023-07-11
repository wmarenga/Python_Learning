""" 
List Comprehension (aprofundamento do conceito):

Nos podemos adicionar estruturas condicionais logicas as nossas List Comprehension

# Exemplos
numeros = [1, 2, 3, 4, 5, 6]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print(pares)
print(impares)

# Refatorando
# Qualquer numero par modulo de 2 e 0, e 0 em Python e False. (not False == True)
pares = [num for num in numeros if not num % 2]

# Qualquer numero impar modulo de 2 e 1, e 1 em Python e True.
impares = [num for num in numeros if num % 2]
print(pares)
print(impares)

# Exemplo 2

# Se o numero for par multiplicar por 2, se for impar divida por 2
res = [num * 2 if num % 2 == 0 else num/ 2 for num in numeros]
print(res)
"""
