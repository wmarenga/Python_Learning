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
