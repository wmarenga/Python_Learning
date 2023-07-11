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

Para definir x como inteiro no SCIP, devemos digitar o comando abaixo:
x = model.addVar('x', vtype='INTEGER')

"""
" No SCIP ja temos uma solucao integrada, porem nao conseguimos utilizar o Pyomo e GUROBI dentro do SCIP "
" No SCIP nao precisamos definir o solver "
from pyscipopt import Model

model = Model('exemplo')

" Para tornar uma variavel inteira no adicionamos vtype='INTEGER' "
x = model.addVar('x', vtype='INTEGER')
y = model.addVar('y')
z = model.addVar('z')

model.setObjective(z, sense='maximize')

model.addCons(z==x+y*x)
model.addCons(-x+2*y*x<=8)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

model.optimize()

sol = model.getBestSol()

print('x=',sol[x])
print('y=',sol[y])