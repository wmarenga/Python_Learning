""" 
numpy 
instalacao: pip install numpy

O Numpy e mais utilizado em performance no processamento das formulas e dos dados. 
"""

" No Python e uma lista mas pode se tornar um vetor no Numpy (Array)"
idades = [10,15,20,18]

import numpy as np

" Definindo como Array "
" Primeira linha da matriz"
idades = np.array([10,15,20,18,20])
print(idades)
print(type(idades))

" Criando um Array notas "
" Segunda linha da matriz "
notas = np.array([9,8,5,7,10])
print(notas[2])

" Criando um filtro "
print(notas[idades==20])

" Funcoes especificar no numpy "
print(np.mean(idades))

" Criando um array multidimensional (salario) "
" Cada colchete interno e uma linha da matriz 3x3"
salario = np.array([[1000,1200,1300],[800,900,950],[2000,2100,2110]])
print(salario)

" linha posicoes 0,1,2/ coluna posicoes 0,1,2 "
" visualiza a segunda linha (posicao 1) e terceira coluna (posicao 2)"
print(salario[1,2])

" O numpy tambem possui funcoes aritimeticas (sen, cos, tang), nao e possivel acha no Python"
" Cosseno em radiano"
print(np.cos(1))

" Tambem podemos importar arquivos externos, tais como: Excel, CSV, TXT, porem no pandas e mais simples e mais estruturado "

" Uso de numero infinito "
x = np.inf
print(x)
print(type(x))

" Podemos criar matrizes com zeros e uns "
matriz = np.zeros([4,3])
print(matriz)

matriz2 = np.ones([3,2])
print(matriz2)