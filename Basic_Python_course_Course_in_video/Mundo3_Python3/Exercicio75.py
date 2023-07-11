# Desafio 75:
# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma Tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9;
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input('Digite o primeiro número: ')),
         int(input('Digite o segundo número: ')),
         int(input('Digite o terceiro número: ')),
         int(input('Digite o quarto número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor não foi digitado em nenhuma posição!')
print('Os valores pares digitados foram ', end='')
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')
