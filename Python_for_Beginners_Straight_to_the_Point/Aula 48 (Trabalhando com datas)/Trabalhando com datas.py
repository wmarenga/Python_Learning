""" 
Olá Wellington, tudo bom?

Se você desejar ver mais registros, você pode usar o comando (antes de imprimir o DataFrame)

pd.set_option('display.max_rows', 10)

Sendo 10 o número de linhas que deseja visualizar do dataframe


No caso, se você tivesse algum registro de data que não fizesse sentido, o Python deveria retornar essa mensagem
time data 'SEU TEXTO' does not match format '%m/%d/%Y' (match)


Eu rodei seu código e aqui pra mim aparece como um DataFrame vazio

dfclientes[dfclientes.dt_nasc != (pd.to_datetime(dfclientes.dt_nasc, format='%m/%d/%Y'))]


Nele você está verificando se algum dado na coluna dt_nasc é diferente dele mesmo, porém convertido.

Para fazer o teste que você deseja, eu aconselho usar o comando isnan().

dfclientes.isna.any()


Assim você irá verificar que não existe um NaN


Talvez, no seu caso apareceu, pois pode ter pulado alguma etapa, como, por exemplo, essa etapa

dfClientes.loc[dfClientes.dt_nasc.isnull(),'dt_nasc'] = '1/1/2020'

Confira isso por favor. Se não encontrar o problema, me envie seu código/notebook para rafaelcxc@gmail.com que posso te ajudar.

Abraços
"""
import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 48 (Trabalhando com datas)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

""" 
Comando para ver mais dados:
pd.set_option('display.max_rows', 10)
"""

" Verificar se existe alguma inconsistencia nas datas "

print(dfclientes)

" Alterando o formato da data para o padrao do pandas (yyyy-mm-dd)"
""" E muito importante que as datas estejam no mesmo formato, pois futuramente poderiamos fazer soma, subtracao e outras
operacoes entre as datas"""
dfclientes.dt_nasc = pd.to_datetime(dfclientes.dt_nasc, format= '%m/%d/%Y')
print(dfclientes[dfclientes.dt_nasc != (pd.to_datetime(dfclientes.dt_nasc, format='%m/%d/%Y'))])
print(dfclientes.dt_nasc[~dfclientes.dt_nasc.isin(pd.to_datetime(dfclientes.dt_nasc, format='%m/%d/%Y'))].count())
print(dfclientes)

" Analisando o dfvendas, percebemos que as datas estao no formato correto (yyyy-mm-dd)"
print(dfvendas.dt_venda[~dfvendas.dt_venda.isin(pd.to_datetime(dfvendas.dt_venda, format='%m/%d/%Y'))].count())
print(dfvendas)

" Analisando o dfpagamentos, percebemos que as datas estao no padra do pandas (yyyy-mm-dd)"
print(dfpagamentos.dt_pgto[~dfpagamentos.dt_pgto.isin(pd.to_datetime(dfpagamentos.dt_pgto, format='%m/%d/%Y'))].count())
print(dfpagamentos)

" Analisando o dfprodutos, nao temos datas"
print(dfprodutos)

" Analisando o dflojas, nao temos datas"
print(dflojas)