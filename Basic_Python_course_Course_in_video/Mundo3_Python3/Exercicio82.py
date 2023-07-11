# Desafio 82:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso , crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.

total = list()
par = list()
ímpar = list()
decisão = 'S'
while True:
    while decisão == 'S':
        num = int(input('Digite um número: '))
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()
        total.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            ímpar.append(num)
    if decisão == 'N':
        break
    if decisão != 'SN':
        decisão = str(
            input('Digite uma opção válida! [S/N]: ')).strip().upper()
print(f'A lista completa é {total}')
print(f'A lista de números pares é {par}')
print(f'A lista de números ímpares é {ímpar}')
