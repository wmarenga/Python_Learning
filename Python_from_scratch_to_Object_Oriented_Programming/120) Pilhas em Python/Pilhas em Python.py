# Pilhas em Python

sequencia = [11, 22, 33, 444]

pilha = []

# estaremos adicionando elementos da lista sequencia na pilha.
for elemento in sequencia:
    pilha.append(elemento)

pilha.append(555)

while len(pilha) > 0:
    print(pilha)
    # Elimina o ultimo elemento .pop()
    topo = pilha.pop()

    print(f'Objeto do topo da pilha: {topo}')
