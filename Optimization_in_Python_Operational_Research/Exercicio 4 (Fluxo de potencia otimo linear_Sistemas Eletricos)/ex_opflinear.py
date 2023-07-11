import pyomo.environ as pyo, numpy as np, pandas as pd
from pyomo.environ import *
from pyomo.opt import SolverFactory

#input
caminho_arquivo = 'D:\\23) Programação\\Cursos\\Python\\6) Otimizacao em Python_Pesquisa Operacional\\Exercicio 4 (Fluxo de potencia otimo linear_Sistemas Eletricos)\\sist_eletrico.xlsx'
barras = pd.read_excel(caminho_arquivo, sheet_name='barras')
geracao = pd.read_excel(caminho_arquivo, sheet_name='geracao')
carga = pd.read_excel(caminho_arquivo, sheet_name='carga')
linha = pd.read_excel(caminho_arquivo, sheet_name='linha')

" Numero de barras, geracoes, cargas e linhas"
Nb = len(barras)
Ng = len(geracao)
Nd = len(carga)
Nl = len(linha)

#modelo
model = pyo.ConcreteModel()
" Criacao das variaveis "
" Criamos range() pois as variaveis sao vetores "
model.Pg = pyo.Var(range(Ng))
model.Pl = pyo.Var(range(Nl))
model.teta = pyo.Var(range(Nb), bounds=(-np.pi,np.pi))
Pg = model.Pg
Pl = model.Pl
teta = model.teta

#objetivo
""" Pg e uma variavel de otimizacao, sendo assim eu busco ela diretamente. O custo nao e uma 
variavel de otimizacao, sendo assim eu busco ela em geracao.custo[g]"""
model.obj = pyo.Objective(expr= sum([Pg[g]*geracao.custo[g] for g in geracao.index]), sense=minimize)

#balanço de potência
model.balanco = pyo.ConstraintList()
for n in barras.index:
    sum_Pg = sum([Pg[g] for g in geracao.index[geracao.barra==n]])
    sum_Pls = sum([Pl[l] for l in linha.index[linha.barra_de==n]])
    sum_Plr = sum([Pl[l] for l in linha.index[linha.barra_para==n]])
    sum_Pd = sum([carga.carga[d] for d in carga.index[carga.barra==n]])
    model.balanco.add(expr= sum_Pg - sum_Pls + sum_Plr == sum_Pd)

#fluxo de potência
model.fluxo = pyo.ConstraintList()
for l in linha.index:
    Bl = linha.Bl[l]
    n_send = linha.barra_de[l]
    n_rec = linha.barra_para[l]
    delta_teta = teta[n_send]-teta[n_rec]
    model.fluxo.add(expr= Pl[l] == Bl*delta_teta)

#limites gerador
model.limger = pyo.ConstraintList()
for g in geracao.index:
    model.limger.add(inequality(0,Pg[g],geracao.pgmax[g]))

#limites fluxo de potência
model.limflux = pyo.ConstraintList()
for l in linha.index:
    model.limflux.add(inequality(-linha.plmax[l],Pl[l],linha.plmax[l]))

#referência
model.ref = pyo.Constraint(expr= teta[0] == 0)

#solve
opt = SolverFactory('gurobi')
opt.solve(model)

#result
model.pprint()