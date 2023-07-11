# Desafio 55:
# Faça um programa que leia o peso de CINCO PESSOAS. No
# final, mostre qual foi o maior e o menor peso lido.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ᵃ pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de \033[32m{:.1f} Kg\033[m.'.format(maior))
print('O menor peso lido foi de \033[32m{:.1f} Kg\033[m.'.format(menor))
