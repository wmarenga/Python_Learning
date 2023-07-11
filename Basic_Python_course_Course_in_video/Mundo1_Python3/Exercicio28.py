# Desafio 28:
# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = int(input('Digite um número entre 0 e 5! '))
numcomp = random.randint(0, 5)
if num == numcomp:
    print('O seu número foi {} e o número do computador foi {}.'.format(num, numcomp))
    print('PARABÉNS! Você venceu!')
else:
    print('O seu número foi {} e o número do computador foi {}.'.format(num, numcomp))
    print('Que pena! Você perdeu!')
print('Tente novamente!')
