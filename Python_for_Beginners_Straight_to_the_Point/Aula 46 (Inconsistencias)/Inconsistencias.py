import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 46 (Inconsistencias)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

""" Verificar a consistencia dos dados de uma tabela e garantir que uma tabela consegue se comunicar com a outra, ou
se existem dados faltantes ou nao se conectam entre si."""

" Buscar por vendas que nao possuem clientes (dfvendas x dfclientes) "
" Este comando faz um Procv entre duas tabelas "
print(dfvendas.id_cliente.isin(dfclientes.id))

" Negativa, acrescentar o ~ (dfvendas x dfclientes), any(), verifica se existe algum valor verdadeiro "
print(~dfvendas.id_cliente.isin(dfclientes.id).any())

" Para lista com filtro se todos os id_cliente de dfvendas estao em id de dfclientes (dfvendas x dfclientes) "
print(dfvendas[~dfvendas.id_cliente.isin(dfclientes.id)])

" Para lista com filtro se todos os id_loja de dfvendas estao em id de dflojas (dfvendas x dflojas) "
print(dfvendas[~dfvendas.id_loja.isin(dflojas.id)])

" Para lista com filtro se todos os id_produto de dfvendas estao em id de dfprodutos (dfvendas x dfprodutos) "
print(dfvendas[~dfvendas.id_produto.isin(dfprodutos.id)])

" Tambem podemos aplicar um count() para ver todos dados por ids"
print(dfvendas[~dfvendas.id_cliente.isin(dfclientes.id)].count())

" Buscar pagamentos que possivelmente nao tem id_venda "
" O dfpagamentos possui apenas id_vendas relacionado com dfvendas"
" Para lista com filtro se todos os id_cliente de dfvendas estao em id de dfclientes (dfvendas x dfclientes) "
print(dfpagamentos[~dfpagamentos.id_venda.isin(dfvendas.id)])

" Verificar se todas as vendas geraram pagamentos. Vendas que nao estao registradas nos pagamentos "
print(dfvendas[~dfvendas.id.isin(dfpagamentos.id_venda)])
" Tambem podemos aplicar um count() para ver todos dados por ids (928 vendas sem pagamentos)"
print(dfvendas[~dfvendas.id.isin(dfpagamentos.id_venda)].count())