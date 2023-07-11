""" 
Set Comprehencion:

lista = [1, 2, 3, 4 ,5]
lista = {1, 2, 3, 4 ,5}

"""
# Exemplos:

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro Exemplo:

numeros = {x ** 2 for x in range(10)}
print(numeros)

# DESAFIO! Faca uma alteracao na estrutura acima para gerar um dicionario ao inves de set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para Finalizar (trabalhando com string)

letras = {letra for letra in 'Geek University'}
print(letras) # As letras repetidas nao serao incluidas no set e tambem apresentara um set sem ordenacao
