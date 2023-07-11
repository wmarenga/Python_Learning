" Lendo arquivo Excel "
import sys, os
import pandas as pd

" Adicionar um diretorio padrao no pythonpath "
sys.path.insert(0,'d:\\23) Programação\\Cursos\\Python\\5) Analise de dados com Python e Machine Leearning')

" Linha de comando para chamar um modulo externo "
sys.path.insert(0,os.path.abspath(os.curdir))

dados_pessoas = pd.read_excel('dados.xlsx', sheet_name='pessoas')
dados_notas = pd.read_excel('dados.xlsx', sheet_name='notas')
print(dados_pessoas)
print(dados_notas)

" Juntando as duas tabelas "
" Temos que definir qual vai ser a variavel chave, neste caso sera 'nome' - para as duas tabelas "
dados_todos = dados_notas.set_index('nome').join(dados_pessoas.set_index('nome'))
print(dados_todos)

" Calculando a medias das notas "
medias = dados_todos.groupby('nome').nota.mean()
print(medias)

" Calculando a medias das idades "
medias = dados_todos.groupby('nome').idade.mean()
print(medias)

" Verificando o valor maximo das notas de cada pessoa "
medias = dados_todos.groupby('nome').nota.max()
print(medias)

" Salvando as medias no Excel "
medias.to_excel('saida.xlsx')