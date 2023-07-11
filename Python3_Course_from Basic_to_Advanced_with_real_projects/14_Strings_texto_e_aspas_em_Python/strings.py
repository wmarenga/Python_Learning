"""
Strings são textos dentro de aspas (simples e duplas).

str - string

print('Alguma coisa')
print("Alguma coisa")

O Python é uma linguagem de tipágem dinâmica, sendo assim, o interpretador
irá atribuir um tipo de dado de acordo com o parâmetro informado ou atribuido.

nome = 'Wellington'  # (str)
numero = '123456'  # (str)
numero = 123456  # (int)
decimal = 12.11  # (float)
decisao = True  # (bool)
lista = []  # (list)

Para verificar o tipo, usamos o comando:
print(type(lista))
print(type(numero))
print(type(12.11))

Aspas dentro de Aspas:

print('Essa é uma "string" (str).')
print("Essa é uma 'string' (str).")

Usando caractéres de escape (somente usar em último caso):

print('Essa é uma \'string\' (str).')
print("Essa é uma \"string\" (str).")

Quebra de linha:

print("Essa é uma \nstring (str).")

Usando o raw strings:

print(r'Essa é uma \nstring (str).')

Obs: Não poderá ser usado para ignorar aspas internas iguais (simples ou duplas).
# Não funciona
print(r'Essa é uma 'string' (str).')
print(r"Essa é uma "string" (str).")

Erro apresentado:
SyntaxError: invalid syntax. Perhaps you forgot a comma?
"""
