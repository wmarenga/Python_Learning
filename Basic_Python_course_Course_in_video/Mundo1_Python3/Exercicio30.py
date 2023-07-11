# Desafio 30:
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número digitado é {}'.format(num))
    print('O seu número é PAR!')
else:
    print('O número digitado é {}'.format(num))
    print('Seu número é IMPAR')
