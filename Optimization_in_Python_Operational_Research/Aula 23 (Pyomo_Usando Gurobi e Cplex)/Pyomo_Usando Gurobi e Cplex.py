""" 
Usando o Gurobi e Cplex no Pyomo:

Gurobi:
- Instale e ative (Veja a aula de LP: Gurobi);
- No Pyomo: opt = SolverFactory('gurobi'). 

CPLEX:
- Acesse: https://ibm.com/br-pt/products/ilog-cplex-optimization-studio
- Login, download e instalar;
- No Pyomo: opt = SolverFactory('cplex')

"""
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr= -x+2*y<=8)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

model.obj = pyo.Objective(expr= x+y, sense=maximize)

#opt = SolverFactory('glpk')
#opt = SolverFactory('gurobi')
opt = SolverFactory('cplex')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)
