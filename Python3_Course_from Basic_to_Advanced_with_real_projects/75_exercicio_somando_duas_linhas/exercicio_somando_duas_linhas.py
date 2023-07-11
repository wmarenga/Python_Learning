"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores
somados:
Se uma lista for maior que a outra, a soma só vai considerar o
tamanho da menor.

Exemplo:
lista_a     = [10, 2, 3, 4, 5]
lista_b     = [12, 2, 3, 6, 50, 60, 70]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
