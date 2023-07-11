""" 
Tarefa: Exercício LP

Resolva o exercício proposto no vídeo para praticar o aprendizado.

Exercicio Proposto:

Imprima o resultado obtido e o tempo de processamento para resolucao do seguinte 
problema de otimizacao, usando o pyomo. 

min -4x - 2y
x + y <= 8
8x + 3y >= -24
-6x + 8y <= 48
3x + 5y <= 15
x <= 3
y >= 0

Observacoes: Use a biblioteca (time) para computar o tempo de processamento. 

Resolva o problema de otimização apresentado e compare com a solução.

x = 3

y = 1,2

tempo de processando depende de cada computador.

"""
import pyomo.environ as pyo
import numpy as np
import time
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

" Variaveis de otimizacao "
" bounds=(limite inferior, limite superior)"
" Usamos o numpy para definir um numero infinito (np.inf)"
model.x = pyo.Var(bounds=(-np.inf,3))
model.y = pyo.Var(bounds=(0,np.inf))

" Atribuindo (model.x/ model.y) a variaveis mais curtas (x/ y) "
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr = x + y <= 8)
model.C2 = pyo.Constraint(expr = 8*x + 3*y >= -24)
model.C3 = pyo.Constraint(expr = -6*x + 8*y <= 48)
model.C4 = pyo.Constraint(expr = 3*x + 5*y <= 15)

" Definindo a funcao objetivo "
model.obj = pyo.Objective(expr= -4*x - 2*y, sense = pyo.minimize)

" Medindo o tempo de processamento com a biblioteca (time), medimos apenas a execucao do modelo e nao a contrucao do mesmo "
tempo_inicial = time.time()

" Definindo qual e o Solver responsavel por solucionar o problema "
opt = SolverFactory('glpk')

" Solicito que o Solver resolva o problema "
opt.solve(model)
tempo = time.time() - tempo_inicial

" Ver todo o modelo impresso na tela com todas as restricoes, variaveis e limites "
model.pprint()

" Capturando as solucoes otimas "
x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n-------------------------------------------------------------------------------------')
print('tempo', tempo)
print('x= ', x_value)
print('y= ', y_value)