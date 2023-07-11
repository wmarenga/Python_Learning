import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 42 (Analise preliminar das bases)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

" ## Analise Preliminar ## "

" 5 dados aleatorios "
print(dfclientes.sample(5))

" 5 dados iniciais "
print(dfclientes.head(5))

" 5 ultimos dados "
print(dfclientes.tail(5))

" Verificar se existe algum dados nulo. Se tivessemos algum dados True (seria nulo)"
print(dfclientes.isnull())

" Aplicaremos uma soma (sum) para verificar quantos dados nulos nos temos da tabela "
print(dfclientes.isnull().sum())

" Vamos transpor a tabela para ver horizontalmente. Com este comando invertemos as linhas e colunas "
print(dfclientes.isnull().T)

" Para cada linha existe a informacao se temos algum registro nulo"
print(dfclientes.isnull().T.any())

" Com este comando, criamos um filtro dos dados nulo no DF"
print(dfclientes[dfclientes.isnull().T.any()])

" Avaliando os valores unicos (descobrimos que temos F, M e nan)"
print(dfclientes.sexo.unique())

" Avaliando o DF lojas "
print(dflojas)

" Avaliando o DF produtos "
print(dfprodutos)

" Verificamos se os valores foram identificados como numeros "
print(dfprodutos.describe())

" Exibimos um grafico com somente a coluna (valor. As bolinhas mostram dados fora do nosso conjunto de dados"
dfprodutos.boxplot(column=['valor'])
plt.show()

" Identificar o registro fora do grupo de dados sem explorar a tabela toda (criamos um filtro)"
print(dfprodutos[dfprodutos.valor>3000000])

" Gerar um BOXPLOT desconsiderando este valor (9  10  xxx-231a  3211352.0)"
dfprodutos[dfprodutos.valor<3000000].boxplot(column=['valor'])
plt.show()

" Verificar se o produto (xxx-231a) foi realmente vendido no dfvendas "
" Existem 182 vendas deste produto, sendo assim precisamos perguntar para o especialista "
print(dfvendas[dfvendas.id_produto==10].count())

" Avaliando divegencias e valores nulos na tabela de vendas "
" Nao existem dados nulos pois os registros foram gerados por computador "
print(dfvendas.isnull().sum())
print(dfvendas.describe())

" Avaliando do dfpagamentos "
print(dfpagamentos.isnull().sum())
print(dfpagamentos.describe())

"""
print(dfclientes)
print(dflojas)
print(dfprodutos)
print(dfvendas)
print(dfpagamentos)

"""