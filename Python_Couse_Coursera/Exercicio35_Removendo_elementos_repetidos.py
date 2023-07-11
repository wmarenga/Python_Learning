"""
Exercício 35 - Removendo elementos repetidos
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros,
verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma
lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar
ordenada.
Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
Exemplo:
>>>lista = [2, 4, 2, 2, 3, 3, 1]
>>>remove_repetidos(lista)
[1, 2, 3, 4]
>>>remove_repetidos([1, 2, 3, 3, 3, 4])
[1, 2, 3, 4]
"""


def remove_repetidos(x):
    lista_nova = []
    for i in x:
        if i not in lista_nova:
            lista_nova.append(i)
    lista_nova.sort()
    return lista_nova


lista = [9, 5, 6, 2, 1, 7, 5, 8, 9, 4, 3, 7, 9]

print(remove_repetidos(lista))
