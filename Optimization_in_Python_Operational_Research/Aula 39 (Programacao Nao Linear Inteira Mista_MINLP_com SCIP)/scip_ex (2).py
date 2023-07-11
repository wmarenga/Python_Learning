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