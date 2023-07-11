#import pyscipopt
from pyscipopt import Model
# import pyscipopt.Model as Model (mesma coisa)

model = Model('exemplo')

" Definindo as variaveis "
x = model.addVar('x')
y = model.addVar('y')
" Acrescentado a variaver (z) para Nao linear "
z = model.addVar('z')

" Definindo a funcao objetivo "
" Linear "
#model.setObjective(x+y, sense= 'maximize')

" Nao Linear (Ira apresentar um erro), para resolver este erro, vamos inserir os comandos abaixo "
#model.setObjective(x+y*x, sense= 'maximize')

" Para corrigir o erro, substituimos a funcao pela variavel (z)"
model.setObjective(z, sense= 'maximize')

" Definindo as restricoes "
" Linear "
#model.addCons(-x+2*y<=8)

" Adicionamos este comando para de (setObjective) acima "
model.addCons(z==x+y*x)
" Nova restricao, mudando de linear para nao linear "
model.addCons(-x+2*y*x<=8)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

" Chamando a solucao do problema  "
model.optimize()

" Salvando a melhor solucao dentro da variavel (sol) "
sol = model.getBestSol()

" Exibindo os resultados para X e Y "
print('x= ', sol[x])
print('y= ', sol[y])