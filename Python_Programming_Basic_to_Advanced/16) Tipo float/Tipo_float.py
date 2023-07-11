"""
Tipo Float

Tipo real, decimal

Casas decimais

Obs.: O separador de casas decimais na programação é o ponto (.) e não a vírgula (,)
"""

# Errado do ponto de vista do "float", pois gera um "tuple".
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos coverter um float para um inteiro.
"""
Obs.: Ao converter valores inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
num = 5j
print(num)
print(num ** 2)
print(type(num))


num = 25
print(type(num))
# Exibe o número em float.
print(type(float(num)))
