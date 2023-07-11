# Desafio 93:
# Crie um programa que gerencie o aproveitamento de um jogodor de
# futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total
# de gols feitos durante o campeonato.

dados = dict()
gols = []
dados['jogador'] = str(
    input('Digite o nome do jogador: ')).strip().capitalize()
partidas = int(
    input(f'Digite quantas partidas {dados["jogador"]} jogou? '))
for p in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
dados['gols'] = gols
dados['total'] = sum(gols)
print('-~'*30)
print(dados)
print('-~'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-~'*30)
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for i, g in enumerate(dados['gols']):
    print(f'   => Na {i+1}ª partida, fez {g} gols')
print(f'Foi um total de {dados["total"]} gols.')
