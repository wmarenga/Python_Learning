""" 
O Modulo random e o que sao modulos:

- Em Python, modulos nada mais sao do que outros arquivos Python.

Modulo Random => Possui varias funcoes para geracao de numeros pseudo-aleatorio (pode haver repeticoes).

# Obs: Existem duas formas de se utilizar um modulo ou funcao deste.

# Forma 1 - importando todo o modulo (Nao recomendado):

import random

# Obs: Ao realizar o import de todo o modulo, todas as funcoes, atribuidas, classes 
# e propriedades que estiverem dentro do modulo ficarao disponiveis (em memoria).
# Caso se saiba quais funcoes voce precisa utilizar deste modulo, entao esta nao
# seria a forma ideal de utilizacao. Nos veremos uma forma melhor na forma 2.

# Como saber as funcionalidades do random:
# print(dir(random))
# Gera um numero pseudo-aleatorio entre 0 e 1

# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 
# 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', 
# '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', 
# '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', 
# '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', 
# '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 
# 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 
# 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 
# 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print(random.random())

# Veja que para utilizar a funcao random() do pacote random, nos colocamos o nome do pacote
# e o nome da funcao. separados por ponto. print(nome_pacote.nome_funcao).

# Obs: Nao confunda a funcao random() com o pacote random. Pode parecer confuso, mas a funcao
# random() e apenas uma funcao dentro do modulo random.

# Forma 2 - Importando uma funcao especifica do modulo (Recomendada):

from random import random

# No import acima, estamos falando: Do modulo random, importe a funcao random.

for i in range(10):
    print(random())

# Gera 10 numeros aleatorios (entre 0 e 1).

# uniform() => Gera um numero pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # O numero 7 nao sera incluido.

# randint() =>  Gera valores pseudo-aleatorios entre os valores (inteiros) estabelecidos.

# Gerador de apostas para a mega-sena
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ') # Comeca em 1 e vai ate 60

# choice() => Mostra um valor aleatorio entre um iteravel.

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice('Geek University'))

# shuffle => Tem a funcao de embaralhar dados

from random import shuffle

cartas = ['k', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas) # Embaralhando as cartas

print(cartas)

print(cartas[0]) # Embaralhando e dando uma carta.

print(cartas.pop()) # O ideal e retirar sempre uma carta (do final), usando o pop()

"""
from random import shuffle

cartas = ['k', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas) # Embaralhando as cartas

print(cartas)