"Cria um array de zeros com 2 linhas e duas colunas"
import numpy as np
a = np.zeros([2,2])
print(a)

"Duas linhas e 3 colunas"
a = np.zeros([2,3])
print(a)

"Podemos inserir/alterar o valor da linha 0 e coluna 1"
a[0,1] = 3
print(a)
"""
"Apresentara um erro pois nao existe dados nesta posicao da matriz (esta fora da matriz definida)"
a[5,0] = 1
print(a)

"""

"Criamos uma matriz com uns (1)"
a = np.ones([4,3])
print(a)