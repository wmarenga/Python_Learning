import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 49 (Definindo Indexes)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

" ### Com este procedimento criaremos uma chave primaria que seja a referencia de todas as linhas ### "

" A primeira coluna e sempre gerada pelo pandas e a segunda coluna foi extraida da planilha importada do Excel, CSV e etc "
" Para facilitar a manipulacao dos dados devemos substituir o index gerado pelo pandas pelo index do Excel "
dfclientes = dfclientes.set_index('id')
print(dfclientes)

""" Importante observar que nao mais conseguimos acessar a coluna (id) pelo dfclientes.id somente conseguimos 
acessar pelo comando dfclientes.index. A coluna id nao existe mais, ela virou o index da planilha."""
print(dfclientes)

" Fazemos o mesmo para dflojas, dfprodutos, dfvendas e dfpagamentos"
print(dflojas)
print(dfprodutos)
print(dfvendas)
print(dfpagamentos)
dflojas = dflojas.set_index('id')
dfprodutos = dfprodutos.set_index('id')
dfvendas = dfvendas.set_index('id')
dfpagamentos = dfpagamentos.set_index('id')
print(dfclientes)
print(dflojas)
print(dfprodutos)
print(dfvendas)
print(dfpagamentos)