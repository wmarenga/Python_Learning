"""
Documentação:
https://docs.python.org/3/tutorial/modules.html

# Importa tudo dentro de calculos

import calculos

print(__name__)  # para o sistema o nome deste módulo é __main__
print(calculos.PI)

lista = [2, 4]
print(calculos.multiplica(lista))

# Importando somente a função multiplica
from calculos import multiplica
print(multiplica([2, 4]))

"""

from calculos import multiplica, dobra_lista, PI
from outro import fala_oi

print(multiplica([2, 4]))
fala_oi()


print(PI)

lista = [2, 4, 5, 6, 7]
nova_lista = []
print(dobra_lista(lista))

for i in dobra_lista(lista):
    nova_lista.append(i * PI)
print(nova_lista)
