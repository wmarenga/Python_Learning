import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 47 (Dados duplicados)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

" Verificar se existe algum dado duplicado "

" Analisando em clientes se existe algum nome duplicado "
print(dfclientes.nome.duplicated())
" Somando as incidencias de nome duplicados "
print(dfclientes.nome.duplicated().sum())
" Aplicando um filtro para visualizar os nomes duplicados "
print(dfclientes[dfclientes.nome.duplicated()])
" Analisando um registro especifico "
print(dfclientes[dfclientes.nome == "Anna Melo"])

" Verificar se alguma linha se repete "
print(dfclientes.id.duplicated())
print(dfclientes.duplicated())

" Verificar se alguma linha se repete aplicando uma soma "
print(dfclientes.id.duplicated().sum())
print(dfclientes.duplicated().sum())

""" Retirando (desconsiderando) a coluna (id) 'ou linha para' evitar divergencia da informacao. Estamos 
considerando apenas o index gerado pelo data frame. """
" axis (0 - linha, 1 - coluna"
print(dfclientes.drop('id', axis=1).duplicated().sum())

" Verificando se existe algum nome de produto duplicado em dfprodutos"
print(dfprodutos.produto.duplicated().sum())

" Verificando se existe alguma cidade duplicada em dflojas"
print(dflojas.cidade.duplicated().sum())

" Analisando o dfvendas, primeiro desconsideramos a coluna id (deixando apenas o index do df)"
print(dfvendas.drop('id',axis=1).duplicated().sum())

" Aplicando um filtro, conseguimos visualizar os dados duplicados "
print(dfvendas[dfvendas.drop('id',axis=1).duplicated()])

" Aplicando um filtro, conseguimos visualizar os dados duplicados (clinte especifico)"
""" Como neste caso e uma venda, nao conseguimos avaliar se o cliente fez 2 compras do mesmo produto ou 
se existe alguma inconsistencia nas vendas duplicadas """
print(dfvendas[(dfvendas.id_cliente==559) & (dfvendas.id_loja==2) & (dfvendas.id_produto==5)])

" Verificando o dfpagamentos "
print(dfpagamentos)
print(dfpagamentos.drop('id', axis=1).duplicated().sum())