""" 
Instalando o Pandas:

pip install pandas

Diferenca entre NUMPY e PANDAS:
O numpy foi desenvolvido para facilitar operacoes matematicas de forma rapida e eficiente. enquanto que o pandas foi criado
para facilitar a manipulacao de dados e tabelas.

Se pretende operar dados e Array dentro de um laco FOR com varias repeticoes, utilize o numpy (performance superior). 
Mas se estamos trabalhando com os dados sem precisar fazer lacos em apenas uma linha, o pandas e mais adequado.

"""

import pandas as pd
import numpy as np
import copy

" Criando uma tabela de forma manual "
" Criamos como se fosse um dicionario "
tabela = pd.DataFrame({'nome': ['Rafael', 'Joao', 'Rafael', 'Maria'], 'nota': [10,9,8,7]})
print(tabela)

" Acessando os dados da tabela "
print(tabela.nome)

" Acessando na posicao 2"
print(tabela.nome[2])

" O numero da linha e o nome da coluna "
print(tabela.loc[2,'nome'])

" Media de nota baseado no nome "
print(tabela.groupby('nome').mean())

" Contabilizar os dados "
print(tabela.groupby('nome').count())

" Criamos um filtros cujo o nome na coluna nome e igual a Rafael e exibimos a nota relativa a este nome "
print(tabela.nota[tabela.nome=='Rafael'])

" Conversoes entre pandas e numpy "
tabela2 = np.array(tabela)
print(tabela2)

" Conseguimos acessar a tabela perfeitamente "
print(tabela2[2,1])

" Tanto o Numpy quanto o Pandas sao orientados a objeto, pois alterando os dados de uma copia, alteramos os dados do original"

#tabela3 = tabela


" Ambas as tabelas foram alteradas "

" Para evitar que isto aconteca, usamos a funcao deepcopy"
tabela3 = copy.deepcopy(tabela)
tabela3.loc[0, 'nota'] = 3
print(tabela3)
print(tabela)