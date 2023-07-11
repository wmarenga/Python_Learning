# Desafio 98:
# Faça um programa que tenha uma função chamada contador(), que
# receba três parâmetros: início, fim e passo. Seu programa tem
# que realizar três contagens através da função criada:
# A) de 1 até 10, de 1 em 1;
# B) de 10 até 0, de 2 em 2
# C) uma contagem personalizada.

from ast import parse
from time import sleep


def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*15)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    print('-='*15)
    sleep(2.5)

    if início < fim:
        cont = início
        while cont <= fim:
            # A função flush não liga o buffer de tela. Não espera o comando terminar totalmente.
            print(f'{cont} ', end='', flush=True)
            cont += passo
            sleep(0.5)
        print('FIM')
    else:
        cont = início
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            cont -= passo
            sleep(0.5)
        print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
contador(início=int(input('Início: ')), fim=int(
    input('Fim: ')), passo=int(input('Passo: ')))
