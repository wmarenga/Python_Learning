""" 
SCIP:
https://www.scipopt.org

Fazer o download do programa e a segunda opcao para adicionar no path (Add SCIPOptSuite to the system PATH for all users). 

biblioteca: PYSCIPOPT
Configurar a variavel de ambiente SCIPOPTDIR

c:\> pip install pyscipopt

Documentacao da biblioteca:
https://github.com/SCIP-Interfaces/PySCIPOpt

E intitulado o Solver gratis mais rapido do mercado. Ele trabalha com problemas lineares, nao lineares e ate mesmo inteiros. 
Muito versatil.

" Definindo a variavel de ambiente "

1) Windows Explore/ botao direito sobre (Este computador)/ Propriedades;
2) Configuracoes avancadas do sistema/ variaveis de ambiente;
3) Variaveis do sistema/ novo;
4) Nova Variavel de Sistema/ Nome da variante: SCIPOPTDIR;
5) Valor da variavel: <Procurar no Diretorio>/ Este computador/ C:\SCIPOpt8 <OK> <OK> <OK>
6) Reboot

*** Sempre procurar pelo nome da biblioteca e nunca por (SCIP), pois a implementacao do SCIP dentro do Python e dada pela
biblioteca (pyscipopt).
*** Podemos tambem rodar o SCIP dentro do Or-Tools, porem precisamos de uma configuracao especial (sera explicada nas proximas aulas). 

Com o SCIP e muito facil converte PL (linear) para PNL (nao linear) somente alteramos a(s) restricoes e o proprio SCIP
e responsavel por fazer as conversoes necessarias.

*** Usando o SCIP, nao e possivel alterar o Solver utilizando. Por exemplo, nao conseguimos utilizar o Gurobi no SCIP.
No Or-Tools e muito simples alterar de um Solver para outro, sendo assim e mais aconselhavel trabalhar com solvers onde
podemos alterar de um solver para outro, em vez de trabalhar com um solver especifico somente. 

"""
#import pyscipopt
from pyscipopt import Model
# import pyscipopt.Model as Model (mesma coisa)

model = Model('exemplo')

" Definindo as variaveis "
x = model.addVar('x')
y = model.addVar('y')

" Definindo a funcao objetivo "
model.setObjective(x+y, sense= 'maximize')

" Definindo as restricoes "
model.addCons(-x+2*y<=8)

" Nova restricao, mudando de linear para nao linear "
#model.addCons(-x+2*x*y<=8)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

" Chamando a solucao do problema  "
model.optimize()

" Salvando a melhor solucao dentro da variavel (sol) "
sol = model.getBestSol()

" Exibindo os resultados para X e Y "
print('x= ', sol[x])
print('y= ', sol[y])