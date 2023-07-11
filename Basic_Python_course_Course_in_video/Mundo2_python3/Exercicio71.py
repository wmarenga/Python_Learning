# Desafio 71:
# Crie um programa que simule o funcionamento de um caixa
# eletrônico. No ínício, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$ 50, R$ 20,
# R$ 10 e R$ 1.

print('='*30)
print('{:^30}'.format('BANCO CURSO EM VÍDEO'))
print('='*30)
valor = int(input("informe o valor a ser sacado : "))

nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
if nota50 != 0:
    print(f"notas de 50 = {nota50}")
if nota20 != 0:
    print(f"notas de 20 = {nota20}")
if nota10 != 0:
    print(f"notas de 10 = {nota10}")
if nota1 != 0:
    print(f"notas de 1 = {nota1}")
print('Obrigado por usar o Banco CURSO EM VÍDEO')
