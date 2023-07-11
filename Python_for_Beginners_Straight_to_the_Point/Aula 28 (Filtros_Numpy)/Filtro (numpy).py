import pandas as pd
import numpy as np

"Lendo a planilha do Excel pelo pandas/Numpy"
caminho_arquivo ='D:\\23) Programação\\Cursos\\Python\\4) Python para Iniciantes (Direto ao que interessa)\\Aula 28 (Filtros_Numpy)\\caso_estudo.xlsx'
pessoas = np.array(pd.read_excel(caminho_arquivo, sheet_name='pessoas'))
print(pessoas)

"Mostrar todas as linhas da 2 coluna que e igual a 'Caio Pereira'"
print(pessoas[pessoas[:,1]=='Caio Pereira'])

"Mostrar todas as linhas da 3 coluna que e igual a 'M'"
print(pessoas[pessoas[:,2]=='M'])

"## Mostrar apenas a coluna 3 ## com todas as linhas da 3 coluna que e igual a 'M'"
print(pessoas[pessoas[:,2]=='M',3])

"## Aplicar uma soma na coluna 3 ## com todas as linhas da 3 coluna que e igual a 'M'"
print(np.sum(pessoas[pessoas[:,2]=='M',3]))

"## Podemos tb aplicar minimo, maximo e mediana coluna 3, como no pandas ## com todas as linhas da 3 coluna que e igual a 'M'"
print(np.min(pessoas[pessoas[:,2]=='M',3]))
print(np.max(pessoas[pessoas[:,2]=='M',3]))
print(np.mean(pessoas[pessoas[:,2]=='M',3]))