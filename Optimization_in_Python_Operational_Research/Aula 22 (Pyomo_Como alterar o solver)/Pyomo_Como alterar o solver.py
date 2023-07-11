""" 
Explorando o Pyomo:

Trabalhando com diferentes solvers:

CyLP
CBC:
https://projects.coin-or.org/CBC
https://bintray.com/coin-or/download/Cbc/
https://ampl.com/products/solvers/open-source/#cbc
https://www.coin-or.org/download/binary/Cbc/

Comando para verificar uma lista de todos os SOLVERS suportados pelo PYOMO:
pyomo help --solvers

 
"""
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y



" Restricao nao linear "
#model.C1 = pyo.Constraint(expr= -x+2*y*x<=8)

" Restricao linear "
model.C1 = pyo.Constraint(expr= -x+2*y<=8)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

model.obj = pyo.Objective(expr= x+y, sense=maximize)

" Usamos o IPOPT para solucoes nao lineares "
#opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')

" Usamos o CBC para solucoes lineares "
opt = SolverFactory('cbc', executable='C:\\cbc\\bin\\cbc.exe')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)