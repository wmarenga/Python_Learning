import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo_Excel ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 44 (Dados Nulos)/caso_estudo.xlsx'
dfclientes = pd.read_excel(caminho_arquivo_Excel, sheet_name='clientes')
dflojas = pd.read_excel(caminho_arquivo_Excel, sheet_name='lojas')
dfprodutos = pd.read_excel(caminho_arquivo_Excel, sheet_name='produtos')
dfvendas = pd.read_excel(caminho_arquivo_Excel, sheet_name='vendas')
dfpagamentos = pd.read_excel(caminho_arquivo_Excel, sheet_name='pagamentos')

" Com este comando, criamos um filtro dos dados nulo no DF"
print(dfclientes[dfclientes.isnull().T.any()])

" Filtrar um id do cliente especifico "
print(dfvendas[dfvendas.id_cliente == 264])

" Substituir danos nulos (NaN) que poderao ser rastreados no futuro "
" Acessa o dado pelo index (1 - index da linha - primeira coluna) e o nome da coluna que desejamos filtrar"
" O comando .loc e mais adequado quando queremos fazer uma substituicao de um registro, evitando assim erros "
print(dfclientes.loc[1,'nome'])

" Tambem podemos acessar citando o no me da coluna e informando o index dentro de []"
print(dfclientes.nome[1])

" O comando loc e mais indicado para fazer uma substituicao de um registro"
" Este comando busca todos os registros nulos na linha em determinada coluna (nome, sexo, dt_nasc) [linhas, colunas]"
dfclientes.loc[dfclientes.nome.isnull(), 'nome'] = 'Sem Nome'
dfclientes.loc[dfclientes.sexo.isnull(), 'sexo'] = 'O'

" As datas sao mais complexas, pois devemos manter o mesmo padrao (dd/mm/aaaa, mm/dd/aaaa)"
" Inserimos uma data para indicar que o cliente tem apenas 1 ano, sendo assim inconsistente "
dfclientes.loc[dfclientes.dt_nasc.isnull(), 'dt_nasc'] = '1/1/2020'

" Para verificar, vamos pegar dois index (ja alterados) para verificar. Ex. 269 e 287"
" Acrescentamos outros colchetes dentro do colchete do loc das linha e : para exibir qualquer valor nas colunas"
" Estamos utilizando o index do DataFrame (primeira coluna) e nao o id da planilha "
print(dfclientes.loc[[269,287], :])

" Com este procedimento, foram retirados todos os dados nulos do DF "
" Quando aplicamos a sum(), nos estamos somando quantos verdadeiros existem no DataFrame"
print(dfclientes.isnull())

print(dfclientes.isnull().sum())

" Os outros Dfs ja nao possuem dados nulosm conferindo"
print(dflojas.isnull().sum())
print(dfvendas.isnull().sum())
print(dfpagamentos.isnull().sum())
print(dfprodutos.isnull().sum())