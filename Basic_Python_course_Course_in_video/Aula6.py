"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma vale ', s)

Sintaxe nova do Python3:
print('A soma vale {} '.format(s))

# Sem declarar o valor será "str"
n1 = input('Digite um valor: ')
print(type(n1))

# Após declarar como inteiro será alterado o tipo.
n1 = int(input('Digite um valor: '))
print(type(n1))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# Print('A soma entre ', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

n = float(input('Digite um valor: '))
print(type(n))
print(n)

# Booleano
n = input('Digite algo: ')
print(n.isnumeric()) # somente números
print(n.isalpha()) # somente letras
print(n.isalnum()) # letras e números

# Desafio 3 (Refazendo):
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma de {} e {} é {}'.format(n1, n2, s))

# Desafio 4:
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
"""
