# Desafio 16:
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
# a sua porção Inteira.
# Ex.: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

# 1) Opção:
import math
from math import trunc
número = float(input('Digite um número: '))
print('O número {}, tem a parte Inteira {}'.format(número, trunc(número)))

# 2) Opção:
número = float(input('Digite um número: '))
print('O número {}, tem a parte Inteira {}'.format(número, math.trunc(número)))

# 3) Opção:
número = float(input('Digite um número: '))
print('O número {}, tem a parte Inteira {}'.format(número, int(número)))
