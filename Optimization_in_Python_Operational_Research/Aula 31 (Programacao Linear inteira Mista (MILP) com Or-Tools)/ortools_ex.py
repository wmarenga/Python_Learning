import ortools.linear_solver.pywraplp as otlp

solver = otlp.Solver('teste',otlp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

x = solver.IntVar(0,10,'x')
y = solver.NumVar(0,10,'y')

solver.Add(-x+2*y<=7)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

solver.Maximize(x+y)

results = solver.Solve()

if results==otlp.Solver.OPTIMAL:
    print('Resultado Encontrado')
else:
    print('Resultado NÃO Encontrado')
    
print('x=',x.solution_value())
print('y=',y.solution_value())