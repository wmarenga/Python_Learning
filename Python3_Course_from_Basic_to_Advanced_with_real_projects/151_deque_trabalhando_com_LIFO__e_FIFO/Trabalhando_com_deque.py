"""
Pilhas e filas
Pilhas (stack) - LIFO - Last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterias em desempenho, porque a cada
item alterado, todos os índices serão modificados.

# LILO = Last in Last out
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)
livro_removido = livros.pop()
print(livro_removido)

# FIFO - First in First out

from collections import deque

fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Luiz Otávio')
fila.append('Wellington')
fila.append('Jo
sé')
print(f'Saiu: {fila.popleft()}')  # Saiu: Joãozinho
print(f'Saiu: {fila.popleft()}')  # Saiu: Maria
print(f'Saiu: {fila.popleft()}')  # Saiu: Luiz Otávio

from collections import deque

# Quantidade máxima de elementos da fila
fila = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
fila.append(5)
print(fila)
# Quando adicionamos 1 elemento, o mais antigo será apagado para adicionar o novo no final
fila.append(6)
print(fila)
fila.append(7)
print(fila)

from collections import deque
from time import sleep

# Quantidade máxima de elementos da fila com for
fila = deque(maxlen=10)

for i in range(1000):
    fila.append(i)
    sleep(1)
    print(fila)

from collections import deque

# Não será possível inserir pois a lista está no tamanho máximo
fila = deque(maxlen=10)
fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fila.insert(2, 'Luiz Otávio')  # insere um elemento no índice 2
print(fila)

# Mostra o índice de um determinado elemento (podemos determinar o intervalo de índices)
fila.index(x, start, finish)

fila.rotate(2)  # Passa os dois últimos elementos para o início da fila
"""
