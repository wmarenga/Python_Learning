""" 
Particle Swarm (Enxame de particulas): pen = np.inf

pip install pyswarm

Documentacao:
https://pythonhosted.org/pyswarm

"""
import numpy as np
from pyswarm import pso

def model_obj(x):
    pen = 0
    " Definindo como x inteiro, pois o pso nao tem esta funcao nativamente "
    x[0] = np.round(x[0],0)
    if not -x[0]+2*x[1]*x[0]<=8: pen = np.inf
    if not 2*x[0]+x[1]<=14: pen = np.inf
    if not 2*x[0]-x[1]<=10: pen = np.inf
    " Minimizacao (-)"
    return -(x[0]+x[1]*x[0]) + pen

" cons e um conjunto de restricoes "
def cons(x):
    return []

" Limites inferiores "
lb = [0,0]
" Limites superiores "
ub = [10,10]
" Chute inicial "
x0 = [0,0]

" Definimos 2 variaveis que vao receber os resultados e a funcao objetivo "
" cons e um conjunto de restricoes "
xopt, fopt = pso(model_obj,lb,ub,x0,cons)

print('x =', xopt[0])
print('y =', xopt[1])