"""
Desempacotamento de Listas:

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista
print(n1, n2, n3, outra_lista)
print(outra_lista)
print(ultimo_da_lista)

# O n1, n2, n3 são o antepenúltimo, penúltimo e último elementos da lista.
*outra_lista, n1, n2, n3 = lista
print(n1)


"""
# Utilizando o *_, estamos dizendo que não precisamos do resto da lista.
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
n1, n2, *_ = lista
print(n1, n2)
