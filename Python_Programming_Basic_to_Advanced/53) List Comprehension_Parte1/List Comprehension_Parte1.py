"""
List COmprehension:

- Utilizando List Comprehension nos podemos gerar novas listas com dados processados
a partir de outro iteravel. 

# Sintaxe da List COmprehension

[ dado for dado in iteravel ]

# Exemplos

numeros = [1, 2, 3, 4 ,5]
res = [num * 10 for num in numeros] # Para cada num em numeros, multiplique por 10 (lendo do final para o inicio)
print(res)

# Para entender melhor o qeu esta acontecendo, devemos dividir a expressao em duas partes:
# - A primeira parte: for num in numeros
# - A segunda parte: num * 10

# Outro Exemplo
res = [num/ 2 for num in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(num) for num in numeros]
print(res)

# List Comprehension versus Loop

# Usando Loop for
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for num in numeros:
    numeros_dobrados.append(num * 2)
    
print(numeros_dobrados)

# Usando List Comprehension
print([num * 2 for num in numeros])

# Convertendo caracteres para maiusculo
nome = 'Geek University'

print([letra.upper() for letra in nome])

# Convertendo os nomes para primeira letra maiuscula
amigos = ['marcia', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amig.capitalize() for amig in amigos])
print([amig.title() for amig in amigos])

# Multiplicando cada numero entre 1 e 9 por 3
print([numero * 3 for numero in range(1, 10)])


# Gerando uma lista booleana para casa valor de outra lista, convertendo para boolena
# 0, [] e '' - Sao False em Python
# True, 1, 3.14 - Sao True
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Convertendo uma lista de numeros inteiros para uma lista de strings
print([str(numero) for numero in [1, 2, 3, 4 ,5]])
"""
print([str(numero) for numero in [1, 2, 3, 4, 5]])
