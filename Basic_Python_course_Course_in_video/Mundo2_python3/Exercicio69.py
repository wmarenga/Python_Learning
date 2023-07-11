# Desafio 69:
# Crie um programa que leia a IDADE e o SEXO de várias
# pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final,
# mostre:
# A) quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados;
# C) Quantas mulheres tem menos de 20 anos.

idademaior = sexom = mulhermenos20 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if idade >= 18:
        idademaior += 1
    if sexo == 'M':
        sexom += 1
    if sexo in 'F' and idade < 20:
        mulhermenos20 += 1
    if resp == 'N':
        break
print('ACABOU!')
print(f'O total de pessoas com mais de 18 anos é {idademaior}.')
print(f'O total de homens é {sexom}.')
print(f'O total de mulheres com menos de 20 anos é {mulhermenos20}')
