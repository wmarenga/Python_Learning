import pandas as pd
caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 20 (novas features)/caso_estudo.xlsx'
pessoas = pd.read_excel(caminho_arquivo,sheet_name='pessoas',engine='openpyxl')
covid = pd.read_excel(caminho_arquivo,sheet_name='registros_covid',engine='openpyxl')

print(pessoas.head())
print(covid.head())

pessoas = pessoas.set_index('id')
covid = covid.set_index('id')

df = pessoas.join(covid.set_index('id_pessoa'))

df = df.fillna(0)

print(df)

"Criar uma coluna (faixa_etaria) com todos os valores (jovem)"
df['faixa_etaria'] = 'jovem'
print(df.head())

"Inserindo um dados na coluna df.loc[linha,coluna] com filtro (criterio)"

df.loc[df.idade>24,'faixa_etaria'] = 'adulto'
df.loc[df.idade>45,'faixa_etaria'] = 'adulto2'
print(df.head())

"Aplicando o groupby para saber a media"
print(df.groupby('faixa_etaria').mean())

"Alterar os dados da coluna severidade para numeros, quando (severidade == 'baixa') vou alterar para 1"
df.loc[df.severidade=='baixa','severidade'] = 1
df.loc[df.severidade=='alta','severidade'] = 2
print(df.head())
"As medias da coluna severidade ainda nao aparecem pois precisamos converter para numeros inteiros"
print(df.groupby('faixa_etaria').mean())

"Convertendo os dados da coluna (severidade) para numeros"
df['severidade']=df['severidade'].astype(int)
print(df.groupby('faixa_etaria').mean())
