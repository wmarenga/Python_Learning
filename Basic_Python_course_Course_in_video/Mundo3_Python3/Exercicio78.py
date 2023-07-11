# Desafio 78:
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas
# respectivas POSIÇÕES na lista.

valor = []
maior = 0
menor = 0
for pos in range(0, 5):
    valor.append(int(input(f'Digite um número para a posição {pos}: ')))
# Solução do curso:
    if pos == 0:
        maior = menor = valor[pos]
    else:
        if valor[pos] > maior:
            maior = valor[pos]
        if valor[pos] < menor:
            menor = valor[pos]
# Minha solução para encontrar o maior e menor valores:
# valor.sort()
# print(f'O menor valor é {valor[0]}')
# print(f'O maior valor é {valor[len(valor)-1]}')

print('-=' * 40)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi: {maior} nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}...', end='')
print()
