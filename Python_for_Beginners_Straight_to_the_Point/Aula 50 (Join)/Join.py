import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 50 (Join)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

""" Juncao de Bases (Data Fusion): 
- Join
- Dados nulos e zerados

Antes de tudo, devemos identificar qual e a base que gera a informacao principal. A tabela de clientes e apenas
um cadastro. A tabela de vendas possui infomacoes estrategicas para nossa analise. 
"""

"""
Existe uma maneira de conectar bases sem setar o index antes:
dfvendas = dfvendas.set_index('id_cliente').join(dfclientes.set_index('id'))
"""

" Antes de juntar as tabela, devemos substituir o index do pandas pelo index do Excel"
dfclientes = dfclientes.set_index('id')
dflojas = dflojas.set_index('id')
dfprodutos = dfprodutos.set_index('id')
dfvendas = dfvendas.set_index('id')
dfpagamentos = dfpagamentos.set_index('id')

print(dfvendas)

""" Juntamos a tabela principal (dfvendas) com o (dfclientes), determinando qual e a coluna (on='id_cliente') que conecta o index
do dfclientes
"""
dfvendas = dfvendas.join(dfclientes, on='id_cliente')
print(dfvendas)

""" Poderiamos tambem adicionar um prefixo a estas novas colunas """
" Criamos uma nova variavel df_juncao para guardar o novo df(unido) tendo como referencia a coluna (id_cliente)"
df_juncao = dfvendas.join(dfclientes.add_prefix('clientes_'), on='id_cliente')
print(df_juncao.columns)
print(df_juncao)

" Precisamos unir as informacoes do dflojas em df_juncao tendo como referencia a coluna (id_loja)"
df_juncao = df_juncao.join(dflojas.add_prefix('lojas_'), on='id_loja')
print(df_juncao)

" Precisamos tambem unir as informacoes do dfprodutos em df_juncao tendo como referencia a coluna (id_produto)"
df_juncao = df_juncao.join(dfprodutos.add_prefix('produto_'), on='id_produto')
print(df_juncao)

"""
Para exportar para um arquivo Excel novo, usamos o comando abaixo:
df_juncao.to_excel('D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 50 (Join)/join_vendas.xlsx', index=False)
"""

" Buscando um registro dentro de dfclientes para validar as informa'c|oes do join "
print(dfclientes.loc[393])

print(dfpagamentos)

" Com este comando nos garantimos que index id_venda e o mesmo  do id do df_juncao"
" Os dados com NaT sao dados nulos ou invalidos"
df_juncao = df_juncao.join(dfpagamentos.set_index('id_venda'))

print(df_juncao)