"""
Entrada de dados:

Sempre retornará uma str:

from datetime import datetime

nome = input("Qual o seu nome? ")
print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}.\n')

idade = input("Qual a sua idade? ")
print(f'{nome} tem idade {idade} anos.')

# Fazer a conversão de idade com Type Cast (casting):
ano_nascimento = datetime.now().year - int(idade)
print(f'Você nasceu em {ano_nascimento}.')

# Exemplo de calculadora para fazer somente soma:

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

Outra Opção:
numero_2 = int(numero_2)

print(numero_1 + numero_2)

Obs: Se convertermos a soma dos caractéres, estaríamos obtendo o
resultado da concatenação convertido para um inteiro.

print(int(numero_1 + numero_2))
"""
