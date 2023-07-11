" Este problema e nao linear inteiro misto, pois a funcao objetivo e nao linear "
" p e N sao variaveis de otimizacao "
import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

" Criacao do modelo "
model = pyo.ConcreteModel()

" Definicao das variaveis de otimizacao "
model.p = pyo.Var(bounds=(50,200))
" Definindo que N e inteiro "
model.N = pyo.Var(within=Integers, bounds=(0,None))
p = model.p
N = model.N

" Criacao da funcao objetivo nao linear "
model.obj = pyo.Objective(expr= p*N, sense=maximize)
" Expressao de restricao "
model.C1 = pyo.Constraint(expr= N == 1001-5*p)

" Definindo o solver que sera utilizado "
opt = SolverFactory('couenne', executable='C:\\couenne\\bin\\couenne.exe')

opt.solve(model)

print('p:', np.round(pyo.value(p),2))
print('N:', np.round(pyo.value(N),2))
print('receita:', pyo.value(p)*pyo.value(N))
