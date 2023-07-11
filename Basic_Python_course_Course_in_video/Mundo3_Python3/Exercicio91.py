# Desafio 91:
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guardem esses resultados em um dicionário em Python. No
# final, coloquem este dicionário em ordem, sabendo que o vencedor tirou
# o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
jogadas = {'jogador1': randint(1, 6), 'jogador2': randint(
    1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

print('-~'*9)
print('Valores sorteados')
print('-~'*9)

# intemgetter(1), ordena pelo valor e itemgetter(0), pela chave.
# FORA DE ORDEM:
for k, v in jogadas.items():
    print(f'O {k} tirou {v} no dado!')

# Ordenando o dicionário.
print('-~'*11)
print('RANKING DOS JOGADORES')
print('-~'*11)
ranking = list()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
sleep(1)
# print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
