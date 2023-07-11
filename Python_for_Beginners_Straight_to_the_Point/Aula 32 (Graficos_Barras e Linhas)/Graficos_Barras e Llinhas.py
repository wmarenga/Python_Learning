"""
Antes de comecar, precisamos instalar a biblioteca do Matplotlib
Outras bibliotecas para grafico, sao: Seaborn, Plotly (mais interativa e avancada), GGplot, Altair, Bokeh, Pygal, Geoplotlib
Se quisermos instalar via comando temos que adicionar uma exclamacao (!pip install matplotlib)

"""

import matplotlib.pyplot as plt 
import pandas as pd

caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 32 (Graficos_Barras e Linhas)/leitura.xlsx'
df = pd.read_excel(caminho_arquivo, sheet_name='dados')
print(df.head())

"Plotando um grafico de linha"
x = df.tempo
y = df.temperatura
plt.plot(x,y)
plt.show()

"Criando um grafico de barras, o grafico de barras e muito bom para categorias"
"Media de tudo"
print(df.groupby('periodo').mean())

"Meida da temperatura somente"
print(df.groupby('periodo').temperatura.mean())

"Acessando os periodos"
print(df.groupby('periodo').temperatura.mean().index)

"Acessando os valores"
print(df.groupby('periodo').temperatura.mean().values)

x = df.groupby('periodo').temperatura.mean().index
y = df.groupby('periodo').temperatura.mean().values
plt.bar(x,y)
plt.show()