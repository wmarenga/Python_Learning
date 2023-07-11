"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única
expressão.

variavel := expressão
"""
# nome = 'Geek University'
# print(nome)

# Declaramos a variável e atribuímos um dados a ela
# print(nome := 'Geek University')
# ao mesmo tempo.

# Python 3.7
# cesta = []
# fruta = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Informe a fruta: ')
#

# Python 3.8
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)

print(cesta)
