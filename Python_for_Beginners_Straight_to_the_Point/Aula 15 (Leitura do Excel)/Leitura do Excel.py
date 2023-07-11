"""
Error possiveis:

1) Erro de (xlrd):
    pip install xlrd (no prompt de comando)
2) Erro engine:
    pip install openpyxl (no prompt de comando)
    e acrescentar , (,engine='openpyxl')
3) Se tiver um arquivo .CSV, use o comando (pb.read_csv)

"""

import pandas as pd
caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 15 (Leitura do Excel)/caso_estudo.xlsx'
pessoas = pd.read_excel(caminho_arquivo,sheet_name='pessoas',engine='openpyxl')
covid = pd.read_excel(caminho_arquivo,sheet_name='registros_covid',engine='openpyxl')
print(pessoas)
print(covid)
