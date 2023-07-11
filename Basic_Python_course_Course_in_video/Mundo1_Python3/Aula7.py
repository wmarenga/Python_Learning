"""
AULA 7 - OPERADORES ARITMÉTICOS:

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))  # Alinhado a esquerda.
print('Prazer em te conhecer {:>20}!'.format(nome))  # Alinhado a direita.
print('Prazer em te conhecer {:^20}!'.format(nome))  # Alinhado ao centro.
# Alinhado ao centro acrescentando caracteres.
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# O resultado poderá ser limitado em casas decimais utilizando :.3f, onde f = float.
# Adicionando o \n, conseguimos fazer a quebra de linha.
print('A soma é {},\no produto é {},\na divisão é {:.3f},\na divisão inteira é {},\ne o expoente é {}'.format(s, m, d, di, e))

# Utilizando o " end='' ", podemos mostrar os resultados de 2 prints em uma linha.

print('A soma é {}, o produto é {}, a divisão é {:.3f},'.format(s, m, d), end=' ')
print('a divisão inteira é {}, o expoente é {}'.format(di, e))

"""
