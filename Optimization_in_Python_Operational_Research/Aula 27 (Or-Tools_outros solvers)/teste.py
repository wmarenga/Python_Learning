import ortools.linear_solver.pywraplp as otlp

solver = otlp.Solver('teste', otlp.Solver.GUROBI_MIXED_INTEGER_PROGRAMMING)

" Definimos as variaveis "
x = solver.NumVar(0, 10, 'x')
y = solver.NumVar(0, 10, 'y')

" Armazenando as restricoes dentro de outra variavel afim de simplificar o codigo "
minha_restricao1 = -x+2*y<=8
minha_restricao2 = 2*x+y<=14
minha_restricao3 = 2*x-y<=10

" Definimos as restricoes "
solver.Add(minha_restricao1)
solver.Add(minha_restricao2)
solver.Add(minha_restricao3)

" Definicao da funcao objetivo "
solver.Maximize(x+y)

" Mostrar o resultado "
results = solver.Solve()

" Verificando se a solucao otima foi encontrada "

if results == otlp.Solver.OPTIMAL:
    print('Resultado Encontrado')
else:
    print('Resultado NAO Encontrado')
print('x= ',int(x.solution_value()))
print('y= ',int(y.solution_value()))