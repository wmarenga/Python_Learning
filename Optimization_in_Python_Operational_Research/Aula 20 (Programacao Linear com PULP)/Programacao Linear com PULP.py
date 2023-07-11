""" 
O PULP trabaha apenas com problemas lineares. 

Instalacao:

pip install cython
pip install pulp

Mais informacoes:
https://github.com/coin-or/pulp

"""
import pulp as pl

" Criando o modelo do problema "
model = pl.LpProblem('Ex', pl.LpMaximize)

" Definindo as variaveis com limite inferior 0 e superior 10 "
x = pl.LpVariable('x',0,10)
y = pl.LpVariable('y',0,10)

" Criando as restricoes "
" Estamos adicionando as restricoes ao modelo (model)"
model += -x+2*y<=8
model += 2*x+y<=14
model += 2*x-y<=10

" Definindo a funcao objetivo "
model += x+y

" Chamando o Solver para resolver o problema "
" Deixando em branco o parametro de solve(), como padrao o PULP define como o Solve (CBC) = Or-Tools "
status = model.solve()

" Capturando os resultados otimos obtidos "
x_value = pl.value(x)
y_value = pl.value(y)

print('x=',x_value)
print('y=',y_value)