"""
from math import sqrt, floor  # Para importar um funcionalidade específica.
# Quando importamos as funcionalidade de "math", serão inseridas todas as novas opções.
# import math
num = int(input('Digite um número: '))
raiz = sqrt(num)
# raiz = math.sqrt(num) - Somente usamos esta forma quando importamos todas as funcionalidades.
# print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) - Somente com todas as funcionalidades.
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

Biblioteca Random:

import random
# num = random.random() - gera um número aleatório entre 0 e 1.
num = random.randint(1, 10)  # gera um número aleatório entre 1 e 10.
print(num)

Importando Emoji's (https://pypi.org/search/?q=emoji):

import emoji
print(emoji.emojize("Ola Mundo :globe_with_meridians:", use_aliases=True))

# Desafio 16:
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
# a sua porção Inteira.
# Ex.: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

1) Opção:
import math
from math import trunc
número = float(input('Digite um número: '))
print('O número {}, tem a parte Inteira {}'.format(número, trunc(número)))

2) Opção:
número = float(input('Digite um número: '))
print('O número {}, tem a parte Inteira {}'.format(número, math.trunc(número)))

3) Opção:
número = float(input('Digite um número: '))
print('O número {}, tem a parte Inteira {}'.format(número, int(número)))

# Desafio 17:
# Faça um programa que leia o comprimento do cateto oposto e cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

# 1) Opção (matemática)

from math import hypot
cateto_oposto = float(
    input('Digite o comprimento do cateto oposto do triângulo: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('O cateto oposto é {}, o cateto adjacente é {} e a hipotenusa é {:.2f}'.format(
    cateto_oposto, cateto_adjacente, hipotenusa))

# 2) Opção (importando de math)
cateto_oposto = float(
    input('Digite o comprimento do cateto oposto do triângulo: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('O cateto oposto é {}, o cateto adjacente é {} e a hipotenusa é {:.2f}'.format(
    cateto_oposto, cateto_adjacente, hypot(cateto_oposto, cateto_adjacente)))

# Desafio 18:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente deste ângulo.

from math import sin, cos, tan, radians
ângulo = int(input('Digite um ângulo: '))
# É preciso converter o ângulo  para radiano.
print('O ângulo que informou foi {},\n o seno de {} é {:.3f},\n o cosseno de {} é {:.3f}\n e a tangente de {} é {:.3f}'.format(
    ângulo, ângulo, sin(radians(ângulo)), ângulo, cos(radians(ângulo)), ângulo, tan(radians(ângulo))))

# Desafio 19:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno sortudo escolhido foi: {}'.format(escolhido))

# Desafio 20:
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

from random import shuffle
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

# Desafio 21:
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

"""

# Desafio 21:
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('aquarela.mp3')
pygame.mixer.music.play()
