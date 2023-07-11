# Desafio 92:
# Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-os (com idade) em um dicionário. Se por acaso
# a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import datetime

cadastro = dict()
cadastro['nome'] = str(input('Digite o nome: ')).strip().capitalize()
cadastro['ano de nascimento'] = int(input('Digite o ano de nascimento: '))
cadastro['carteira de trabalho'] = int(
    input('Digite o número da Carteira de Trabalho [0 => não tem]: '))
if cadastro['carteira de trabalho'] != 0:
    cadastro['Ano de Contratação'] = int(
        input('Digite o ano de contratação: '))
    cadastro['Salário'] = float(input('Digite o salário €'))
    # Outra maneira de pegar a data atual.
# anoatual = int(datetime.now().strftime('%Y'))
anoatual = int(datetime.now().year)
cadastro['idade'] = anoatual - cadastro['ano de nascimento']
cadastro['aposentadoria'] = (
    cadastro['Ano de Contratação'] + 35) - cadastro['ano de nascimento']
print('-~'*30)
for k, v in cadastro.items():
    print(f'O(a) seu(sua) {k} é {v};')
