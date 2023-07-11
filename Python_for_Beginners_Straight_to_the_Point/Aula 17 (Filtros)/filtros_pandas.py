import pandas as pd
caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 17 (Filtros)/caso_estudo.xlsx'
pessoas = pd.read_excel(caminho_arquivo,sheet_name='pessoas',engine='openpyxl')
covid = pd.read_excel(caminho_arquivo,sheet_name='registros_covid',engine='openpyxl')

"Todas as linha com pessoas com idades > 40 anos"
print(pessoas[pessoas.idade>40])

"Contagem de dados em cada coluna de pessoas com idades > 40 anos"
print(pessoas[pessoas.idade>40].count())

"Contagem de dados em uma coluna (id) de pessoas com idades > 40 anos"
print(pessoas.id[pessoas.idade>40].count())

"Lista de nomes de pessoas com idade igual a 48 anos"
print(pessoas.nome[pessoas.idade==48])

"Media das pessoas do sexo feminino"
print(pessoas.idade[pessoas.sexo=='F'].mean())

"Nome da pessoas que comecam com a letra (A)"
print(pessoas[pessoas.nome.str[0]=='A'])

"Nome da pessoas que comecam com (Ana)"
print(pessoas[pessoas.nome.str[0:3]=='Ana'])

"Todas as linha com pessoas com idades > 10 anos"
print(pessoas[pessoas.idade>10])