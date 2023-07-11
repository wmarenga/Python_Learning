"""
Exercício 38 - Invertendo sequência
Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência 
de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina 
pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:

Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1
"""

lista = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num == 0:
        del(lista[-1])
        break

lista.reverse()
for i in lista:
    print(i)
