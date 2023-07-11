""" 
Cercar um Jardim:

Qual a maior area que podemos cercar de um jardim usando uma cerca de ate 100 metros?
Defina tambem as dimensoes desse jardim. 

Obs.: O jardim ja e cercado por um muro de pedra em uma de suas extremidades. 

"""
" Este problema e nao Linear pois a funcao objetivo e (x*y)"
import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

" O limite inferior e zero e o limite superior nao existe "
model.x = pyo.Var(bounds=(0,None))
model.y = pyo.Var(bounds=(0,None))
x = model.x
y = model.y

" Definindo a funcao objetivo "
model.obj = pyo.Objective(expr= x*y, sense=maximize)
" Criando a restricao "
model.c1 = pyo.Constraint(expr= 2*x+y <= 100)

" Definindo o solver "
opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')
" Resolvendo o problema "
opt.solve(model)
" Imprimindo os resultados "
print('x:', np.round(pyo.value(x),2))
print('y:', np.round(pyo.value(y),2))
print('A:', np.round(pyo.value(x)*pyo.value(y),2))