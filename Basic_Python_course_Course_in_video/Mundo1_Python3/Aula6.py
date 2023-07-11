"""
AULA 6 - TIPOS PRIMITIVOS E SAÍDA DE DADOS:

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
"""
