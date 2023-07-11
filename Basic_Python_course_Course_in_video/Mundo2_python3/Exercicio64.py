# Desafio 64:
# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre
# QUANTOS NÚMEROS foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

num = int(input('Digite um número: '))
cont = 1
novonum = 0
soma = novonum + num
while novonum != 999:
    novonum = int(input('Digite outro número: '))
    soma = soma + novonum
    cont += 1
soma = soma - 999
print('A soma é {} e foram digitado {} números.'.format(soma, cont - 1))
