# Desafio 111:
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos
# chamados moeda e dado. Tranfira todas as funções utilizadas no desafios
# 107, 108, 109 para o primeiro pacote e mantenga tudo funcionando.


import moeda

preço = float(input('Digite o preço '))
taxaaumento = int(input('Digite a taxa de aumento % '))
taxaredução = int(input('Digite a taxa de redução % '))
moeda.resumo(preço, taxaaumento, taxaredução)
