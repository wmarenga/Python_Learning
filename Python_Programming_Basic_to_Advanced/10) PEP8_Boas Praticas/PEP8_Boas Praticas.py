"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

cmd: import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] Utilize Camel Case para nomes de classes;

[2] Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_dois():
    pass


numero = 4


numero_impar = 5

[3] Utilize 4 espaços para identação! ## NÃO USE A TECLA TAB ##;

if 'a' in 'banana':
    print('tem') - 4 espaços
[4] Linhas em branco:
- Separar funções e definições de classes com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com ma única linha em branco;

## 2 linhas ##
class Classe:
    pass
## 2 linhas ##

[5] Imports:
- Imports devem ser sempre feitos em linhas separadas;

# Import ERRADO #
import sys, os

# Import Certo #
import sys
import os

# Não há problemas em utilizar: #
from types import StringType, ListType

# Caso tenhamos muitos imports de um mesmo pacote, recomenda-se fazer: #
from types import (StringType, ListType, SetType, OutroType)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
antes de constantes ou variáveis globais. #

[6] Espaços em expressões e instruções;

# Não faça!: #
funcao( algo[ 1 ], { outro: 2 } )
algo (1)
dict [ 'chave' ] = list [indice]
x          = 1
y          = 3
variavel_longa         = 5

# Faça! #
funcao(algo[1], {outro: 2})
algo(1)
dict['chave'] = lista[indice]
x = 1
y = 3
variavel_longa = 5

[7] Termine sempre uma instrução com uma nova linha vazia;

"""