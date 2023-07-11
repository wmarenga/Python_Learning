"""
Oi Wellington.

Quando falamos de DataFrames, a ordem dos dados não nos interessa (normalmente). Pois eles são 
irrelevantes quando aplicamos um filtro.

Porém, se você realmente deseja ordenar seus dados, você pode usar o comando sort_values, veja 
o exemplo abaixo

import pandas as pd
 
df = pd.DataFrame()
 
#criando 3 registros
df = df.append({'Nome':'Rafael', 'classe': 'B'}, ignore_index=True)
df = df.append({'Nome':'Wellington', 'classe': 'A'}, ignore_index=True)
df = df.append({'Nome':'Maria', 'classe': 'A'}, ignore_index=True)
 
#adicionando um registro e ordenando por nome
df = df.append({'Nome':'João', 'classe': 'C'}, ignore_index=True).sort_values('Nome')
 
#reordenando index
df = df.reset_index(drop=True)
 
print(df)

Se você precisa inserir em uma posição específica e não quer ordenar por nome, eu indicaria você criar 
uma nova coluna 'ordem' e sempre definir ela ao inserir, e depois ordenar por ela, caso contrário, você 
teria que trabalhar com o index do dataframe e será mais trabalhoso

Para criar uma nova coluna num lugar específico, você  pode usar o comando INSERT e definir o número da 
posição da coluna no parametro LOC

import pandas as pd
 
df = pd.DataFrame()
 
#criando 3 registros
df = df.append({'Nome':'Rafael', 'classe': 'B'}, ignore_index=True)
df = df.append({'Nome':'Wellington', 'classe': 'A'}, ignore_index=True)
df = df.append({'Nome':'Maria', 'classe': 'A'}, ignore_index=True)
 
#adicionando um registro e ordenando por nome
df = df.append({'Nome':'João', 'classe': 'C'}, ignore_index=True).sort_values('Nome')
 
#reordenando index
df = df.reset_index(drop=True)
 
#adicionar nova coluna antes de classe (loc é o numero da coluna onde vc quer inserir, iniciando em 0)
df.insert(loc=1, column='Idade', value=1)
 
print(df)

loc é a posição da nova coluna (a primeira posição é 0)

value é o valor que será preenchido para todos os registros existentes.

Abraço!

"""
import pandas as pb
df = pb.DataFrame({'nome':['Rafael','Maria','Joao'],'idade':[10,30,20]})
print(df)

""" Alterando o nome de uma celula"""
df.loc[0,'nome'] = 'Rafael2'
print(df)

""" Adicionando uma nova coluna 'sexo' com valores inseridos"""
df['sexo'] = ['M','F','M']
print(df)

""" Adicionando uma nova linha apos a ultima linha"""
df = df.append({'nome':'Ana','idade':15,'sexo':'F'},ignore_index = True)
print(df)

""" Adicionando uma lista com dois valores"""
df = df.append({'nome':['Ana, Tereza'],'idade':15,'sexo':'F'},ignore_index = True)
print(df)
