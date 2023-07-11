""" 
Gurobi:
https://www.gurobi.com
- Fazer download do instalador (Windows);
- Ativar Gurobi;
    - Pegar o codigo de ativacao no site;
    - Copiar e colar no prompt de comando;
    - Copiar o nome da variavel (GRB_LICENCE_FILE);
    - Abrir Windows Explorer/ botao direito em (este computador)/ Propriedades
    - Configuracoes avancadas do sistema/ variaveis de ambiente
    - Nova variavel de sistema/ Nome da variavel: GRB_LICENSE_FILE;
    - Valor da variavel: C:\gurobi951\gurobi.lic. <OK> <OK> <OK>
    - Reboot
    
Instalar a biblioteca gurobipy:

Os passos a seguir sao para a versao 9.0 do Gurobi
Para versao 9.1, use os seguintes passos:
- Dentro do prompt de comando, va ate a pasta de instalacao do Gurobi
ex.: cd c:\gurobi910\win64
- Use o comando: python setup.py install
Pronto!

pip install gurobipy

*** Se houver algum erro no PIP, va ate a pasta de instalacao do Gurobi (c:\gurobiXXX\win64\bin\pysetup.bat), sera solicitada
a pasta de instalacao do Python. Se nao souber a pasta de instalacao do Python, digitar o comando (where python). Copie tudo
exceto o (python.exe). Por fim cole este caminho no prompt de comando e <enter>.

"""

import gurobipy

from gurobipy import *
from gurobipy import Model

model = Model('exemplo')

" obj e o peso da variavel na funcao objetivo, como e x+y, o peso de x=1 "
" vtype='C' - continuo"
x = model.addVar(obj=1, vtype='C', name='x')
y = model.addVar(obj=1, vtype='C', name='y')

" Utilizamos este comando para que as veriaveis sejam gravadas como variaveis de otimizacao. "
model.update()

" Criando as restricoes "
" Estou informando que e uma expressao linear (-x + 2y)"
#L1 = LinExpr([-1, 2], [x,y])
" Definindo a restricao "
#model.addConstr(L1, "<", 8)

" Podemos alterar o L pela funcao (-x+2*y)"
model.addConstr(-x+2*y <= 8)

#L2 = LinExpr([2, 1], [x,y])
" Definindo a restricao "
#model.addConstr(L2, "<", 14)
model.addConstr(2*x+y <= 14)

#L3 = LinExpr([2, -1], [x,y])
" Definindo a restricao "
#model.addConstr(L3, "<", 10)
model.addConstr(2*x-y <= 10)

" Definindo a funcao objetivo "
model.ModelSense = -1

" Definindo o otimizador "
model.optimize()

print('x= ', x.X)
print('y= ', y.X)
