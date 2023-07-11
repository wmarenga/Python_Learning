"""
Formatando valores com modificadores:

:s - Texto (str);
Exemplo:
nome = 'Luiz Otávio'
print(f'{nome:s}')

:d - Inteiros (int);
Exemplo:
idade = 51
print(f'{idade:d}')

:f - Números de ponto flutuante (float);
Exemplo:
salario = 1200.34
print(f'{salario:f}')

:. (NÚMERO)f - Quantidade de casas decimais (float);
Exemplos:
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(divisao)

# Usando .format()
print('{:.2f}'.format(divisao))

# Usando com f-strings
print(f'{divisao:.2f}')

: (CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f).
Exemplo:
num_1 = 1
print(f'{num_1:0>10}')  # Serão adicionados 9 zeros.

num_2 = 1150
print(f'{num_2:0>10}')  # Serão adicionados 6 zeros, pois já temos 4 números.

num_3 = 9999
print(f'{num_3:0^11}')  # Serão adicionados 3 zeros a esquerda e 4 a direita.

> - Esquerda
< - Direita
^ - Centro

# Combinado
# Exemplo:
num_4 = 1150
print(f'{num_4:0>10.2f}')

# Podemos usar com str também

nome = 'Otávio Miranda'
print(len(nome))
print(50 - len(nome))  # Deixar a minha str com 50 caractéres.

print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome)

# Não adicionada nada, pois já é a quantidade de caractéres da str.
nome_formatado2 = '{:@>14}'.format(nome)
print(nome_formatado)
print(nome_formatado2)

# Nomeado
nome_formatado3 = '{n:0<20}'.format(n=nome)
print(nome_formatado3)

# Utilizando índices em uma str
nome = 'Wellington'
sobrenome = 'Marenga'
nome_formatado5 = '{0:-^50}\n''{1:+^50}'.format(nome, sobrenome)
#nome_formatado6 = '{1:+^50}'.format(nome, sobrenome)
print(nome_formatado5)
# rint(nome_formatado6)

# Utilizando funções de str

# Justifica a esquerda
nome = 'welLiNgton'
# nome = nome.ljust(20, '#')
print(nome)

# Justifica a direita
nome2 = 'Marenga'
nome2 = nome2.rjust(20, '*')
print(nome2)

# Justifica ao centro
nome3 = 'Junior'
nome3 = nome3.center(20, '@')
print(nome3)

print(nome.lower())  # tudo minúsculo
print(nome.upper())  # tudo maiúsculo
print(nome.title())  # primeiras letras maiúsculas

"""
