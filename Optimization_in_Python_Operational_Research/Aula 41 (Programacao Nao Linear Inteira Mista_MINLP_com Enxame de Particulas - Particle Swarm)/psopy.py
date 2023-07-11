import numpy as np
from pyswarm import pso

def model_obj(x):
    pen = 0
    x[0] = np.round(x[0],0)
    if not -x[0]+2*x[1]*x[0]<=8: pen = np.inf
    if not 2*x[0]+x[1]<=14: pen = np.inf
    if not 2*x[0]-x[1]<=10: pen = np.inf
    return -(x[0]+x[1]*x[0]) + pen

def cons(x):
    return []

lb = [0,0]
ub = [10,10]
x0 = [0,0]

xopt, fopt = pso(model_obj,lb,ub,x0,cons)

print('x =', xopt[0])
print('y =', xopt[1])