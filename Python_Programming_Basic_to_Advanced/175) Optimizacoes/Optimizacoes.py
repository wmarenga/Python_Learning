import sys
import collections
from timeit import timeit

# Forma rápida de criar classes.
Pessoa = collections.namedtuple('Pessoa', 'nome email')
felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')
print(timeit('felicity.email', globals=globals()))
# 0.09260549998725764
# Percebeu-se uma melhoria de performance, em relação ao Python 3.7.9

# Dentro de globals(), ficam armazenados os objetos utilizados.
print(globals())

# Outro Exemplo:

# Quantos bites foram necessários para gerar a lista (232656216 bites).
print(sys.getsizeof(list(range(29082020))))
