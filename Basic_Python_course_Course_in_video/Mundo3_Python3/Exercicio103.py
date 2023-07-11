# Desafio 103:
# Faça um programa que tenha uma função chamada ficha(), que receba 2
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} marcou {gol} gols no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
