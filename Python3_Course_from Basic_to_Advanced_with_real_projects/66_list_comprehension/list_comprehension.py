"""
List Comprehension:

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exemplo 1:
ex1 = [variavel for variavel in l1]
print(ex1)

# Exemplo 2:
ex2 = [v * 2 for v in l1]
print(ex2)

# Exemplo 3:
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

# Exemplo 4:
l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]
print(ex4)

# Exemplo 5:
tupla = (
    ('chave1', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)  # cast para um dicionário
print(ex5)
print(ex5['valor2'])

# Exemplo 6:
l3 = list(range(100))

# Os números divisíveis por 2
ex6 = [v for v in l3 if v % 2 == 0]
print(ex6)

# Os números divisíveis por 3 e também por 8
ex6 = [v for v in l3 if v % 3 == 0 and v % 8 == 0]
print(ex6)

# Exemplo 7 (utilizando o else):
l3 = list(range(100))
ex7 = [v if v % 3 == 0 and v % 8 == 0 else '-' for v in l3]
print(ex7)
"""
