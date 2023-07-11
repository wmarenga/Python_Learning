"""
Pergunta 1:
Crie uma matriz de 10x10 com ZEROS e na posição (linha 2, coluna 5) com valor 100.

Use o Numpy para isso

a) import numpy as np
matriz = zeros([10,10])
matriz[2,5] = 100

*** b) import numpy as np
matriz = np.zeros([10,10])
matriz[2,5] = 100

c) import numpy as np
matriz = np.zeros(10,10)
matriz[2,5] = 100

Pergunta 2:
Crie uma matriz 10x10 cheias de número 5

a) import numpy as np
matriz = np.fives([10,10])

*** b) import numpy as np
matriz = 5*np.ones([10,10])

c) import numpy as np
matriz = 5*np.ones(10,10)

Pergunta 3:
Quando você deve usar Numpy?

a) Numpy sempre e melhor que Pandas
b) Numpy e melhor para exploracao de dados e analises graduais de descobertas de dados
***c) Numpy e a melhor opcao para matrizes e operacoes matematicas. Tambem e a melhor 
opcao para se usar dentro de lacos iterativos

Pergunta 4:
Considere o array abaixo

import numpy as np
matriz = np.array([[1,2,3],[10,20,30],[5,15,35]])
Crie um código que retorne os dados das linhas que tenha pelo menos 1 dado acima de 10

Dica: use o comando: np.any(filtro, 0)

filtro deve ser a condição

0 indica dados por linha, se fosse coluna, seria 1

*** a) matriz[np.any(matriz>10, 0)]
b) matriz[np.any(>10, 0)]
c) matriz[matriz>10]
"""

import numpy as np
matriz = np.array([[1,2,3],[10,20,30],[5,15,35]])
print(matriz[np.any(matriz>10, 0)])