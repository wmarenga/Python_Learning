# Desafio 70:
# Crie um programa que leia o nome e preço de vários
# produtos. O programa deverá perguntar se o usuário
# vai continuar. No final, mostre:
# A) Qual é o total gasto na compra;
# B) Quantos produtos custam mais de R$ 1000;
# C) Qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
barato = ' '
while True:
    nomeproduto = str(input('Digite o nome do produto: ')).strip().capitalize()
    preço = float(input('Digite o valor do produto R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nomeproduto
    decisão = ' '
    while decisão not in 'SN':
        decisão = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if decisão == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra é R$ {total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00.')
print(f'O produto mais barato foi a/o {barato} e custa R$ {menor:.2f}')
