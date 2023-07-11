# Desafio 32:
# Faça um programa que leia um ano qualquer e mostre se ele é "Bissexto".

from datetime import date
ano = int(input(
    'Digitel um ano para saber se é Bissexto. Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year  # Pega o ano atual.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} É Bissexto.'.format(ano))
else:
    print('O ano de {} NÃO é Bissexto.'.format(ano))
