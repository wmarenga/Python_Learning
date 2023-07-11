"""
Trabalhando com Cores:

# Pesquisar o módulo colorize.

\033[0:33;44 m]
0  -> style
33 -> text
44 -> background

style
0 -> none
1 -> negrito
4 -> underline
7 -> negative

text
30 -> branco
31 -> vermelho
32 -> verde
33 -> amarelo
34 -> azul
35 -> roxo
36 -> azul claro
37 -> cinza

background
40 -> fundo branco
41 -> fundo vermelho
42 -> fundo verde
43 -> fundo amarelo
44 -> fundo azul
45 -> fundo roxo
46 -> fundo azul claro
47 -> fundo cinza

print('\033[1;31;43mOlá Mundo!\033[m')  # letra vermelha.
print('\033[4;;45mOlá Mundo!\033[m')  # letra branca com fundo roxo.
print('\033[0;33;44mOlá Mundo!\033[m')  # letra amarela com fundo azul.
print('\033[7;33;44mOlá Mundo!\033[m')  # letra azul com fundo amarelo.

a = 3
b = 5
print(
    'Os valores são \033[2;33;45m{}\033[m e \033[2;34;43m{}\033[m'.format(a, b))

# Inserindo as cores dentro do format.
nome = 'Wellington'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(
    '\033[1;33;44m', nome, '\033[m'))

nome = 'Wellington'
cores = {'limpa': '\033[m', 'azul': '\033[34m',
         'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(
    cores['azul'], nome, cores['limpa']))

# Criando um dicionário de código de cores:

nome = 'Wellington'
cores = {'limpa': '\033[m', 'azul': '\033[34m',
         'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(
    cores['azul'], nome, cores['limpa']))
print(type(cores))

"""


