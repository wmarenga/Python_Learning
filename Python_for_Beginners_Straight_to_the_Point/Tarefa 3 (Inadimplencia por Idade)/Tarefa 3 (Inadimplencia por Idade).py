""" 
Tarefa: Inadimplência por idade

10 minutos para concluir

Tente descobrir se a promoção impacta no tempo de pagamento!

Tente gerar gráficos e informações para concluir se a idade do comprador pode influenciar a coluna pg ser 
igual a 0, ou seja, uma inadimplência na compra.

Lembre que idade - 0 indica que não temos a data de nascimento do comprador!

Perguntas dessa tarefa

Existe alguma relação entre idade e inadimplência (coluna pg=0) ?

"""
from logging import PercentStyle
from turtle import left
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import seaborn as sns
import datetime

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Tarefa 3 (Inadimplencia por Idade)/caso_estudo.xlsx'
caminho_arquivo_Excel_prom ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Tarefa 3 (Inadimplencia por Idade)/caso_estudo_venda_promocao.csv'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')
dfpromocao = pd.read_csv(caminho_arquivo_Excel_prom, sep=";")

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

dfclientes = dfclientes.join(dfpromocao.set_index('id_venda'))
df_juncao = dfvendas.join(dfclientes.add_prefix('clientes_'), on='id_cliente')
df_juncao = df_juncao.join(dflojas.add_prefix('lojas_'), on='id_loja')
df_juncao = df_juncao.join(dfprodutos.add_prefix('produto_'), on='id_produto')
df_juncao = df_juncao.join(dfpagamentos.set_index('id_venda'))

df_juncao['pg'] = 1
df_juncao.loc[df_juncao.dt_pgto.isnull(), 'pg'] = 0
tempo_pgto = df_juncao.dt_pgto - df_juncao.dt_venda
df_juncao['tempo_pg'] = (df_juncao.dt_pgto - df_juncao.dt_venda).dt.days
df_juncao['cliente_idade'] = np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))

" Com este comando podemos ajustar quantas colunas serao exibidas"
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 120)

" ## INADIMPLENCIA POR IDADE ## "

" Inadimplencia total "
print(df_juncao)

" Inadimplencia por idade "
print(df_juncao[df_juncao.pg == 0].groupby('cliente_idade').count().pg)
graf_dados = df_juncao[df_juncao.pg == 0].groupby('cliente_idade').count().pg.sort_values(ascending=False)
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title(" Inadimplencia por Idade ")
plt.xticks(rotation=45)
plt.show()

" Gerando um percentual da coluna (pg)"
print(df_juncao.groupby('cliente_idade').mean().pg.sort_values(ascending=False))
graf_dados = df_juncao.groupby('cliente_idade').mean().pg.sort_values(ascending=False)
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title(" Percentagem inadimplencia por por idade ")
plt.xticks(rotation=45)
plt.show()

"""SOLUCAO DO PROFESSOR """

graf_dados = df_juncao[['cliente_idade','pg']].groupby('cliente_idade').mean().sort_values('cliente_idade')
print(graf_dados)
graf_dados.plot()
plt.show()

" O grafico mostra que a idade nao importa na porcentagem de pagamentos "

" Percebemos que existem dados que alteramos para poder trabalhar com a tabela (cliente_idade < 1) "

print(df_juncao[df_juncao.cliente_idade < 1])