from pyscipopt import Model

model = Model('exemplo')

x = model.addVar('x', vtype='INTEGER')
y = model.addVar('y')

model.setObjective(x+y, sense='maximize')

model.addCons(-x+2*y<=7)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

model.optimize()

sol = model.getBestSol()

print('x=',sol[x])
print('y=',sol[y])