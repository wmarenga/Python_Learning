"""
Exercício 36 - Soma dos elementos de uma lista
Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros 
e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
"""


def soma_elementos(a):
    soma = 0
    for num in a:
        soma += num
    return soma


lista = [1, 3, 6, 7, 8, 9, 2]

print(soma_elementos(lista))
