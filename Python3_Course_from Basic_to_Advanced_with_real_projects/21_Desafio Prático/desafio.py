"""
- Criar variáveis para nome (str), idade (int), altura (float) e
peso (float) de uma pessoa;
- Criar variáveis com o ano atual (int);
- Obter o ano de nascimento da pessoa (baseado na idade e no ano
atual)
- Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa);
- Exibir um texto com todos os valores na tela usando F-strings (com
as chaves).
"""
from datetime import datetime

nome = str(input('Digite o seu nome: ')).capitalize()
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Informe o seu peso: '))
ano_atual = datetime.now().year
data_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura:.2f} m de altura e pesa {peso} Kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {data_nascimento}.')
