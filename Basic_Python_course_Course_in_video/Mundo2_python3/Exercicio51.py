# Desafio 51:
# Desenvolva um programa que leia o PRIMEIRO TERMO e a
# RAZÃO de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

print('='*30)
nome = '10 TERMOS DE UMA PA'
print('{:^30}'.format(nome))
print('='*30)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='→ ')
print('ACABOU')
