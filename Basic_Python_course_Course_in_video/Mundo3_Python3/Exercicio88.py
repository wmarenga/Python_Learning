# Desafio 88:
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista coposta.

from random import randint
from time import sleep
totjogos = []
jogos = []
print('-'*30)
print('       JOGO DA MEGA SENA       ')
print('-'*30)
print()
palpites = int(input('Quer palpites para quantos jogos? '))
print(f'Sorteado {palpites} jogos')

for p in range(0, palpites):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    totjogos.append(jogos.copy())
    jogos.clear()
print('-='*3, f'SORTEADO {cont} JOGOS ', '-=' * 3)
print()
for i, l in enumerate(totjogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print()
print('-='*3, '< BOA SORTE!!! >', '-='*3)
