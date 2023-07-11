'''
Entendendo o funcionamento de modulos e pacotes:

** importando a biblioteca
import statistics 
z = [10, 20, 30, 40]
x = statistics.mean(z)
y = statistics.median(z)
print(x)
print(z)

** Criando uma abreviacao para o nome da biblioteca

import statistics as est
z = [10, 20, 20, 40]
x = est.mean(z)
y = est.median(z)
print(x)
print(y)

** importando as funcionalidade mean e median da biblioteca diretamente. Somente escrevemos os nome das
funcionalidade diretamente. 

from statistics import mean, median
z = [10, 20, 20, 40]
x = mean(z)
y = median(z)
print(x)
print(y)

** importacao de toda a biblioteca. Somente escrevemos os nome das funcionalidade diretamente. 

from statistics import *
z = [10, 20, 20, 40]
x = mean(z)
y = median(z)
print(x)
print(y)

'''