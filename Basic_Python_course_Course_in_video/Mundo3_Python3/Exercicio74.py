# Desafio 74:
# Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma Tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor
# que estão na Tupla.

from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10), )
print('-='*30)
print(f'Os números gerados foram: {tupla}', end='')
# opção 1:
print(f'\nO menor número da tupla é {sorted(tupla)[0]}')
print(f'O maior número da tupla é {sorted(tupla)[-1]}')
# Opção 2:
print(f'O menor número da tupla é {min(tupla)}')
print(f'O maior número da tupla é {max(tupla)}')
