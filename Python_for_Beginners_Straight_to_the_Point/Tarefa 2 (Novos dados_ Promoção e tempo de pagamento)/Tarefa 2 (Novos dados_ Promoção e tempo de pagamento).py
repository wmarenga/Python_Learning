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

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Tarefa 2 (Novos dados_ Promoção e tempo de pagamento)/caso_estudo.xlsx'
caminho_arquivo_Excel_prom ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Tarefa 2 (Novos dados_ Promoção e tempo de pagamento)/caso_estudo_venda_promocao.csv'
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

df_juncao['pg'] = 'Pago'
df_juncao.loc[df_juncao.dt_pgto.isnull(), 'pg'] = 'Inadimplente'
tempo_pgto = df_juncao.dt_pgto - df_juncao.dt_venda
df_juncao['tempo_pg'] = (df_juncao.dt_pgto - df_juncao.dt_venda).dt.days
df_juncao['cliente_idade'] = np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))

" Com este comando podemos ajustar quantas colunas serao exibidas"
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 120)

" ## NOVOS DADOS: PROMOCAO E TEMPO DE PAGAMENTO ## "

""" Um novo dado surgiu: promoções!! Será que ele nos ajuda em algo? "

Instruções da tarefa
10 minutos para concluir
Suponha que você tenha buscado novos dados e descobriu uma nova base de promoções!

Ela mostra se cada venda foi gerada a partir de uma promoção ou não (base em anexo, em CSV)

Nessa nova base temos o ID da venda e uma coluna binária, informando se houve promoção (1) ou não (0).

Tente avaliar se a promoção influencia o tempo de pagamento.

Cuidado, a base está em CSV, o comando para leitura dela deve ser:

alguma_variavel = pd.read_csv('caso_estudo_venda_promocao.csv', sep=";")

Outra dica importante é que você precisará fazer um JOIN entre o DataFrame df e esse novo dado.

Não se preocupe, temos a resolução do exercício na próxima aula!

Perguntas dessa tarefa
Tente descobrir se a promoção impacta no tempo de pagamento!

"""
graf_dados = df_juncao[['tempo_pg', 'clientes_promoção']].groupby('tempo_pg').sum().clientes_promoção.sort_values(ascending=False)
print(graf_dados)
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Tempo de Pagamento influenciado pela promocao - Barras')
plt.show()
""" Nao foi verificado uma maior concentracao de promocoes nos menores tempos de pagamentos """

graf_dados = df_juncao[['tempo_pg', 'clientes_promoção']].groupby('tempo_pg').sum().clientes_promoção.sort_values(ascending=False)
print(graf_dados)
plt.figure(figsize=(15,5))
sns.histplot(data=df_juncao.tempo_pg, kde=True)
plt.title('Tempo de Pagamento influenciado pela promocao - Histograma ')
plt.show()
""" De acordo com o grafico do histograma nao verifquei nenhuma relacao entre o tempo de pagamento sendo reduzido pelo fato da participacao dos clientes em
promocoes.Nao incidindo uma curva normal com maior concentracao dos dados em maior volume de promocoes em relacao ao menor tempo de pagamento dos clientes"""

"""SOLUCAO DO PROFESSOR """

" Tempo médio de pagamento por promoção "

#lendo arquivo CSV
dfPromo = pd.read_csv('D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Tarefa 2 (Novos dados_ Promoção e tempo de pagamento)/caso_estudo_venda_promocao.csv', sep=";")
#definir index
dfPromo = dfPromo.set_index('id_venda')
#join entre df e dfPromo
df_juncao = df_juncao.join(dfPromo)
print(df_juncao)

" Grafico Boxplot dos tempos medios de pagamento quando tem promocao e sem promocao "
" Quando temos promocao, o tempo medio de pagamento parace aumentar "
graf_dados = df_juncao[['promoção','tempo_pg']][~df_juncao.tempo_pg.isnull()]
graf_dados.groupby('promoção').boxplot(column=['tempo_pg'])
plt.show()

" Grafico quando a promocao e igual a zero"
" Percebemos que quando o cliente nao tem promocao, os pagamentos acontecem com mais frequencia antes de 20 dias "
sns.histplot(data=graf_dados.tempo_pg[graf_dados['promoção']==0], kde=True)
plt.title('Tempo médio de pagamento para casos sem promoção')
plt.show()

" Grafico quando a promocao e igual a um"
" Percebemos que quando o cliente tem promocao, os pagamentos acontecem com mais frequencia apos 20 dias "
sns.histplot(data=graf_dados.tempo_pg[graf_dados['promoção']==1], kde=True)
plt.title('Tempo médio de pagamento para casos com promoção')
plt.show()