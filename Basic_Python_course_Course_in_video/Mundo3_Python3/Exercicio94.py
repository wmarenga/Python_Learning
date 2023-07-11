# Desafio 94:
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoa foram cadastradas;
# B) A média de idade;
# C) Uma lista com as mulheres;
# D) Uma lista de pessoas com idade acima da média.

dados = dict()
cadastro = list()
soma = 0
média = 0
while True:
    dados['nome'] = str(input('Digite o seu nome: ')).strip().capitalize()
    dados['sexo'] = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    while dados['sexo'] not in 'MmFf':
        print('ERRO! Por favor digite novamente M ou F.')
        dados['sexo'] = str(
            input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MmFf':
            break
    dados['idade'] = int(input('Digite a sua idade: '))
    soma += dados['idade']
    cadastro.append(dados.copy())
    dados.clear()
    decisão = str(input('Quer continuar? [S/N] ')).strip().upper()
    while decisão not in 'SsNn':
        print('ERRO! Por favor digite S => Sim ou N => Não.')
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()
        if decisão in 'Ss':
            break
    if decisão in 'Nn':
        break
# ANÁLISE DOS RESULTADOS:
print('-~'*30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
média = soma / len(cadastro)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média de idade: ')
for p in cadastro:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} => {v}; ', end='')
        print()
print('<< ENCERRADO >>')
