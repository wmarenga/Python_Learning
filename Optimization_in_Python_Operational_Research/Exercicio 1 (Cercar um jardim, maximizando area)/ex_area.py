import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,None))
model.y = pyo.Var(bounds=(0,None))
x = model.x
y = model.y

model.obj = pyo.Objective(expr= x*y, sense=maximize)
model.c1 = pyo.Constraint(expr= 2*x+y <= 100)

opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')
opt.solve(model)

print('x:', np.round(pyo.value(x),2))
print('y:', np.round(pyo.value(y),2))
print('A:', np.round(pyo.value(x)*pyo.value(y),2))