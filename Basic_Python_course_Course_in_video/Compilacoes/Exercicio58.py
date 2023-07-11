# Desafio 58:
# Melhore o jogo do DESAFIO 28, onde o computador vai "pensar" em
# um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites foram necessários
# para vencer.
"""
# Solução do professor:
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
"""
from random import randint
print('Sou seu computador...\nAcabei de pensar um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? \nQual é seu palpite?')
jogar = str(input('Quer iniciar o jogo agora? [S/N]: ')).strip().upper()[0]
if jogar == 'S':
    while jogar in 'S':
        numcomp = randint(0, 10)
        cont = 0
        num = int(input('Digite um número entre 0 e 10! '))
        cont += 1
        while num != numcomp:
            if num < numcomp:
                num = int(
                    input('Mais... Tente mais uma vez. \nQual é seu palpite? '))
                cont += 1
            else:
                num = int(
                    input('Menos... Tente mais uma vez. \nQual é seu palpite? '))
                cont += 1
        print('O número do computador foi {} e você acertou com {} tentativas.'.format(
            numcomp, cont))
        jogar = str(
            input('Quer iniciar o jogo agora? [S/N]: ')).strip().upper()[0]
print('O jogo ACABOU!')
