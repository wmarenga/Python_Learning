import pandas as pd
import numpy as np

"Lendo a planilha do Excel pelo pandas"
caminho_arquivo ='D:\\23) Programação\\Cursos\\Python\\4) Python para Iniciantes (Direto ao que interessa)\\Aula 27 (Leitura do Excel_Numpy)\\caso_estudo.xlsx'
pessoas = pd.read_excel(caminho_arquivo, sheet_name='pessoas')
print(pessoas)

"Convertendo um DataFrame em um array"
pessoas = np.array(pessoas)
print(pessoas)

"Se quiser fazer a leitura e a conversao em uma unica linha"
pessoas = np.array(pd.read_excel(caminho_arquivo, sheet_name='pessoas'))
print(pessoas)

"Acessando os dados (Todos os dados da ultuma coluna"
"Inserimos os 2 ponto (:) para indicar que queremos todos os dados da linha e/ou coluna"
print(pessoas[:,3])

"Aplicando uma soma em uma coluna (numpy)"
print(np.sum(pessoas[:,3]))

"Aplicando uma soma em uma coluna (pandas)"
print(pessoas.idade.sum())