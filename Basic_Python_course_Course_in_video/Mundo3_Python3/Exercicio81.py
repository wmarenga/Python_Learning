# Desafio 81:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados;
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
num = []
cont = 0
decisão = 'S'
while True:
    while decisão in 'S':
        num.append(int(input('Digite um valor: ')))
        cont += 1
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()
    if decisão == 'N':
        break
    if decisão != 'SN':
        decisão = str(
            input('Digite uma opção válida! [S/N]: ')).strip().upper()
if 5 in num:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')
print(f'Foram digitados {cont} números.')
num.sort(reverse=True)
print('A ordem decrescente da lista é {}'.format(num))
