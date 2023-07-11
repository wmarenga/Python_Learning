# Desafio 4:
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
# primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(x))
print('O tipo primitivo desse valor é {}'.format(type(x)))
print('É um número? ', x.isnumeric())
print('{} é um número? {}'.format(x, x.isnumeric()))
print('É alfanumérico? ', x.isalnum())
print('{} é alfanumérico? {}'.format(x, x.isalnum()))
print('É alfabético? ', x.isalpha())
print('{} é alfabético? {}'.format(x, x.isalpha()))
print('Está capitalizada? ', x.istitle())
print('{} está capitalizada? {}'.format(x, x.istitle()))
print('Está em minúsculas? ', x.islower())
print('{} está em minúsculas? {}'.format(x, x.islower()))
print('Está em maiúsculas? ', x.isupper())
print('{} está em maiúsculas? {}'.format(x, x.isupper()))
print('Só tem espaço? ', x.isspace())
print('{} só tem espaço? {}'.format(x, x.isspace()))
