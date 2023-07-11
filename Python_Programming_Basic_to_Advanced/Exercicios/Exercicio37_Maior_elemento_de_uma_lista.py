"""
Exercício 37 - Maior elemento de uma lista
Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e 
devolve um número inteiro correspondente ao maior valor presente na lista recebida.
"""


def maior_elemento(a):
    maior = 0
    for num in a:
        if num < 0:
            maior = num
        if num > maior:
            maior = num
    return maior


lista = [-90, -27, -12, 10]
#lista = [2, 4, 9, 10, 3, 0, 88]

print(maior_elemento(lista))
