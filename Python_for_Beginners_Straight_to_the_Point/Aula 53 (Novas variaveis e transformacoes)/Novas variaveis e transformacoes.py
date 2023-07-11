""" 
Criando novos dados (Feature Engineering)
1) Faca perguntas que voce gostaria de responder.
- Quais lojas mais vendem?
- Quais produtos mais vendem?
- Quais lojas geram maior receita?
- Quais produtos geram maior receita?
- Existe algum cliente que mais realiza compras?
- Existe alguma relacao entre loja e cliente?
- Qual o tempo medio entre compra e pagamento? (tempo_pg = dt_pag - dt_compra)
- Existe alguma loja em que esse tempo e menor? E produto?
- Qual produto mais gera inadimplencia? (pg)
- Qual loja tem mais inadimplencias?
- Existe alguma relacao entre idade e inadimplencia? (cliente_idade)
- E possivel prever inadimplencia atraves dos dados idade, cidade e produto?

2) Gere novos dados ou transforme.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 50 (Join)/caso_estudo.xlsx'
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

" ## Feature Engineering ## "

""" Incluindo uma nova coluna de pagamentos (pg) e defimimdo com 1 para dizer que todas as vendas 
tiveram pagamentos """
df_juncao['pg'] = 1
print(df_juncao)

""" Alterando todos os registros sem pagamentos para 'Inadimplente'
df.loc[nome_linha, nome_coluna]"""
df_juncao.loc[df_juncao.dt_pgto.isnull(), 'pg'] = 0
print(df_juncao)

" Criando o dados de tempo de pagamento "
tempo_pgto = df_juncao.dt_pgto - df_juncao.dt_venda
print(tempo_pgto)

" Retirando o (days) do DataFrame, fazendo com que a informacao seja convertida para numeros "
df_juncao['tempo_pg'] = (df_juncao.dt_pgto - df_juncao.dt_venda).dt.days
print(df_juncao)

" Criando a idade dos clientes (O comando 'pd.to_datetime('today')' pega a data atual"
" Usamos estecomando do numpy para converter para anos (/np.timedelta64(1,'Y')"
print(dfclientes.dt_nasc)
print((pd.to_datetime('today') - dfclientes.dt_nasc)/np.timedelta64(1,'Y'))

" Acrescentando no inicio da sequencia de comando o comando (np.floor), teremos um arredondamento para baixo"
print(np.floor((pd.to_datetime('today') - dfclientes.dt_nasc)/np.timedelta64(1,'Y')))

" Armazenando os dados gerados em uma nova coluna chamada ('cliente_idade')"
df_juncao['cliente_idade'] = np.floor((pd.to_datetime('today') - dfclientes.dt_nasc)/np.timedelta64(1,'Y'))
print(df_juncao)