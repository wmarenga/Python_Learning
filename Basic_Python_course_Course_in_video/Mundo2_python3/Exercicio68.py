# Desafio 68:
# Faça um programa que jogue PAR OU ÍMPAR com o
# computador. O jogo só será interrompido quando
# o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
print('=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*10)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Pas ou Ímpar? [P/I] ')).strip().upper()[0]
    print(
        f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('*** DEU PAR ***' if total % 2 == 0 else '*** DEU ÍMPAR ***')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('VAMOS JOGAR NOVAMENTE...')
print(f'GAME OVER! Você venceu {v} vezes.')
