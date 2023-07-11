""" 
Explorando o Pyomo

Queremos minimizar o custo de cada gerador vezes a sua potencia gerada (min Cg x Pg)
Pg tem que ser maior que zero ==> Pg (ig) >-= 0
Pg esta limitada ao consumo do gerador ==> Pg (ig) <= Pg (ig) LIM

Cg - Custo de cada gerador
Pg - Potencia gerada
Pc - Potencia por carga
ig - indice que percorre os geradores
ic - indice de consumo

"""
import pandas as pd
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

#Leitura de dados de entrada
" Tambem poderiamos utilizar dados orientados a objeto (dados.ger, dados.carga. dados.dep) "
caminho_arquivo = 'D:\\23) Programação\\Cursos\\Python\\6) Otimizacao em Python_Pesquisa Operacional\\Aula 24 (Pyomo_ Vetores e Somatorio)\\inputs_dados.xlsx'
dados_ger = pd.read_excel(caminho_arquivo, sheet_name='geracao')
dados_carga = pd.read_excel(caminho_arquivo, sheet_name='carga')
dados_dep = pd.read_excel(caminho_arquivo, sheet_name='dependencia')

" Com este comando verificamos o numero de linhas da tabela = numero de geradores (Ng)"
Ng = len(dados_ger)

model = pyo.ConcreteModel()

" Criacao da variavel de otimizacao "
" Pc (informacao fornecida), Cg (informacao fixa e fornecida), a unica variavel de otimizacao e Pg "
" range(Ng) define que a variavel e um vetor "
" O limite inferior e zero, mas o limite superior depende do gerador Nome=liberado (bounds=(0, None)"
model.Pg = pyo.Var(range(Ng), bounds=(0,None))

" Se tivessemos mais uma dimensao (tempo) alem de Ng - numero de geradores"
" Primeira dimensao com tamanho 3 (0, 1, 2) e a segunda tem tamanho Ng (0, 1, 2, 3, 4)"
#model.Pg = pyo.Var(range(3),range(Ng), bounds=(0,None))

" Acessando esta variavel "
" tempo 0 do gerador 2 "
#model.Pg[0][2]

Pg = model.Pg

#restricoes

" Somatoria de geracao (sum([Pg[g] for g in dados_ger.id]) = somatoria de carga (sum(dados_carga.valor)) "
" Somatorio de geracao ([Pg[0] + Pg[1] + Pg[2] + Pg[3] + Pg[4]])"
model.balanco = pyo.Constraint(expr = sum([Pg[g] for g in dados_ger.id])==sum(dados_carga.valor) )

" Sempre converter para float para evitar a geracao de erros "
#model.cond = pyo.Constraint(expr = float(dados_carga.valor[0]) <= Pg[0]+Pg[3])


model.limites = pyo.ConstraintList()
for g in dados_ger.id:
    " Para todo ig "
    model.limites.add(expr = Pg[g]<=float(dados_ger.maximo[g]))

" Esta restricao e para cada carga que tem dependencia (dados_dep)"
model.cond = pyo.ConstraintList()

" Criamos uma restricao generica "
" Criamos um For para percorrer somente as cargas unicas (carga zero) c = 0"
for c in dados_dep.carga.unique():
    model.cond.add(expr = float(dados_carga.valor[c]) <= sum([Pg[g] for g in dados_dep.gerador[dados_dep.carga==c]]))

#obj
model.obj = pyo.Objective(expr = sum([Pg[g]*float(dados_ger.custo[g]) for g in dados_ger.id]))

opt = SolverFactory('glpk')
opt.solve(model)

model.pprint()

dados_ger['geracao'] = [pyo.value(Pg[g]) for g in dados_ger.id]
print(dados_ger)