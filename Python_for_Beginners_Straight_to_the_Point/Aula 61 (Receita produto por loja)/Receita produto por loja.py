from logging import PercentStyle
from turtle import left
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import seaborn as sns

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 61 (Receita produto por loja)/caso_estudo.xlsx'
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

print(df_juncao)
print(df_juncao.isnull().sum())

" ## FEATURE ENGINEERING ## "

""" Incluindo uma nova coluna de pagamentos (pg) e defimimdo com 1 para dizer que todas as vendas 
tiveram pagamentos """
df_juncao['pg'] = 'Pago'
print(df_juncao)

""" Alterando todos os registros sem pagamentos para 'Inadimplente'
df.loc[nome_linha, nome_coluna]"""
df_juncao.loc[df_juncao.dt_pgto.isnull(), 'pg'] = 'Inadimplente'
print(df_juncao)

" Criando o dados de tempo de pagamento "
tempo_pgto = df_juncao.dt_pgto - df_juncao.dt_venda
print(tempo_pgto)

" Retirando o (days) do DataFrame, fazendo com que a informacao seja convertida para numeros "
df_juncao['tempo_pg'] = (df_juncao.dt_pgto - df_juncao.dt_venda).dt.days
print(df_juncao)

" Criando a idade dos clientes (O comando 'pd.to_datetime('today')' pega a data atual"
" Usamos estecomando do numpy para converter para anos (/np.timedelta64(1,'Y')"
print((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))

" Acrescentando no inicio da sequencia de comando o comando (np.floor), teremos um arredondamento para baixo"
print(np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y')))

" Armazenando os dados gerados em uma nova coluna chamada ('cliente_idade')"
df_juncao['cliente_idade'] = np.floor((pd.to_datetime('today') - df_juncao.clientes_dt_nasc)/np.timedelta64(1,'Y'))
print(df_juncao)

" ## ANALISE DE LOJAS E PRODUTOS QUE MAIS VENDEM ## "

" Com este comando podemos ajustar quantas colunas serao exibidas"
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 120)

print(df_juncao)

" Contabilizando todos os dados pelas lojas das cidades "
print(df_juncao.groupby('lojas_cidade').count())

" Somando todos os dados pelas lojas das cidades "
print(df_juncao.groupby('lojas_cidade').sum())

" Somando apenas os dados das lojas das cidades para (produto_valor) = receita de cada loja"
print(df_juncao.groupby('lojas_cidade').sum().produto_valor)

" Contagem da quantidade de venda apenas das lojas das cidades para (produto_valor)"
print(df_juncao.groupby('lojas_cidade').count().produto_valor)

" Ordenando a contagem de quantidade de venda apenas das lojas das cidades para (produto_valor)"
print(df_juncao.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False))

" Inserir o groupby de vendas por cidades em uma variavel "
graf_dados = df_juncao.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False)
print(graf_dados)

" Criando um grafico no matplotlib (vendas por loja)"
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Vendas por Loja')
plt.show()

" ## ANALISANDO A QUANTIDADE DE PRODUTOS QUE MAIS VENDEM ## "

" Contabilizando todos os dados dos produtos, considerando produto_valor como a informacao mais relevante "
print(df_juncao.groupby('produto_produto').count().produto_valor)

" Ordenando a contagem de quantidade de produtos, considerando produto_valor como a informacao mais relevante)"
print(df_juncao.groupby('produto_produto').count().produto_valor.sort_values(ascending=False))

" Armazenado o groupby de produtos em uma variavel "
graf_dados = df_juncao.groupby('produto_produto').count().produto_valor.sort_values(ascending=False)
print(graf_dados)
print(graf_dados.index)
print(graf_dados.values)

" Criando um grafico no matplotlib (Vendas por Produtos)"
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Vendas por Produto')
plt.show()

" ## RECEITA POR LOJA ## "

" Somando todos os dados pelas lojas das cidades "
print(df_juncao.groupby('lojas_cidade').sum())

" Criando um filtro para aas colunas que queremos trabalhar "
" Fazendo um filtro antes do groupby, deixamos o codigo mais leve, pois realizamos o filtro antes de fazer a conta matematica "
print(df_juncao[['lojas_cidade', 'produto_valor']].groupby('lojas_cidade').sum())

" Ordenando a contagem de quantidade de produtos_valor por cidades "
" Desta maneira e apresentada uma serie, sendo mais facil de ser operada em um grafico de barras "
print(df_juncao[['lojas_cidade', 'produto_valor']].groupby('lojas_cidade').sum().produto_valor.sort_values(ascending=False))

" Se nao informarmos a coluna (produto_valor) apos a sum(), temos que informar no parametro sort_values(ascending=False, by='produto_valor')"
" Desta maneira e exibido um DataFrame"
print(df_juncao[['lojas_cidade', 'produto_valor']].groupby('lojas_cidade').sum().sort_values(ascending=False, by='produto_valor'))

" Armazenado o groupby de Receita por Loja em uma variavel "
graf_dados = df_juncao[['lojas_cidade', 'produto_valor']].groupby('lojas_cidade').sum().produto_valor.sort_values(ascending=False)
print(graf_dados)
print(graf_dados.index)
print(graf_dados.values)

" Criando um grafico no matplotlib (Receita por Loja)"
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Receita por Loja')
plt.show()

" Analisar qual e o percentar de receita do Rio de Janeiro em relacao as outras lojas "
print(graf_dados.max()/graf_dados[graf_dados!=graf_dados.max()].mean())
" Descrevendo melhor o valor apresentado "
" O primeiro valor e o maior, o segundo e a comparacao entre RJ e outras cidades e o terceiro e a media (denominador)"
print('O maior valor e %i, sendo %.2f vexes a media dos demais, que e %i' % (graf_dados.max(), graf_dados.max()/graf_dados[graf_dados!=graf_dados.max()].mean(), graf_dados[graf_dados!=graf_dados.max()].mean()))
print(graf_dados.max()/graf_dados[graf_dados!=graf_dados.max()].mean())

" ## RECEITA POR PRODUTO ## "

" Criando um filtro para aas colunas que queremos trabalhar (produto_produto e produto_valor) e realizamos a soma na coluna produto_produto"
" Pegamos apenas a coluna produto_valor (apos sum()) para traze-lo para uma seria "
print(df_juncao[['produto_produto', 'produto_valor']].groupby('produto_produto').sum().produto_valor.sort_values(ascending=False))

" Armazenado o groupby de Receita dos Produtos em uma variavel "
graf_dados = df_juncao[['produto_produto', 'produto_valor']].groupby('produto_produto').sum().produto_valor.sort_values(ascending=False)
print(graf_dados)
print(graf_dados.index)
print(graf_dados.values)

" Criando um grafico no matplotlib (Receita dos Produtos)"
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Receita dos Produtos')
plt.show()

" ## CRIANDO UM SUBPLOT ## "

" Definindo o tamanho da area de amostragem do Subplot "
plt.figure(figsize=(10,7))

" Gerando o primeiro plot "
" (linha, coluna, posicao-temos 4 posicoes no total)"
plt.subplot(2,2,1)
graf_dados = df_juncao.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Vendas por Loja')
plt.xticks(rotation=30)

" Gerando o segundo plot "
" (linha, coluna, posicao-temos 4 posicoes no total)"
plt.subplot(2,2,2)
graf_dados = df_juncao.groupby('produto_produto').count().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Vendas por Produto')
plt.xticks(rotation=30)

" Gerando o terceiro plot "
" (linha, coluna, posicao-temos 4 posicoes no total)"
plt.subplot(2,2,3)
graf_dados = df_juncao[['lojas_cidade', 'produto_valor']].groupby('lojas_cidade').sum().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Receita por Loja')
plt.xticks(rotation=30)

" Gerando o quarta plot "
" (linha, coluna, posicao-temos 4 posicoes no total)"
plt.subplot(2,2,4)
graf_dados = df_juncao[['produto_produto', 'produto_valor']].groupby('produto_produto').sum().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index, graf_dados.values)
plt.title('Receita dos Produtos')
plt.xticks(rotation=30)

" Para resolver a sobreposicao do texto e so usar o comando abaixo "
plt.tight_layout()
plt.show()

" ## RECEITA POR CLIENTE ## "

" Fazendo um filtro para acessar as colunas clinte_nome e produto_valor "
print(df_juncao[['clientes_nome','produto_valor']])

""" Fazendo um filtro para acessar a soma de todas as compras feitas por cliente e gerando uma serie usando 
a coluna produto_valor apos sum() (groupby), tambem criando um filtro decrewscente nos valores """
print(df_juncao[['clientes_nome','produto_valor']].groupby('clientes_nome').sum().produto_valor.sort_values(ascending=False))

" Armazenando estes valores filtrados dentro da variavel graf_dados "
graf_dados = df_juncao[['clientes_nome','produto_valor']].groupby('clientes_nome').sum().produto_valor.sort_values(ascending=False)

" Criando um grafico (de linha = Plot) no matplotlib (Receita por ciiente)"
plt.figure(figsize=(15,5))
plt.plot(graf_dados.index, graf_dados.values)
plt.title('Receita por Cliente')
plt.show()

" Criando um grafico mostrando o acumulado da receita, sobre este grafico existente "

" Primeiro definimos duas variaveis (fig e ax) "
fig, ax = plt.subplots(figsize=(15,5))

" Criando o primeiro grafico "
ax.plot(graf_dados.index, graf_dados.values, color='C0')

" Para retirar o eixo (x), devemos inserir o comando abaixo (Grafico 1)"
ax.get_xaxis().set_visible(False)

" Criando o segundo grafico "
" Criando o segundo grafico e informando que serao juntos "
ax2 = ax.twinx()

" print(ax2.plot(graf_dados.index, graf_dados.values, color='C1') ## color = RGB code ## "
" Alterando o segundo grafico para que seja a soma acumulada e porcentagem (dividindo pela suma acumulada * 100) "
ax2.plot(graf_dados.index, (graf_dados.values.cumsum()/graf_dados.values.sum())*100, color='#800080')

" Para retirar o eixo (x), devemos inserir o comando abaixo (Grafico 2)"
ax2.get_xaxis().set_visible(False)

" Definindo que o grafico 2 no eixo y sera porcentagem "
ax2.yaxis.set_major_formatter(PercentFormatter())
plt.title('Receita por Cliente Vs Receita Acumulada %')
plt.show()

" 1/3 dos clientes aproximadamente geram 60% da receita total "
" Gerando numeros para comprovar - Receita acumulada em ordem crescente"
receita_acumulada = graf_dados.cumsum()/graf_dados.sum()
print(receita_acumulada)

" Gerando um filtro para visualizar a receita acumulada em ate 60%"
print(receita_acumulada[receita_acumulada<0.60])

" Gerando um filtro para visualizar a receita acumulada em ate 60% (conta de clientes)"
print(receita_acumulada[receita_acumulada<0.60].count())

" Gerando um filtro para visualizar a receita acumulada em ate 60% (conta de clientes, dividido pelo numero total de clientes)"
print(receita_acumulada[receita_acumulada<0.60].count()/receita_acumulada.count())

" Gerando um filtro para visualizar a receita acumulada em ate 60% (conta de clientes, dividido pelo numero total de clientes) - Percentual"
" Verificamops que 31,70% dos clientes gerar 60% da receita total "
print((receita_acumulada[receita_acumulada<0.60].count()/receita_acumulada.count())*100)

" ## PARETO ## "

" Receita por Produto "
""" Pegamos as colunas (produto_produto, produto_valor), fazemos um groupby da some de  (produto_produto) e 
pegamos a coluna (produto_valor) para converter em uma serie e colocando em ordem decrescente """
graf_dados = df_juncao[['produto_produto', 'produto_valor']].groupby('produto_produto').sum().produto_valor.sort_values(ascending=False)

" Iremos criar 2 graficos "

" Primeiro definimos duas variaveis (fig e ax) "
fig, ax = plt.subplots(figsize=(15,5))

" Criando o primeiro grafico "
ax.bar(graf_dados.index, graf_dados.values, color='#228B22')

" Criando o segundo grafico "
" Criando o segundo grafico e informando que serao juntos "
ax2 = ax.twinx()

" Alterando o segundo grafico para que seja a soma acumulada e porcentagem (dividindo pela suma acumulada * 100) "
" Geramos tambem um marcador para identificar as categorias (marker = 'D')"
ax2.plot(graf_dados.index, (graf_dados.values.cumsum()/graf_dados.values.sum())*100, color='#FFA500', marker='D')

" Definindo que o grafico 2 no eixo y sera porcentagem "
ax2.yaxis.set_major_formatter(PercentFormatter())
" Se quiser alterar os valores min e max do eixo y (lado direito) do grafico, usar o comando abaixo: "
plt.ylim(0,110)
plt.title('Pareto de Receita por Produto')
plt.show()

" ## RECEITA COMBINANDO PRODUTO E LOJA ## "

""" E sempre recomendado usar comando do pandas pois garantem mais performance, porem tambem podemos usar lacos 
(FOR, WHILE, etc) para alcancar os resultados esperados """
"""
" Criando um df com 3 coluna vazias "
graf_dados = pd.DataFrame(columns=('loja', 'produto', 'receita'))

" Vamos preencher os dados de receita com a combinacao loja e produto "
" Criamos 2 lacos FOR com cidade e produto "
for cidade in dflojas.cidade:
    for produto in dfprodutos.produto:
        " adicionamos um dicionario para inserir os dados dentro dos df (cidade e produto) nas colunas (loja, produto e receita) "
        " Para gerar a receita nos devemos aplicar um filtro em produto_valor definindo que o novo df tera (loja_cidade e produto_produto) tenha seus conteudos correspondentes a (cidade e produto) associados e aplicando uma soma no filtro "
        " Incluimos o parametro (ignore_index=True) para nao precisar informar o index do df "
        graf_dados = graf_dados.append({'loja': cidade, 'produto': produto, 'receita': df_juncao.produto_valor[(df_juncao.lojas_cidade == cidade) & (df_juncao.produto_produto == produto)].sum()}, ignore_index=True)
print(graf_dados)

" Antes temos que instalar a biblioteca de graficos (seaborn) pip install seaborn "
" O segundo passo e gerar uma tabela dinamica (pivot_table) "
graf_dados = graf_dados.pivot_table(index='loja', columns='produto', values='receita', aggfunc='sum')

" Gerando um mapa de calor "
" Usamos o parametro cmap para alterar a cor dos dados no mapa "
sns.heatmap(graf_dados)
plt.show()
"""

" Gerando um grafico de barras "

""" E sempre recomendado usar comando do pandas pois garantem mais performance, porem tambem podemos usar lacos 
(FOR, WHILE, etc) para alcancar os resultados esperados """

" Criando um df com 3 coluna vazias "
graf_dados = pd.DataFrame(columns=('loja', 'produto', 'receita'))

" Vamos preencher os dados de receita com a combinacao loja e produto "
" Criamos 2 lacos FOR com cidade e produto "
for cidade in dflojas.cidade:
    for produto in dfprodutos.produto:
        """ adicionamos um dicionario para inserir os dados dentro dos df (cidade e produto) nas colunas 
        (loja, produto e receita) """
        """ Para gerar a receita nos devemos aplicar um filtro em produto_valor definindo que o novo df tera (loja_cidade e produto_produto) 
        tenha seus conteudos correspondentes a (cidade e produto) associados e aplicando uma soma no filtro """
        " Incluimos o parametro (ignore_index=True) para nao precisar informar o index do df "
        graf_dados = graf_dados.append({'loja': cidade, 'produto': produto, 'receita': df_juncao.produto_valor[(df_juncao.lojas_cidade == cidade) & (df_juncao.produto_produto == produto)].sum()}, ignore_index=True)

" Criando um mapa de calor "
#graf_dados = graf_dados.pivot_table(index='loja', columns='produto', values='receita', aggfunc='sum')
#sns.heatmap(graf_dados)
#plt.show()

" Vamos ordenar os dados pela receita (decrescente) "
graf_dados = graf_dados.sort_values(by='receita', ascending=False)
print(graf_dados)

" Criando uma nova coluna com os dados de loja e produto (conjugados) - concatenados "
graf_dados['lojaprod'] = graf_dados.loja + '-' + graf_dados.produto
print(graf_dados)

" Gerando o grafico de barras com uma categoria e um valor (cat, valor)"
plt.figure(figsize=(15,5))
plt.bar(graf_dados.lojaprod, graf_dados.receita)
plt.show()

" Notamos que existem muitos dados com receitas muito pequenas, sendo assim criaremos um filtro com apenas os valores significativos "
plt.bar(graf_dados.lojaprod[graf_dados.receita>0.01*graf_dados.receita.max()], graf_dados.receita[graf_dados.receita>0.01*graf_dados.receita.max()])
plt.show()

plt.figure(figsize=(15,5))
plt.bar(graf_dados.lojaprod[graf_dados.receita>0.01*graf_dados.receita.max()], graf_dados.receita[graf_dados.receita>0.01*graf_dados.receita.max()])
" Para melhorar a visualizacao do grafico, vamos rotacionar os eixos (x, y)"
plt.xticks(rotation=90)
" Aplicar um titulo "
plt.title("Receita por Loja-Produto")
plt.show()