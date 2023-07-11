"""
Teste de Velocidade com Expressoes Geradoras:

# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

# <generator object nums at 0x000001EDFE381F50>
# <class 'generator'>
print(ge1)  # Generator
print(type(ge1))  # Generator

print(next(ge1))  # 1
print(next(ge1))  # 2
print(next(ge1))  # 3
print(next(ge1))  # 4

# Generator Expression:

ge2 = (num for num in range(1, 10))

# <generator object <genexpr> at 0x000001EDFE381D90>
# <class 'generator'>
print(ge2)  # Generation Expression <genexpr>
print(type(ge2))  # Generation Expression

print(next(ge2))  # 1
print(next(ge2))  # 2
print(next(ge2))  # 3
print(next(ge2))  # 4

# Podemos também várias funções integradas do Python
print(sum(num for num in range(1, 10)))

"""

# Realizando o teste de velocidade
import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhões
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
