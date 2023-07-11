# Desafio 25:
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite seu nome: ')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in nome))
