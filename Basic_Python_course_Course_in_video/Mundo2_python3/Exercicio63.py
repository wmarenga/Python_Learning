# Desafio 63:
# Escreva um programa que leia um NÚMERO n inteiro
# qualquer e mostre na tela os n primeiros elementos
# de uma SEQUÊNCIA DE FIBONACCI.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Informe quantos termos quer mostrar: '))
tant = 0
tpos = 1
print('~'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('~'*30)
print('{} -> {}'.format(tant, tpos), end='')
cont = 3
while cont <= n:
    tfim = tant + tpos
    print(' -> {}'.format(tfim), end='')
    tant = tpos
    tpos = tfim
    cont += 1
print(' -> FIM!')
print(''*30)
