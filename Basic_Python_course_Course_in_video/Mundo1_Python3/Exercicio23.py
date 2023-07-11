# Desafio 23:
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos
# separados.
# Ex.: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

# Forma Matemática:

número = int(input('Digite um número entre 0 e 9999: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('Analisando o número: {}'.format(número))
print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('A milhar é: {}'.format(m))
