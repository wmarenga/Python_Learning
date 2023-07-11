import pandas as pd
dados_pessoas = pd.read_excel('dados.xlsx', sheet_name='pessoas')
dados_notas = pd.read_excel('dados.xlsx', sheet_name='notas')

" O comando .set_index vai indicar qual e a variavel chave que servira de referencia para as duas tabelas "
dados_todos = dados_notas.set_index('nome').join(dados_pessoas.set_index('nome'))

medias = dados_todos.groupby('nome').nota.mean()

medias.to_excel('saida.xlsx')