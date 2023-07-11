# Desafio 22:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas;
# 2) O nome com todas minúsculas;
# 3) Quantas letras ao todo (sem considerar espaços);
# 4) Quantas letras tem o primeiro nome.

nome = str(input('Escreva o seu nome: ')).strip()
print('Olhe o seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Olhe o seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras, sem espaços.'.format(
    len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
# Outra maneira:
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras.'.format(
    separa[0], len(separa[0])))
