"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples (**Mais Comum**) -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

* Sempre devemos finalizar com o mesmo tipo de aspas que começamos.
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = """Geek University"""
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

# Usando \n pulamos uma linha nos caractéres seguintes.
nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

# Se pulármos uma linha no string, o Python irá imprimir com a linha pulando também.
nome = """Angelina
Jolie"""
print(nome)
print(type(nome))

""" Se precisármos usar aspas dentro do string, devemos usar barra invertida para permitir
visualizar as aspas. (Caracteres de escape)"""
nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())
print(nome.lower())

# Separa a string em duas partes ['Geek', 'University']
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])

# Array [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12, 13,  14 ]
#       ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

nome = 'Geek University'
# A última posição não é considerada [0:4], serão mostradas as posições: 0, 1, 2, 3.
print(nome[0:4])  # Slice de string.

# Comece do primeiro elemento, vá até o último elemento e inverta.
print(nome[::-1])  # Inversão da String -> Método Pythônico.

print(nome.replace('e', 'i'))  # Substitui a letra "e" por "i"
print(type(nome))

# Palíndromo.
texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])
