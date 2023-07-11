# Desafio 13:
# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Digite o seu salário atual: R$ '))
novo_salário = salário * 1.15
print('Um funcionário que ganha um salário de R$ {:.2f}, com acrescido de 15% irá ganhar R$ {:.2f}'.format(
    salário, novo_salário))
