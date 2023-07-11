""" 
Pyomo:

1) pip install pyomo;
2) Instale um solver (Gurobi, SCIP ou GLPK);

GLPK para Windows
https://sourceforge.net/projects/winglpk

Add GLPK e GLPK/win64 na variavel de ambiente.
1) Baixe o arquivo no site/ descompacte/ copie a pasta descompactada em c:/
2) Clique com o botao direito em (este computador)/ Propriedades do sistema/ / variaveis de ambiente
3) Em variaveis de sistema clique duas vezes em "Path"
4) Localize a pasta (C:\glpk-4.65\w64) e copie na ultima posicao vazia de path. <OK> <OK> <OK>

Documentacao:
https://pyomo.readthedocs.io

"""
" Importando desta maneira iremos garantir que funcoes como seno e cosseno funcionem dentro do Python (nao nativas da linguagem ) "
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))

" Atribuindo (model.x/ model.y) a variaveis mais curtas (x/ y) "
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr = -x + 2*y <= 8)
model.C2 = pyo.Constraint(expr = 2*x + y <= 14)
model.C3 = pyo.Constraint(expr = 2*x - y <= 10)

" Definindo a funcao objetivo "
model.obj = pyo.Objective(expr= x + y, sense = pyo.maximize)

" Definindo qual e o Solver responsavel por solucionar o problema "
opt = SolverFactory('glpk')

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