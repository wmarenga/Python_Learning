# Desafio 18:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente deste ângulo.

from math import sin, cos, tan, radians
ângulo = int(input('Digite um ângulo: '))
# É preciso converter o ângulo  para radiano.
print('O ângulo que informou foi {},\n o seno de {} é {:.3f},\n o cosseno de {} é {:.3f}\n e a tangente de {} é {:.3f}'.format(
    ângulo, ângulo, sin(radians(ângulo)), ângulo, cos(radians(ângulo)), ângulo, tan(radians(ângulo))))
