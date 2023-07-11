"""
Funções com Retorno

numeros = [1, 2, 3]
print(numeros)

ret_pop = numeros.pop()  # Remove o último elemento de uma lista.
print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

Obs: Em Python, quando uma função não retorna nenhum valor, o retorno é "None".

Obs: Funcoes em Python que retornam valores, devem retornar estes valores com a
palavra reservada (return).

Obs: Nao precisamos necessariamente criar uma variavel para receber o retorno de
uma funcao. Podemos passar a execucao da funcao para outras funcoes ou mesmo para
outras funcoes.

# Exemplo função

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()
print(f'Retorno {ret}')  # None.

# Vamos refatorar (reescrever, modificar) esta função para que ela retorne o valor.

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função.
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7() + 1}')  
# Simplificado em uma linha, podendo usar operações matemáticas.

# Refatorando a primeira função.
def diz_oi():
    return 'Oi '  # Retorna um resultado (número, string, etc)

print(diz_oi())

alguem = 'Pedro!'

print(diz_oi() + alguem)

Obs: Sobre a palavra reservada "return".

# Exemplo 1 (Ela finaliza a função, ou seja, ela sai da execução da função):

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi! '
    print('Estou sendo executado após o retorno...') # Nao sera executada apos o return


print(diz_oi())

# Exemplo 2 (Podemos ter, em uma função, diferentes "returns"):

def nova_funcao():
    variavel = False
    if variavel:
        return 4 # Se True.
    elif variavel is None:
        return 3.2 # Se None.
    return 'b' # Se False


print(nova_funcao())

# Exemplo 3 (Podemos, em uma função, retornar qualquer tipo de dado até mesmo múltiplos valores.):

def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao() # Desempacotando os elementos.
print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda.

from random import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1.
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação 
desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False #tendo somente duas opções não é necessário utilizar o "else".


print(eh_impar())
"""