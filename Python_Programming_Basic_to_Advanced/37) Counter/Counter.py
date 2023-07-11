"""
Módulo Collections - Counter (contador):

Docs:
https://docs.python.org/3/library/collections.html?highlight=counter#collections.Counter
https://docs.python.org/pt-br/3/library/collections.html?highlight=counter#collections.Counter

Collections é conhecido como "High-performance Container Detetypes.

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo (Colletions Counter) que é parecido
com um dicionário. Contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências deste elemento.

# Utilizando o Counter

# Realizando o import
from collections import Counter

# Exemplo 1:

# Podemos utilizar qualquer iteráve.
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4,
         4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

>>> <class 'collections.Counter' >
# Para cada  elemento da lista, o Counter criou um chave e colocou como valor a qtd de ocorrência (repetições).
>>> Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Exemplo 2:

from collections import Counter

print(Counter('Geek University'))

# >>> Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3:

from collections import Counter

texto = "Uma corrida armamentista naval entre Argentina, Brasil e Chile — países mais poderosos e ricos da
América do Sul — começou no início do século XX, quando o governo brasileiro comprou três dreadnoughts,
formidáveis embarcações couraçadas cujas capacidades ultrapassavam em muito a dos navios mais antigos das
marinhas do resto do mundo."

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto.
print(res.most_common(5))

# Se quisérmos verificar as funcionalidades do Counter podemos digital no terminal:

>>> from collections import Counter
>>> help(Counter)
"""
from collections import Counter

texto = """Uma corrida armamentista naval entre Argentina, Brasil e Chile — países mais poderosos e ricos da
América do Sul — começou no início do século XX, quando o governo brasileiro comprou três dreadnoughts,
formidáveis embarcações couraçadas cujas capacidades ultrapassavam em muito a dos navios mais antigos das
marinhas do resto do mundo."""

palavras = texto.split()

res = Counter(palavras)
print(res)
