""" 
Constraint Programming - CP:

E muito utilizado em problemas com grande analise combinatorial, tais como problemas de agendamento. 
Seu conceito e baseado em identificar solucoes factiveis, sendo mais direcionado as restricoes e as logicas
que elas criam do que a funcao objetivo propriamente dito. Nao e requisito ter uma funcao objetivo para
geram um CP. 
O CP e bastante aplicado em problemas onde temos candidatos para alocacao de recursos como em uma agenda.
Ex. Temos 3 funcionarios A, B e C e precisa-se aloca-los no tempo, sendo assim poderiamos trabalhar com 
vetores com nomes. 

Ortools:
https://developers.google.com/optimization/cp/integer_opt_cp

maximize 2x + 2y + 3z
subject to 

x + 7/2 y + 3/2 z <= 25
3x - 5y + 7z <= 45
5x + 2y - 6z <= 37
x, y, z >= 0
x, y, z integers

"""
from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    "Print intermediate solutions."

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count

" Criacao do modelo "
model = cp_model.CpModel()

" Criacao das variaveis model.NewIntVar(limite inferior, limite superior, 'nome da variavel') "
" Quando estamos trabalhando com CP, e muito importante definir o limite superior (None - nao e bom)"
x = model.NewIntVar(0, 1000, 'x')
y = model.NewIntVar(0, 1000, 'y')
z = model.NewIntVar(0, 1000, 'z')

" Criacao das restricoes "
" Multiplicamos tudo por 2 para retirar a fracao, pois estamos trabalhando com numeros inteiros "
model.Add(2*x+7*y+3*z<=50)
model.Add(3*x-5*y+7*z<=45)
model.Add(5*x+2*y-6*z<=37)
model.Add(x+y+z>=10)

" Funcao objetivo "
#model.Maximize(2*x+2*y+3*z)

solver = cp_model.CpSolver()
status = solver.Solve(model)

print('Status =', solver.StatusName(status))
print('FO =', solver.ObjectiveValue())
print('x =', solver.Value(x))
print('y =', solver.Value(y))
print('z =', solver.Value(z))

" Com os comandos abaixo, nos iremos imprimir todos os resultados de um problema "
" Para que possamos imprimir todos os resultados, temos que retirar a funcao objetivo "
solution_printer = VarArraySolutionPrinter([x, y, z])
status = solver.SearchForAllSolutions(model, solution_printer)