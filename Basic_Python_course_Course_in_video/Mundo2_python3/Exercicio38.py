# Desafio 38:
# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O PRIMEIRO número é maior.')
elif num2 > num1:
    print('O SEGUNDO número é maior.')
elif num1 == num2:
    print('O dois números são IGUAIS.')
