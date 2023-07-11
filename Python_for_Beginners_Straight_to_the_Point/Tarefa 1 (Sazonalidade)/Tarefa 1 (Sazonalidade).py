""" 
Tarefa: Sazonalidade
10 minutos para concluir

Agora é com você, tente criar uma análise para ver se existe alguma sazonalidade nos nossos dados. Sazonalidade é um 
comportamento no tempo, mostrando que nossos dados podem ter algum padrão na variação no tempo.

Perguntas dessa tarefa
Tente responder as perguntas:

- Você observa alguma sazonalidade nos dados?

- As vendas estão crescendo ou diminuindo ano a ano? (cuidado! a receita é mais importante que a quantidade vendida)

"""
from logging import PercentStyle
from turtle import left
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import seaborn as sns
import datetime

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Tarefa 1 (Sazonalidade)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

dfclientes.loc[dfclientes.nome.isnull(), 'nome'] = 'Sem Nome'
dfclientes.loc[dfclientes.sexo.isnull(), 'sexo'] = 'O'
dfclientes.loc[dfclientes.dt_nasc.isnull(), 'dt_nasc'] = '1/1/2020'

dfprodutos.loc[9,'valor'] = dfprodutos.valor[9]/10000
dfclientes.dt_nasc = pd.to_datetime(dfclientes.dt_nasc, format= '%m/%d/%Y')

dfclientes = dfclientes.set_index('id')
dflojas = dflojas.set_index('id')
dfprodutos = dfprodutos.set_index('id')
dfvendas = dfvendas.set_index('id')
dfpagamentos = dfpagamentos.set_index('id')

df_juncao = dfvendas.join(dfclientes.add_prefix('clientes_'), on='id_cliente')
df_juncao = df_juncao.join(dflojas.add_prefix('lojas_'), on='id_loja')
df_juncao = df_juncao.join(dfprodutos.add_prefix('produto_'), on='id_produto')
df_juncao = df_juncao.join(dfpagamentos.set_index('id_venda'))

df_juncao['pg'] = 'Pago'
df_juncao.loc[df_juncao.dt_pgto.isnull(), 'pg'] = 'Inadimplente'
tempo_pgto = df_juncao.dt_pgto - df_juncao.dt_venda
df_juncao['tempo_pg'] = (df_juncao.dt_pgto - df_juncao.dt_venda).dt.days
df_juncao['cliente_idade'] = np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))

" Com este comando podemos ajustar quantas colunas serao exibidas"
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 120)

graf_dados = df_juncao.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False)

" ## ANALISANDO CRITERIOS DE SAZONALIDADE ## "
print(df_juncao)
df_juncao['meses_venda'] = (df_juncao['dt_venda'].dt.month)

df_juncao['meses_venda'] = df_juncao['meses_venda'].map({1:'Janeiro',2:'Fevereiro',3:'Marco',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'})
print(df_juncao)

df_juncao['Produto_loja'] = df_juncao.produto_produto + " / Cidade: " + df_juncao.lojas_cidade

print(df_juncao)

" Esse comando gera uma média móvel de 30 dias de um agrupamento de vendas por dia "
graf_dados = df_juncao[['produto_valor','dt_venda']].groupby('dt_venda').sum().rolling(30)
print(graf_dados)

""" 1) Você observa alguma sazonalidade nos dados? """

" Criando um grafico no matplotlib (Receita por Mes)"

" Vamos ordenar os dados pela receita (decrescente) "

graf_dados = df_juncao[['meses_venda', 'produto_valor']].groupby('meses_venda').sum().produto_valor.sort_values(ascending=False)

plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Receita por Mes')
plt.show()
" O mes de Julho foi o mes que mais vendeu "

graf_dados = df_juncao[['Produto_loja', 'produto_valor']].groupby('Produto_loja').sum(min_count=100).produto_valor.sort_values(ascending=False)
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Produto/Loja que mais venderam')
plt.xticks(rotation=20)
plt.show()
" O produto que mais vendeu foi o laptop Basico (no Rio de Janeiro)"

df_juncao['Produto_meses'] = df_juncao.produto_produto + " - " + df_juncao.meses_venda
graf_dados = df_juncao[['Produto_meses', 'produto_valor']].groupby('Produto_meses').sum(min_count=100).produto_valor.sort_values(ascending=False)
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Produto por mes que mais venderam')
plt.xticks(rotation=20)
plt.show()
" O laptop basico vendeu mais um Julho "

""" As vendas estão crescendo ou diminuindo ano a ano? (cuidado! a receita é mais importante que a quantidade vendida) """

" Soma das vendas mes a mes por cidade "
plt.figure(figsize=(15,5))
graf_dados = pd.pivot_table(df_juncao, index='meses_venda', columns='lojas_cidade', values='produto_valor', aggfunc='sum')
graf_dados = graf_dados.reset_index()

" Renomeando colunas com nome incorretos "
df_juncao['meses_venda'] = df_juncao['meses_venda'].map({1:'Janeiro',2:'Fevereiro',3:'Marco',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'})
graf_dados['Belo Horizonte'] = 'Belo_Horizonte'
graf_dados['Rio de Janeiro'] = 'Rio_de_Janeiro'
graf_dados['Santa Catarina'] = 'Santa_Catarina'
graf_dados['São Paulo'] = 'Sao_Paulo'
graf_dados = graf_dados[['meses_venda', 'Brasília']].groupby('meses_venda').sum().Brasília.sort_values(ascending=True)
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Produto por mes que mais venderam')
plt.xticks(rotation=20)
plt.show()

" Ao final desta analise eu nao consegui ordenar a coluna 'meses_venda' pois eu havia convertido para os nomes dos meses para ficar mais facil de identificar "

""" Exibir colunas e indices
print(graf_dados.columns.tolist())
print(graf_dados.index.tolist())
"""

"""SOLUCAO DO PROFESSOR """

" Plotar Media Movel da Receita "
plt.figure(figsize=(15,5))
graf_dados = df_juncao[['produto_valor', 'dt_venda']].groupby('dt_venda').sum().rolling(30).mean()
plt.plot(graf_dados.index, graf_dados.values)
plt.title('Media Movel (30 dias) da Receita')
plt.xticks(rotation=45)
plt.show()

" Plotar Media Movel da Receita por Cidade "
fig, ax = plt.subplots(figsize=(15,5))
graf_dados = df_juncao[['produto_valor','lojas_cidade','dt_venda']].groupby(['dt_venda','lojas_cidade']).sum().rolling(30).mean().unstack().plot(ax=ax)
plt.show()

" Plotar média móvel da receita por produto "
fig, ax = plt.subplots(figsize=(15,5))
graf_dados = df_juncao[['produto_valor','produto_produto','dt_venda']].groupby(['dt_venda','produto_produto']).sum().rolling(30).mean().unstack().plot(ax=ax)
plt.show()

" criando uma nova coluna contendo o ano da venda "
df_juncao['venda_ano'] = pd.DatetimeIndex(df_juncao.dt_venda).year

" tendencia de receita por ano "
fig, ax = plt.subplots(figsize=(15,5))
graf_dados = df_juncao[['produto_valor','venda_ano']].groupby(['venda_ano']).sum().unstack().plot(ax=ax)
plt.show()

"tendência por produto" 
fig, ax = plt.subplots(figsize=(15,5))
graf_dados = df_juncao[['produto_valor','produto_produto','venda_ano']].groupby(['venda_ano','produto_produto']).sum().unstack().plot.bar(ax=ax)
plt.show()

" tendência por cidade "
fig, ax = plt.subplots(figsize=(15,5))
graf_dados = df_juncao[['produto_valor','lojas_cidade','venda_ano']].groupby(['venda_ano','lojas_cidade']).sum().unstack().plot.bar(ax=ax)
plt.show()