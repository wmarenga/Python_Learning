from itertools import groupby
import pandas as pd
caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 18 (Group By_pandas)/caso_estudo.xlsx'
pessoas = pd.read_excel(caminho_arquivo,sheet_name='pessoas',engine='openpyxl')
covid = pd.read_excel(caminho_arquivo,sheet_name='registros_covid',engine='openpyxl')

"""O comando groupby() sozinho nao significa nada, temos que aplicar alguma operacao 
matematica para que ele faca sentido (mean()-media, min() - valor minimo, max() e count())"""

print(pessoas.groupby('sexo').mean())

"""Como a coluna (id) nao e significativa, inclimos idade antes de .mean() para especificar a 
coluna que queremos"""

print(pessoas.groupby('sexo').idade.mean())

"""Inserir uma coluna chamada (inicial) com as primeiras letras do nomes"""

pessoas['inicial'] = pessoas.nome.str[0]
print(pessoas)

"""Pegar apenas a coluna inicial, pegando as idade associadas a inicial e aplicando uma media"""

print(pessoas.groupby('inicial').idade.mean())
