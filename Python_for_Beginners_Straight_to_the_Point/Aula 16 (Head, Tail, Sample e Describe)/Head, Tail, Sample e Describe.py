"""
Error possiveis:

1) Erro de (xlrd):
    pip install xlrd (no prompt de comando)
2) Erro engine:
    pip install openpyxl (no prompt de comando)
    e acrescentar , (,engine='openpyxl')
3) Se tiver um arquivo .CSV, use o comando (pb.read_csv)

### Podemos utilizar o comando display(df) no Jupyter para visualizar melhor a tabela ###
"""

import pandas as pd
caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 16 (Head, Tail, Sample e Describe)/caso_estudo.xlsx'
pessoas = pd.read_excel(caminho_arquivo,sheet_name='pessoas',engine='openpyxl')
covid = pd.read_excel(caminho_arquivo,sheet_name='registros_covid',engine='openpyxl')

"head() - Implime o cabecalho da planilha com 5 primeiros dados (padrao)"
print(pessoas.head())
print(covid.head())

"head() - Implime o cabecalho da planilha com 10 primeiros dados (definido nos parametros)"
print(pessoas.head(10))
print(covid.head(10))

"tail() - Implime os 5 ultimos dados da planilha (padrao)"
print(pessoas.tail())
print(covid.tail())

"tail() - Implime os 10 ultimos dados da planilha (definido nos parametros)"
print(pessoas.tail(10))
print(covid.tail(10))

"sample() - Implime aleatoriamenteos algum dado da planilha (padrao 1 dado somente)"
print(pessoas.sample())
print(covid.sample())

"sample() - Implime aleatoriamenteos algum dado da planilha (definido nos parametros)"
print(pessoas.sample(5))
print(covid.sample(5))

"describe() - Implime um resumo da colunas da planilha (quantidade, media, desvio padrao, minimo, maximo"
print(pessoas.describe())
print(covid.describe())