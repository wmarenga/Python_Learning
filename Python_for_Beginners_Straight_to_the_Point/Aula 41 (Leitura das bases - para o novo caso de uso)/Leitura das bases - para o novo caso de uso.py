import pandas as pd

"A proxima etapa e ler o arquivo Excel (xlsx)"
caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 41 (Leitura das bases - para o novo caso de uso)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')
print(dfclientes)
print(dflojas)
print(dfprodutos)
print(dfvendas)
print(dfpagamentos)

"A leitura dos arquivos CSV tambem e bem simples"
""" O Excel e limitado a 1 millhao de linhas, enquanto que o csv tem um limite muito maior
podemos trabalhar com dados em csv de gigabites"""
caminho_arquivo_csv_clientes = 'D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 41 (Leitura das bases - para o novo caso de uso)/caso_estudo_clientes.csv'
caminho_arquivo_csv_lojas = 'D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 41 (Leitura das bases - para o novo caso de uso)/caso_estudo_lojas.csv'
caminho_arquivo_csv_pagamentos = 'D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 41 (Leitura das bases - para o novo caso de uso)/caso_estudo_pagamentos.csv'
caminho_arquivo_csv_produtos = 'D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 41 (Leitura das bases - para o novo caso de uso)/caso_estudo_produtos.csv'
caminho_arquivo_csv_vendas = 'D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 41 (Leitura das bases - para o novo caso de uso)/caso_estudo_vendas.csv'

"O separador padrao do csv e virgula, porem se o arquivo csv tiver ponto e virgula, use o parametro sep=';'"
dfclientes_csv = pd.read_csv(caminho_arquivo_csv_clientes, sep=';')
dflojas_csv = pd.read_csv(caminho_arquivo_csv_lojas, sep=';')
dfprodutos_csv = pd.read_csv(caminho_arquivo_csv_pagamentos, sep=';')
dfvendas_csv = pd.read_csv(caminho_arquivo_csv_produtos, sep=';')
dfpagamentos_csv = pd.read_csv(caminho_arquivo_csv_vendas, sep=';')
print(dfclientes_csv)
print(dflojas_csv)
print(dfprodutos_csv)
print(dfvendas_csv)
print(dfpagamentos_csv)

" Se apresentar algum problema da biblioteca xlrd, instale (pip install xlrd) "
