""" 
A Programacao Linear Inteira mista retorna valores (coordenadas) nao inteiros (4.2, 5.6). 

max x + y
-x + 2y <= 7
2x + y <= 14
2x - y <- 10
0 <= x <= 10
0 <= y <= 10
x com valores inteiros

Sendo x assumindo somente valores inteiros, estaremos considerando somente alguns intervalos da area de solucao. 

Para definir x como inteiro no Pyomo, devemos digitar o comando abaixo:
model.x = pyo.Var(within=Integers)

Afim de saber mais sobre outras classes de variaveis, acesse o link abaixo:
https://pyomo.readthedocs.io/en/stable/pyomo_modeling_components/Sets.html#predefined-virtual-sets

Verificamos que apos definir (within=Integers) para x, o mesmo passa a pertencer ao dominio dos numeros inteiros e y 
continua pertencendo aos numeros reais. 

    x : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   4.0 :    10 : False : False : Integers
    y : Size=1, Index=None
        Key  : Lower : Value : Upper : Fixed : Stale : Domain
        None :     0 :   5.5 :    10 : False : False :  Reals
        
"""
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

" Considerando apenas os valores inteiros de x "
model.x = pyo.Var(within=Integers, bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))

x = model.x
y = model.y

model.C1 = pyo.Constraint(expr= -x+2*y<=7)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

model.obj = pyo.Objective(expr= x+y, sense=maximize)

opt = SolverFactory('gurobi')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)