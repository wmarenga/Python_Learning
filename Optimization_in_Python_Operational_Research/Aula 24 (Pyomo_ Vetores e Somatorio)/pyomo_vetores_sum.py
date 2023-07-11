import pandas as pd
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

#dados entrada
dados_ger = pd.read_excel('inputs_dados.xlsx', sheet_name='geracao')
dados_carga = pd.read_excel('inputs_dados.xlsx', sheet_name='carga')
dados_dep = pd.read_excel('inputs_dados.xlsx', sheet_name='dependencia')
Ng = len(dados_ger)

model = pyo.ConcreteModel()

model.Pg = pyo.Var(range(Ng), bounds=(0,None))
Pg = model.Pg

#restricoes
model.balanco = pyo.Constraint(expr = sum([Pg[g] for g in dados_ger.id])==sum(dados_carga.valor) )
#model.cond = pyo.Constraint(expr = float(dados_carga.valor[0]) <= Pg[0]+Pg[3])
model.limites = pyo.ConstraintList()
for g in dados_ger.id:
    model.limites.add(expr = Pg[g]<=float(dados_ger.maximo[g]))
model.cond = pyo.ConstraintList()
for c in dados_dep.carga.unique():
    model.cond.add(expr = float(dados_carga.valor[c]) <= sum([Pg[g] for g in dados_dep.gerador[dados_dep.carga==c]]))

#obj
model.obj = pyo.Objective(expr = sum([Pg[g]*float(dados_ger.custo[g]) for g in dados_ger.id]))

opt = SolverFactory('glpk')
opt.solve(model)

model.pprint()

dados_ger['geracao'] = [pyo.value(Pg[g]) for g in dados_ger.id]