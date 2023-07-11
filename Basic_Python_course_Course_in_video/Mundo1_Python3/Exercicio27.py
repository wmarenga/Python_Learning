# Desafio 27:
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
# primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro nome = Ana
# Último nome = Souza

nome = str(input('Digite seu nome completo: ')).strip().title()
separado = nome.split()
print('O seu primeiro nome é {}'.format(separado[0]))
print('O seu último nome é {}'.format(separado[len(separado) - 1]))
