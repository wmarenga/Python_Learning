"""
Módulos padrão do Python:

Módulos são arquivos .py que contém códigos Python e servem para expandir
as funcionalidades padrão da linguagem.

Veja todos os módulos padrão em Python na documentação abaixo:
https://docs.python.org/3/py-modindex.html

import sys  # todo o módulo
print(sys.platform)  # win32 (sistema operacional)

# from sys import platform  # um objeto do módulo
# print(platform)  # não precisa usar o sys

# Exemplo criando um apelido
from sys import platform as plat

print(plat)

# Exemplo com random

import random
for i in range(10):
    print(random.randint(0, 10))

from random import randint
for i in range(10):
    print(randint(0, 10))

# Exemplo re-escrevendo um módulo
from random import randint as ri_orig


def randint(*args):
    return 'hahaha'


for i in range(10):
    print(ri_orig(0, 10))

print(randint())

# Exemplo importando tudo

from random import *

for i in range(10):
    print(randint(0, 10))

# Exemplo importando mais objetos
# A função random.random gera um número aleatório entre 0 e 1 (float)

from random import randint, random

for i in range(10):
    print(randint(0, 10), random())

# Instalando módulo não nativos do Python
# pip install mysqlclient
import pymysql

# Desinstalando um módulo
# pip uninstall pymysql
"""
