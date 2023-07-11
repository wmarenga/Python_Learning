'''
Módulos:

O que é?

Módulos são arquivos Python (extensão .py) que contém conjuntos de funções, objetos, variáveis, entre outros.
Essas funcionalidades podem ser chamadas das seguintes maneiras:

import Nome_do_modulo
import Nome_do_modulo as abreviação
from Nome_do_modulo import algum_objeto

Referência

Lista de módulos do Python: https://docs.python.org/3.8/py-modindex.html

import numpy

Retorna o valor de pi
a = numpy.pi
print(a)

Retorna o valor do cosseno
b = numpy.cos(0)
print(b)

Usando uma abreviacao
import numpy as np 
a = np.pi
print(a)
b = np.cos(0)
print(b)

importando funcionalidade especificas de uma biblioteca
from numpy import pi, cos

a = pi
print(a)
a = cos(0)
print(a)

Criando um modulo com uma funcao dentro (em outro arquivo)

def media_2(n1, n2):
    media = (n1 + n2)/ 2
    return media
g = 9.8

Importando do meu codigo
import media

a = 5
b = 10

print(media.media_2(a, b))

Usando abreviacao do modulo

import media as md

a = 5
b = 10

print(md.media_2(a, b))

Importando os objetos diretamente

from media import g

print(g)

'''