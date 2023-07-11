# Desafio 12:
# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: R$ '))
novo_preço = preço * 0.95
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% custará R$ {:.2f}'.format(
    preço, novo_preço))
