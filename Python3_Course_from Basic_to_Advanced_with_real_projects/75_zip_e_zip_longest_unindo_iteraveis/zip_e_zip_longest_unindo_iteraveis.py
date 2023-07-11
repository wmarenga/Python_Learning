"""
Zip => Unindo iteráveis
Zip_longest => Itertools
"""
from itertools import zip_longest, count

# indice = range(100, 1000, 10)  # 100, 110, 120
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

# Irá unir pela menor lista
cidades_estados = zip(indice, estados, cidades)
# Gera um loop infinito
# cidades_estados = zip_longest(indice, estados, cidades, fillvalue='Estado')

# Ele é um iterador (um número de cada vez)
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
