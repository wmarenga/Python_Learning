# Desafio 84:
# Faça um programa que leia o nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) Uma listagem com as pessoas mais pesadas;
# C) Uma listagem com as pessoas mais leves.

cadastro = []
dados = []
decisão = 'S'
maior = menor = 0
cont = 0
while True:
    while decisão == 'S':
        dados.append(str(input('Qual o seu nome? ')).strip().capitalize())
        dados.append(float(input('Qual o seu peso? ')))
        if len(cadastro) == 0:
            maior = menor = dados[1]
        else:
            if dados[1] > maior:
                maior = dados[1]
            if dados[1] < menor:
                menor = dados[1]
        cadastro.append(dados.copy())
        # cadastro.append(dados[:]) - outra maneira de fazer.
        dados.clear()
        cont += 1
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()
    if decisão == 'N':
        break
    if decisão != 'SN':
        decisão = str(
            input('Digite uma opção válida! [S/N]: ')).strip().upper()
print('-='*40)
print(f'Ao todo, você cadastrou {cont} pessoas. ')
# print(f'Ao todo, você cadastrou {len(cadastro)} pessoas.') - outra
# maneira de fazer sem o contador.
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
