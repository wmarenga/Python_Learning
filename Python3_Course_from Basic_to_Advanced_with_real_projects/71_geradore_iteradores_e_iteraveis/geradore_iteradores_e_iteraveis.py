"""
Geradore, Iteradores e Iteraveis:

lista = [0, 1, 2, 3, 4, 5]
lista1 = 1234
lista2 = 'String'

# Para verificar se o objeto é iterável
print(hasattr(lista, '__iter__'))  # True
print(hasattr(lista1, '__iter__'))  # False
print(hasattr(lista2, '__iter__'))  # True

# Transforma a lista em um iterador para exibirmos os elementos da
# lista
for v in lista:
    print(v)

lista = [0, 1, 2, 3, 4, 5]
lista1 = 1234
lista2 = 'String'

# Tornando um objeto iterador

print(hasattr(lista, '__next__'))  # False (não é um iterador)
lista = iter(lista)
# Criamos o método __next__
print(hasattr(lista, '__next__'))  # True (não é um iterador)

print(next(lista))  # 0
print(next(lista))  # 1
print(next(lista))  # 2
print(next(lista))  # 3
print(next(lista))  # 4
print(next(lista))  # 5

# Geradores
# Utilizamos os geradores para otimizar a alocaçao de meméria
import sys
import time

lista = list(range(10))  # 136 bites
# lista = list(range(100))  # 856 bites
# lista = list(range(1000))  # 8056 bites (8Kb)
# lista = list(range(10000))  # 80056 bites (80Kb)

# Verifica quanta memória está sendo usada para lista
print(sys.getsizeof(lista))


# Espera pelo preenchimento de toda a lista e depois mostra
def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r


g = gera()

for v in g:
    print(v)

# Agora usando geradores
# O gerador irá retornar um valor de cada vez se esperar todos os
# valores serem carregados.
import time


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

for v in g:
    print(v)  # Mostra o que estã sendo executado no exato momento

print(hasattr(g, '__iter__'))  # Geradores são iteráveis
print(hasattr(g, '__next__'))  # Geradores são iteradores

print(next(g))
print(next(g))
print(next(g))

# Outro exemplo:


def gera1():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


g1 = gera1()
print(next(g1))  # Valor 1
print(next(g1))  # Valor 2
print(next(g1))  # Valor 3
print(next(g1))  # StopIteration
"""
import sys

lista = [x for x in range(1000)]
print(type(lista))  # <class 'list'>
print(sys.getsizeof(lista))  # 8856 bites

# Somente trocando os colchetes pelos parênteses
gerador = (x for x in range(1000))
print(type(gerador))  # <class 'generator'>
print(sys.getsizeof(gerador))  # 104 bites

# Alterando de 1000 para 100000
lista = [x for x in range(100000)]
print(type(lista))  # <class 'list'>
print(sys.getsizeof(lista))  # 800984 bites

# Somente trocando os colchetes pelos parênteses
gerador = (x for x in range(100000))
print(type(gerador))  # <class 'generator'>
print(sys.getsizeof(gerador))  # 104 bites
