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

Para definir x como inteiro no Or-Tools, devemos digitar o comando abaixo:
x = solver.IntVar(0,10,'x')
onde alteramos .NumVar para .IntVar
        
"""
import ortools.linear_solver.pywraplp as otlp

" Tambem temos que definir um solver para variaveis inteiras (CBC) "
solver = otlp.Solver('teste',otlp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)

" Para definir x como inteiro no Or-Tools, devemos apenas alterar .NumVar para .IntVar" 
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