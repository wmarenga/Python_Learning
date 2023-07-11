import pandas as pd
caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 19 (Join_pandas)/caso_estudo.xlsx'
pessoas = pd.read_excel(caminho_arquivo,sheet_name='pessoas',engine='openpyxl')
covid = pd.read_excel(caminho_arquivo,sheet_name='registros_covid',engine='openpyxl')

print(pessoas.head())
print(covid.head())

"Substituindo o index do Python (0,1,2...) pelo index da planilha (id)"
pessoas = pessoas.set_index('id')
print(pessoas)

covid = covid.set_index('id')
print(covid)

"""Desta maneiro o (id_pessoa) sera utilizado provisoriamente como referencia das duas tabelas juntas
Sera associado o id (na tabela pessoas) com o id_pessoa da tabela covid"""
df = pessoas.join(covid.set_index('id_pessoa'))
print(df)

"Desta maneira as tabelas sao unidas utilizando a coluna id de cada uma"
df1 = pessoas.join(covid)
print(df1)

"Como retirar ou substituir os dados (NqN - sem valor apos o join)"
df = df.fillna('Sem informacao')
print(df)

"Mostrar a media das severidades"
print(df.groupby('severidade').idade.mean())
