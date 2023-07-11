# Desafio 95:
# Aprimore o desafio 93 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

dados = dict()
gols = []
time = []
total = 0
while True:
    dados['jogador'] = str(
        input('Digite o nome do jogador: ')).strip().capitalize()
    partidas = int(
        input(f'Digite quantas partidas {dados["jogador"]} jogou? '))

    for p in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
        total = sum(gols)
    dados['gols'] = gols.copy()
    gols.clear()
    dados['total'] = total
    time.append(dados.copy())
    decisão = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while decisão not in 'SsNn':
        print('ERRO! Por favor digite S => Sim ou N => Não.')
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if decisão in 'Ss':
            break
    if decisão in 'Nn':
        break
# VALIDAÇÃO E APRESENTAÇÃO DOS DADOS:
print('-~'*20)
print('Cod  ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-~'*20)
for k, v in enumerate(time):
    print(f'{k:^5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-~'*20)

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (9999 para parar) '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print(f'ERRO! Não existe jogador com o código {mostrar}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[mostrar]["jogador"]}')
        for i, g in enumerate(time[mostrar]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print()
print('<< VOLTE SEMPRE >>')
print()
