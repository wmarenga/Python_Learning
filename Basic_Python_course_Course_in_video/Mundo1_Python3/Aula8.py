"""
from math import sqrt, floor  # Para importar um funcionalidade específica.
# Quando importamos as funcionalidade de "math", serão inseridas todas as novas opções.
# import math
num = int(input('Digite um número: '))
raiz = sqrt(num)
# raiz = math.sqrt(num) - Somente usamos esta forma quando importamos todas as funcionalidades.
# print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) - Somente com todas as funcionalidades.
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

Biblioteca Random:

import random
# num = random.random() - gera um número aleatório entre 0 e 1.
num = random.randint(1, 10)  # gera um número aleatório entre 1 e 10.
print(num)

Importando Emoji's (https://pypi.org/search/?q=emoji):

import emoji
print(emoji.emojize("Ola Mundo :globe_with_meridians:", use_aliases=True))

"""
