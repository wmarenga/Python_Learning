"""
print('Olá' + 5) # can only concatenate str (not "int") to str

# Atenção: No Python toda variável é um objeto.

'''Usamos o input para o usuário inserir dados'''
nome = input('Qual é o seu nome?')
idade = input('Qual é a sua idade?')
peso = input('Qual é o seu peso?')
print(nome, idade, peso)

nome = 'Wellington'
idade = 49
peso = 72
'''Usamos vírgula para separar as variáveis (str, int, int)'''
print(nome, idade, peso)
'''Não podemos usar o sinal de adição para variáveis mistas'''
print(nome+ idade + peso)
'''(str + str) - OK'''
print('Wellington'+ 'Marenga')
'''(int+ int) - OK'''
print(7+4)
'''(str+ int) - Erro (can only concatenate str (not "int") to str)
print('Olá', 5) # Se quisermos unir uma string com um número, devemos utilizar vírgula.
"""
'''
Desafio 1: 
nome = input('Qual o seu nome? ')
print('Olá', nome, '! Prazer em te conhecer!')

'''
'''
Desafio 2:
dia_nascimento = input('Em que dia você nasceu? ')
mes_nascimento = input('Em que mês você nasceu? ')
ano_nascimento = input('Em que ano você nasceu? ')
print('Você nasceu no dia ', dia_nascimento, 'de ', mes_nascimento, 'de ', ano_nascimento, '. Correto?')

'''
'''
Desafio 3:
Temos que determinar o tipo de variável que será inserido.
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
print('A Soma é', num1+num2)

'''
