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

opt = SolverFactory('glpk')
result = opt.solve(model)

print('\nMODELO\n---------------------------------------------------------------------')
model.pprint()

print('\nRESTRIÇÃO\n---------------------------------------------------------------------')
model.C1.pprint()

print('\nVARIÁVEL\n---------------------------------------------------------------------')
model.x.pprint()

print('\nRETORNO SOLVER\n---------------------------------------------------------------------')
print(result)
