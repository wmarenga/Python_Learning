# *** TUPLA ***
# num = (2, 5, 9, 1)
# num[2] = 3
# Não permite alteração pois é uma TUPLA.
# TypeError: 'tuple' object does not support item assignment
# print(num)
"""
num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 -> Não conseguimos adicionar valores desta maneira. Temos que usar o
# comando "APPEND"  -> num.append(7).
num.append(7)  # adiciona valores
num.sort()  # ordena os elementos em ordem crescente
num.sort(reverse=True)  # ordena os elementos em ordem decrescente (inversa).
num.insert(2, 0)  # Na posição 2 inserir o valor 0.
num.pop()  # Elimina o último valor da lista.
num.pop(2)  # Elimina o elemento na posição 2 (index).
# Elimina o primeiro elemento 2 da lista (da esquerda para direita).
num.remove(2)
# Dessa maneira podemos eliminar os elementos somente se eles existirem na lista.
if 4 in num:
    num.remove(4)
    else:
        print('Não achei o número 4')
print(num)
# Mostra a quantidade de elementos em uma lista.
print(f'Essa lista tem {len(num)} elementos.')

# Podemos utilizar as duas maneiras abaixo para criar uma lista vazia.
valores = []
# valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# Digitar cinco valores, do índice 0 até 4.
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a

# Quando igualamos duas lista, qualquer alteração em uma lista, altera a outra também.
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')

"""

# Desta maneira criamos uma cópia da lista A e não uma ligação entre elas.
# Alterando o elemento da lista B, não alteramos a lista A.
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
