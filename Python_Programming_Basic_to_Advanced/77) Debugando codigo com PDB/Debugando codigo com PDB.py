""" 
Debugando codigo com PDB:

PDB => Python Debugger (Retirar problemas de codigos)

Bug => Inseto (A palavra debug nasceu de um problema em computadores antigos, onde um inseto 
entrou na sala de computadores e precisaram retirar o inseto que estava provocando problemas)

# Obs: A utilizacao dp rint() para debugar codigo e uma pratica ruim.

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err: # Podemos passar uma tupla com varios erros possiveis 
                                                    # e criar uma apelido para ver a descricao do erro.
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger.
# Em Python, podemos fazeer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB (Python Debogger).

# Exemplo com o PyCharm:

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err: # Podemos passar uma tupla com varios erros possiveis 
                                                    # e criar uma apelido para ver a descricao do erro.
        return f'Ocorreu um problema: {err}'

print(dividir(4, 0))

# Exemplo 1 com o PDB - Python Debugger

# Para utilizarmos o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a funcao
# set_trace()

# A partir do Python 3.7, nao e mais necessario importar a biblioteca pdb, pois o comando de
# debug foi incorporado como funcao built-in (integrada) chamada breakpoint().

# Comandos basicos do PDB 
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace() # Break point
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)

# Exemplo 2 com o PDB - Python Debugger

# Para utilizarmos o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a funcao
# set_trace()

# A partir do Python 3.7, nao e mais necessario importar a biblioteca pdb, pois o comando de
# debug foi incorporado como funcao built-in (integrada) chamada breakpoint().

# Comandos basicos do PDB 
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace() # Break point
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)

# Porque utilizar este formato?
# O debug e utilizado durante o desenvolvimento. Costumamos realizar todos os imports
#  de bibliotecas no inicio do arquivo. Por isso, ao inves de colocarmos o import do 
# pdb no inicio do arquivo, nos colocamos somente onde vamos debugar, e ao finalizar ja
# fazemos a remocao.

# Exemplo 3 com o PDB - Python Debugger

# A partir do Python 3.7, nao e mais necessario importar a biblioteca pdb, pois o comando de
# debug foi incorporado como funcao built-in (integrada) chamada breakpoint().

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)

# Obs: Cuidado com conflitos entre nomes de variaveis e os nomes do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Como os nomes das variaveis sao os nomes dos comandos do pdb:
# Se quisermos exibir as variaveis mesmo com o conflito, nos incluimos o 'p' antes do nome 
# da variavel 'p n', 'p l', 'p c'

# Afim de evitar conflitos e falta de entendimento do codigo, nada de colocar nomes nao
# representativos em variaveis. Sempre optar por nomes significativos (num1, nome, idade, etc)

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""
