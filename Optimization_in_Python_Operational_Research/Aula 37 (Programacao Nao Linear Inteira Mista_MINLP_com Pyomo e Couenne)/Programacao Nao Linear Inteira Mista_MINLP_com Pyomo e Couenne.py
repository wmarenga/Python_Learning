""" 
Pyomo: Couenne:

Documentacao:
https://projects.coin-or.org/Couenne

https://www.coin-or.org/download/binary/Couenne/

1) Baixar e descompactar em C:\

2) opt = SolverFactory('couenne', executable='C:\\couenne\\bin\\couenne.exe')

"""
" Importando desta maneira iremos garantir que funcoes como seno e cosseno funcionem dentro do Python (nao nativas da linguagem ) "
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

#model.x = pyo.Var(bounds=(0,10))
" Definindo a variavel x como inteira "
model.x = pyo.Var(within=Integers, bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))

" Atribuindo (model.x/ model.y) a variaveis mais curtas (x/ y) "
x = model.x
y = model.y

" Linear "
#model.C1 = pyo.Constraint(expr = -x + 2*y <= 8)
" Nao Linear "
model.C1 = pyo.Constraint(expr = -x + 2*y*x <= 8)
model.C2 = pyo.Constraint(expr = 2*x + y <= 14)
model.C3 = pyo.Constraint(expr = 2*x - y <= 10)

" Definindo a funcao objetivo "
" Linear "
#model.obj = pyo.Objective(expr= x + y, sense = pyo.maximize)
" Nao Linear "
model.obj = pyo.Objective(expr= x + y*x, sense = pyo.maximize)

" Definindo qual e o Solver responsavel por solucionar o problema "
#opt = SolverFactory('glpk')

" Devemos definir o (Coenne) para solucionar este problema de MINLP"
opt = SolverFactory('couenne', executable='C:\\couenne\\bin\\couenne.exe')

" Solicito que o Solver resolva o problema "
opt.solve(model)

" Ver todo o modelo impresso na tela com todas as restricoes, variaveis e limites "
model.pprint()

" Capturando a solucao "
x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n-------------------------------------------------------------------------------------')
print('x= ', x_value)
print('y= ', y_value)