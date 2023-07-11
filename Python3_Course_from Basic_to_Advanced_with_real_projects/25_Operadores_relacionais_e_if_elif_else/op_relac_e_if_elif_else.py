"""
Operadores Relacionais:

== (igualdade)
!= (diferente)
>  (maior que)
>= (maior ou igual a)
<  (menor que)
<= (menor ou igual a)

print(2 == 2)  # True
print(2 != 2)  # False

num_1 = 2  # int
num_2 = '2'  # str

# Visualmente são iguais, porém num_1 é um int e num_2 é str.
print(num_1, num_2)

print(num_1 == num_2)  # False

num_3 = 3
num_4 = 4

expressao = num_3 <= num_4
print(expressao)

var_1 = 'Luiz'
var_2 = 'Otávio'

expressao_2 = (var_1 != var_2)
print(expressao_2)

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
idade_menor = 20  # Muito jovem
idade_maior = 30  # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

"""
