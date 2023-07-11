# Desafio 60:
# Faça um programa que leia um NÚMERO qualquer
# e mostre o seu FATORIAL.
# Ex.: 5! - 5x4x3x2x1 = 120
"""
# Usando um método do Python:
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {}! é {}.'.format(n, f))
"""
num = int(input('Digite um número: '))
cont = num
f = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))
