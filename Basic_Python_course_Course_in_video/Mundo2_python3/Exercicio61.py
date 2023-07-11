# Desafio 61:
# Refaça o DESAFIO 51, lendo o primeiro termo e a
# razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura WHILE.

print('='*10)
nome = 'GERADOR DE PA'
print('{:^30}'.format(nome))
print('='*10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('ACABOU')
