"""
AULA 4 - COMANDOS BÁSICOS:

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

x = 'Curso de Python no cursoemvideo'
print(x[1:5])
"""
