# Desafio 54:
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ᵃ pessoa nasceu? '.format(c)))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade. \n{} pessoas são menores de idade.'.format(maior, menor))
