"""
Tipo Booleano

Algebra Booleana, criado por George Boole

2 constates: Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

Obs.: Sempre com a inicial maiúscula

Errado: true, false

Correto: True, False
"""

ativo = False
print(ativo)

"""
Operações básicas
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, se for
falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""

print(not ativo)

logado = True

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro valor deverá ser verdadeiro.
- True or True -> True
- True or False -> True
- False or True -> True
- False or False -> False
"""
print(ativo or logado)

# E (and)
"""
É uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.
- True and True -> True
- True and False -> False
- False and True -> False
- False and False -> False
"""
print(type(True))

ativo = True
print(type(ativo))
print(dir(ativo))

print(5 > 6)
print(5 < 6)
print(6 == 6)
print(4 <= 5)
