""" 
Tarefa: Exercício MILP

Resolva o exercício apresentado no vídeo

Exercicio Proposto:

Imprima o resultado obtido e o tempo de processamento para a resolucao do seguinte
problema de otimizacao, usando o pyomo. 

min somatoria (i= 1 a 5) xi + y
somatoria (i=1 a 5) xi + y <= 20
xi + y >= 15, para todo i 
somatoria (i=1 a 5)i * xi >= 10
x5 + 2y >= 30
xi, y >= 0
xi inteiro, para todo i

Qual o resultado do problema apresentado?

x[1] = 0

x[2] = 0

x[3] = 0

x[4] = 0

x[5] = 2

y = 15

O tempo de processamento depende de cada computador

"""
" Importando desta maneira iremos garantir que funcoes como seno e cosseno funcionem dentro do Python (nao nativas da linguagem ) "
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import time, numpy as np

model = pyo.ConcreteModel()

" Temos que acrescentar +1, pois se deixarmos 5 estaremmos considerando o intervalo de 1 ate 4 "
model.x = pyo.Var(range(1,6), bounds=(0,np.Inf), within=Integers)
model.y = pyo.Var(bounds=(0,np.Inf))

" Atribuindo (model.x/ model.y) a variaveis mais curtas (x/ y) "
x = model.x
y = model.y

" Nesta expressao o i nao esta definido, sendo assim precisamos defini-lo em ([x[i] for i in range(1,6)]) "
model.C1 = pyo.Constraint(expr = sum([x[i] for i in range(1,6)]) + y <= 20)
" Nesta expressao nos definimos o i no FOR "
model.C2 = pyo.ConstraintList()
for i in range(1,6):
    model.C2.add(expr = x[i] + y >= 15)
model.C3 = pyo.Constraint(expr = sum([i * x[i] for i in range(1,6)]) >= 10)
model.C4 = pyo.Constraint(expr = x[5] + 2*y >= 30)

" Conferindo se o modelo esta correto "
model.pprint()

" Definindo a funcao objetivo "
" O padrao ja e (minimize), mas podemos definir mesmo assim "
model.obj = pyo.Objective(expr= sum([x[i] for i in range(1,6)]) + y, sense = pyo.minimize)

" Medindo o tempo de processamento com a biblioteca (time), medimos apenas a execucao do modelo e nao a contrucao do mesmo "
t_inicial = time.time()

" Definindo qual e o Solver responsavel por solucionar o problema "
opt = SolverFactory('glpk')

" Solicito que o Solver resolva o problema "
opt.solve(model)
Deltat = time.time() - t_inicial

" Ver todo o modelo impresso na tela com todas as restricoes, variaveis e limites "
model.pprint()

" Capturando a solucao "
" Definimos que o Deltat tera apenas 2 casa decimais "
print('tempo = ', np.round(Deltat, 2))

for item in range(1,6):
    print('x[%i] = %i' % (i, pyo.value(x[i])))
print('y = %.2f' % pyo.value(y))

" Imprimindo a funcao objetivo "
print('obj', pyo.value(model.obj))