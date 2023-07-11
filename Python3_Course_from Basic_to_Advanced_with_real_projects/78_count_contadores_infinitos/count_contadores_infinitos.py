"""
count - Itertools (retorna um iterador):
Gera a função next

# Exemplo para saber se é um gerador
from types import GeneratorType
variavel = zip('Alo', 'Alo')
print(isinstance(variavel, GeneratorType))  # False (não é um gerador)

# Para converter para um gerador (com list Comprehension)

variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType))  # True (Agora é um gerador)

from itertools import count
contador = count()

print(next(count()))
print(next(count()))
print(next(count()))

# Loop infinito
for valor in contador:
    print(valor)

# O contador tem definição de início

from itertools import count
contador = count(start=5, step=0.05)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break
        
# Contagem regressiva

from itertools import count
contador = count(start=9, step=-1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break     
"""

# Gerando um índice para cada elemento da lista
from itertools import count

contador = count()
# Irá adicionar novos índice para novos elementos adicionados (automaticamente).
lista = ['Luiz', 'João', 'Maria', 'José']
lista = zip(contador, lista)
print(list(lista))
