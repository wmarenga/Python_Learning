"""
Comportamento de Geradores e Iteradores

# list, tuple, str => Sequences => Iteráveis
nome = 'Luiz Otávio'

for letra in nome:
    print(letra)

print('#' * 80)

for letra in nome:
    print(letra)
"""
# Ao contrário de um iterável o gerador executa até o final e acabou
# Geradores são iteráveis e são também iteradores
nome = 'Luiz Otávio'
iterador = iter(nome)
gerador = (letra for letra in nome)

# Exemplo com gerador:

print(next(gerador))  # L
print(next(gerador))  # u
print(next(gerador))  # i
print(next(gerador))  # z

# A partir daqui ele irá consumir o restante do gerador (com for)
print('Consumindo o restante com for:')

for letra in gerador:
    print(letra)

print('Olha o outro for sem valor: ')

for letra in gerador:
    print(letra)
print('############################')
"""
Exemplo com iterador:

try:
    print(next(iterador))  # L
    print(next(iterador))  # u
    print(next(iterador))  # i
    print(next(iterador))  # z
    print(next(iterador))  # espaço
    print(next(iterador))  # O
    print(next(iterador))  # t
    print(next(iterador))  # á
    print(next(iterador))  # v
    print(next(iterador))  # i
    print(next(iterador))  # o
    print(next(iterador))  # StopIteration
except:
    pass

print(next(iterador))  # StopIteration

# Esgotamos todas as iterações (todas as iterações foram utilizadas).
"""
