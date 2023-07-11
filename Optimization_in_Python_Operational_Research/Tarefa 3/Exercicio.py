""" 
 Tarefa: Exercício NLP

Resolva o problema apresentado no vídeo para exercitar seu aprendizado

Exercicio Proposto:

Imprima o resultado obtido e o tempo de processamento para resolucao de seguinte
problema de otimizacao, usando o pyomo. 

max cos(x+1) + cos(x)*cos(y)
-5 <= x <= 5
-5 <= y <= 5 

Aproveite e explore as funcoes 
model.x = pyo.Var(Initialize=N)
opt.options['tol'] = N

Perguntas dessa tarefa

1) Qual a solucao encontrada?

x = -0,5
y = 0

"""
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import time, numpy as np

model = pyo.ConcreteModel()

" Definindo o valor inicial (initialize=0), evita que o modelo recebe minimos locais, nao definidos por nos "
model.x = pyo.Var(initialize=0, bounds=(-5,5))
model.y = pyo.Var(initialize=0, bounds=(-5,5))

" Alterando para -2, os valores encontrados sao alterados, pois existe um maximo local proximo de -2 (para x e y) "
#model.x = pyo.Var(initialize=-2, bounds=(-5,5))
#model.y = pyo.Var(initialize=-2, bounds=(-5,5))

" Atribuindo (model.x/ model.y) a variaveis mais curtas (x/ y) "
x = model.x
y = model.y

" Nao e necessario criar as restricoes pois ja foram determinadas nos (bounds)"
#model.C1 = pyo.Constraint(expr= x+y*x<=8)
#model.C2 = pyo.Constraint(expr= 8*x+3*y>=-24)
#model.C3 = pyo.Constraint(expr= -6*x+8*y<=48)
#model.C4 = pyo.Constraint(expr= 3*x+5*y<=15)

" Conferindo se o modelo esta correto "
#model.pprint()

" Definindo a funcao objetivo "
" O padrao ja e (minimize), mas podemos definir mesmo assim "
model.obj = pyo.Objective(expr= cos(x+1) + cos(x)*cos(y), sense = pyo.maximize)

" Medindo o tempo de processamento com a biblioteca (time), medimos apenas a execucao do modelo e nao a contrucao do mesmo "
t_inicial = time.time()

" Definindo qual e o Solver responsavel por solucionar o problema "
" Utilizamos o solver (ipopt), para metodo de pontos interiores "
opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')

" Determinando a tolerancia "
opt.options['tol']=1e-6

" Solicito que o Solver resolva o problema "
opt.solve(model)
Deltat = time.time() - t_inicial

" Ver todo o modelo impresso na tela com todas as restricoes, variaveis e limites "
model.pprint()

" Capturando a solucao "
" Definimos que o Deltat tera apenas 2 casa decimais "
print('tempo = ', np.round(Deltat, 2))

" Imprimindo a funcao objetivo "
print('obj', pyo.value(model.obj))

" Capturando a solucao "
x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n-------------------------------------------------------------------------------------')
print('x= ', x_value)
print('y= ', y_value)