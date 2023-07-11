""" 
Programacao Nao Linear com IPOPT Usando Pyomo:

1) Pesquisa por ipopt binaries:
https://www.coin-or.org/download/binary/ipopt
https://github.com/coin-or/Ipopt/releases

2) Descompacte em C:/

3) Pyomo:
opt = SolverFactory('ipopt'), executable='C:\\ipopt\\bin\\ipopt.exe'

O IPOPT e bastante utilizado em exemplos na internet e utiliza o metodo dos pontos interiores. O metodo dos 
pontos interiores sempre retornara um erro que devera estar entre sexta e oitava casa decimal. 

"""
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

" Linear "
#model.C1 = pyo.Constraint(expr= -x+2*y<=8)
" Aterado para nao Linear "
model.C1 = pyo.Constraint(expr= -x+2*y*x<=8)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

" Linear "
#model.obj = pyo.Objective(expr= x+y, sense=maximize)
" Alterado para Nao Linear "
model.obj = pyo.Objective(expr= x+y*x, sense=maximize)

" Nao conseguimos resolver NAO LINEAR com este solver (glpk) "
#opt = SolverFactory('glpk')
" Nao conseguimos resolver NAO LINEAR com este solver (gurobi) "
#opt = SolverFactory('gurobi')
#opt = SolverFactory('cplex')
opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')

opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)

