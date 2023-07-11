# Exemplo 1 (atalho)
nome = input('Qual o seu nome? ')
print(nome or 'Você não digitou nada!')

# Exemplo 2
a = 0
b = None
c = False
d: list = []
e: dict = {}
f = 22
g = 'Wellington'

variavel = a or b or c or d or e or f or g
# Exibe o primeiro True => 22
print(variavel)

# Da maneira manual (mais trabalhosa)
if a:
    variavel = a
elif b:
    variavel = b
elif c:
    variavel = c
elif d:
    variavel = d
elif e:
    variavel = e
elif f:
    variavel = f
else:
    variavel = g
