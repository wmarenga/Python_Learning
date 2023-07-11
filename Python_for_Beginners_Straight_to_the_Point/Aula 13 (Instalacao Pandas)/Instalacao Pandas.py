"""
Instalacao do Pandas:
1) Abrir p Prompt de comandos como administrador
2) Digitar:
$ pip install pandas
3) Usar o (import pandas as pb) para solicitar a biblioteca na primeira linha de comandos
4) Dentro do pandas temos uma estrutura de tabela chamada (DataFrame)
5) Criamos uma variavel (df) e dentro das chaves (dicionarios)
df = pb.DataFrame({'nomes':['Rafael','Maria','Joao'],'idade':[10,30,20]})
"""
import pandas as pb
df = pb.DataFrame({'nome':['Rafael','Maria','Joao'],'idade':[10,30,20]})
print(df)

print(df.idade[0])

print(df.idade[1])
print(df['idade'][1])
print(df.loc[1,'idade'])

print(df.idade.min())
print(df.idade.max())
print(df.idade.mean())
