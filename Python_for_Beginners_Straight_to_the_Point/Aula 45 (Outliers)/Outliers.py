import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 45 (Outliers)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

""" A busca por OUTLIERS deve ser feita apenas para dados numericos, em raros casos, tambem podem ser usados em datas 
muito fora do padrao. """
" Vamos verificar oa dados de todos os DFs"

"Nao possui nenhum dado numerico, exceto o id"
print(dfclientes)
"Nao possui nenhum dado numerico, somente string"
print(dflojas)
"Nao possui nenhum dado numerico, somente string"
print(dfvendas)
"Nao possui nenhum dado numerico, somente string"
print(dfpagamentos)

" Possui nenhum dado numerico na coluna (valor)"
" O DF produtos e o unico com dados numericos que precisam ser analizados"
" Observamos um nome do produto muito estranho que precisamos verificar com um especialista"
" Outro dados nao usual e o produto estar custando mais de 3 milhoes"
print(dfprodutos)

" Devem[os manipular o dado para chegar a um numero proximo ao real (de preferencia com a orientacao de um especialista)"
" Buscando a informacao no index 9 e coluna (valor) [9,'valor']"
dfprodutos.loc[9,'valor'] = dfprodutos.valor[9]/10000
print(dfprodutos)

" Plotando os novos dados apos altera-los"
dfprodutos.boxplot(column=['valor'])
plt.show()