""" 
Trabalhando com modulos Built-In (modulos integrados, que ja vem instalados no Python)
_________________________
|Python |Modulos builtin|
-------------------------

Documentacao:

https://docs.python.org/3/py-modindex.html

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__']

import random
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__', 'random']

# Apos importar o random, ele passa a fazer parte das bibliotecas que poderao ser utilizadas

# Utilizando alias (apelido) para modulos/ funcoes
import random as rdm

print(rdm.random())

# Podemos importar todas as funcoes de um modulo utilizando o *

from random import *

print(random())

# Importando todo o modulo
import random

print(random.random())

# Utilizando alias (apelido) para modulos/ funcoes

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

# Costumamos utilizar tuple para colocar multiplos imports de um mesmo modulo
from random import (random, randint, shuffle, choice)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))

"""

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

# Costumamos utilizar tuple para colocar multiplos imports de um mesmo modulo
from random import (random, randint, shuffle, choice)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))