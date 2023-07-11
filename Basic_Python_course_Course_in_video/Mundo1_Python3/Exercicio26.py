# Desafio 26:
# Faça um programa que leia uma frase pelo teclado e mostre:
# 1) Quantas vezes aparece a letra "a";
# 2) Em que posição a primeira vez;
# 3) Em que posição a última vez.

algo = str(input('Digite alguma coisa: ')).lower().strip()
print('Na frase que digitou aparece {} a letra "a".'.format(algo.count('a')))
print('Na frase que digitou aparece a primeira vez a letra "a" na posição {}.'.format(
    algo.find('a')+1))
print('Na frase que digitou aparece a última vez a letra "a" na posição {}.'.format(
    algo.rfind('a')+1))
