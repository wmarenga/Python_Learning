"""
Pacotes:

Entendendo o que são módulos e pacotes:

Módulo => É apenas um arquivo Python que pode ter diversas funções para
utilizarmos;
Pacotes => É um diretório contendo uma coleção de módulos;

Obs: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versões do Python 3,x, não é mais obrigatória a utilização deste arquivo,
mas normalmente ainda é utilizado para manter compatibilidade.

Foi criada uma pasta Geek (módulo) com um arquivo __init__.py e 2 arquivos
Geek1 e Geek2.py

Dentro da pasta Geek, foi criada outra pasta University (módulo) com um arquivo
__init__.py (dunder init) e e 2 arquivos Geek3 e Geek4.py

# Importando e utilizando os pacotes e módulos que criamos:

from Geek import geek1, geek2
from Geek.University import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4, 6))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())

from Geek.geek1 import funcao1
from Geek.University.geek4 import funcao4

print(funcao1(6, 9))
print(funcao4())
"""
