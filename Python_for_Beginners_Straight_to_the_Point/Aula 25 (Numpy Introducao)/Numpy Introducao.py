"""
A biblioteca Numpy e muito util para quem trabalha com muita operacao matematica etambem e muito rapido

Para instalar o Numpy:
$ pip install numpy (prompt de comando)

a = np.array([10,20,30])
"Um array e bem parecido com uma lista do Python mas podemos fazer bastante coisa com um array"
print(a)

"Acessando a primeira posicao do array"
print(a[0])

"Acessando as posicoes 0 e 1 de uma lista (lembrar que a posicao 2 nao e incluida)"
print(a[0:2])

"""
import numpy as np

"Criando uma matriz em um array"
a = np.array([[10,20,30],[100,200,300]])
print(a)

"Acessando o array na primeira linha e terceira coluna"
print(a[0,2])

"Media de todos os valores"
print(a.mean())

"Media das linhas"
print(a.mean(0))

"Media por coluna"
print(a.mean(1))

