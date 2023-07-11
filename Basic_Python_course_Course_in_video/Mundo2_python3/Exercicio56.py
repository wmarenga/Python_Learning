# Desafio 56:
# Desenvolva um programa que leia o NOME, IDADE e SEXO de
# 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('-'*5, end='')
    print(' {}ᵃ PESSOA '.format(p), end='')
    print('-'*5)
    nome = str(input('Digite o {}ᵃ nome: '.format(p))).strip().lower()
    idade = int(input('Digite a {}ᵃ idade: '.format(p)))
    sexo = str(
        input('Digite o sexo da {}ᵃ pessoa [M/F]: '.format(p))).strip().lower()
    somaidade += idade
    if p == 1 and sexo == 'm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'f' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(
    maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
