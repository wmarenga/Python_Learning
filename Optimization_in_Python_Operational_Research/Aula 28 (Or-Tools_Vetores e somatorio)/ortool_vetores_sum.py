import pandas as pd, numpy as np
import ortools.linear_solver.pywraplp as otlp

#entrada

caminho_arquivo = 'D:\\23) Programação\\Cursos\\Python\\6) Otimizacao em Python_Pesquisa Operacional\\Aula 28 (Or-Tools_Vetores e somatorio)\\inputs_dados.xlsx'
dados_ger = pd.read_excel(caminho_arquivo, sheet_name='geracao')
dados_carga = pd.read_excel(caminho_arquivo, sheet_name='carga')
dados_dep = pd.read_excel(caminho_arquivo, sheet_name='dependencia')

" Com este comando verificamos o numero de linhas da tabela = numero de geradores (Ng)"
Ng = len(dados_ger)

" Criacao do modelo "
solver = otlp.Solver('teste', otlp.Solver.GLOP_LINEAR_PROGRAMMING)

#entrada
" np.zeros(5), criamos uma matriz linha com zeros [0,0,0,0,0] "
""" np.zeros(2,5), criamos uma matriz com 2 linha e 5 colunas com zeros [0,0,0,0,0] 
                                                                        [0,0,0,0,0]"""
" np.zeros(Ng) sendo que Ng e igual a 5 "
" O comando .tolist() faz o array virar uma lista "
Pg = np.zeros(Ng).tolist()

" Definindo que (Pg) e uma variavel de otimizacao "
for g in range(Ng):
    " solver.NumVar(limite inferior, limite superior, nome da variavel)"
    " 'Pg[{}]' ficara fora do loop, sendo assim substituimos o (g) por {} "
    " .format([g]), estaremos definindo que as {} devem ser alteradas por (g) "
    """ Em "float(dados_ger.maximo[g])", estaremos acessando linha alinha da coluna maximo de (dados_ger) e 
    convertendo para float para evitar erros """
    Pg[g] = solver.NumVar(0, float(dados_ger.maximo[g]),'Pg[{}]'.format([g]))
    
""" Se quisermos acrescentar mais uma dimensao (variavel de otimizacao tempo(t)), com 3 periodos. Teriamos 
entao o numero de geradores (Ng) e o tempo (t) """

" np.zeros(Ng) sendo que Ng e igual a 5 "
" Acrescentariamos [3 linhas, Ng colunas]"
" O comando .tolist() faz o array virar uma lista "
#Pg = np.zeros([3,Ng]).tolist()

#for t in range(3):
# for g in range(Ng):
" solver.NumVar(limite inferior, limite superior, nome da variavel)"
" 'Pg[{}]' ficara fora do loop, sendo assim substituimos o (g) por {} "
" .format([g]), estaremos definindo que as {} devem ser alteradas por (g) "
""" Em "float(dados_ger.maximo[g])", estaremos acessando linha alinha da coluna maximo de (dados_ger) e 
convertendo para float para evitar erros """
" Acrescentamos [t] (Pg[t][g]) e .format([t,g]), acrescentamos o t dentro do [] "
    #Pg[t][g] = solver.NumVar(0, float(dados_ger.maximo[g]),'Pg[{}]'.format([t,g]))

#restrições
" Somatoria de geracao (sum([Pg[g] for g in dados_ger.id]) = somatoria de carga (sum(dados_carga.valor)) "
" Somatorio de geracao ([Pg[0] + Pg[1] + Pg[2] + Pg[3] + Pg[4]])"
solver.Add(sum([Pg[g] for g in range(Ng)])==sum(dados_carga.valor))

for c in dados_dep.carga.unique():
    solver.Add(float(dados_carga.valor[c]) <= sum([Pg[g] for g in dados_dep.gerador[dados_dep.carga==c]]))

#obj
solver.Minimize(sum([Pg[g]*float(dados_ger.custo[g]) for g in range(Ng)]))

" Executando o solver"
results = solver.Solve()

" Verificando se o valor otimo foi encontrado "
if results == otlp.Solver.OPTIMAL:
    print('Resultado ## Otimo ## encontrado')
else:
    print('Resultado Não encontrado')

" Imprimindo o valor das variaveis "
" As variaveis encontradas estao dentro de Pg[Ng] que e um vetor "
for g in range(Ng):
    print('Pg[%i] = %.2f' % (g,Pg[g].solution_value()))

" Verificamos que o gerador mais caro e o gerador 3 com custo 0.50 "
" O custo de gerador 2 e mais barato 0.30 (verificar porque o gerador 1 nao foi considerado o mais barato "
print(dados_ger)
