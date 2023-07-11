""" 
O Or-Tools e um FrameWork e por este motivo requer o solver instalado para resolver problemas.

1) Garanta que o Gurobi e Scip estao instalados;
2) pip install wheel;
3) Instale o Git: https://git-scm.com
** O git sera usado para baixar os arquivos fonte do Or-Tools.

4) Instale o Cmake: https://www.cmake.org
** O CMAKE sera utilizado para realizar a compilacao do Or-Tools.

5) Instale o Microsoft Visual Studio 2019 (pacote de desenvolvimento C++), versao comunidade;
** Sera atraves do Visual Studio que iremos compilar o Or-Tools. 

6) Abra o X64 Native Tools Command Prompt (abrir como administrador);
7) cd c:\
8) git clone https://github.com/google/or-tools
9) cd or-tools
10) tools\make third_party
10) edit Makefile.local
    - Abrir Windows Explorer (C:\or-tools\Makefile.local);
    - Clicar com botao direito no arquivo (Makefile.local) <abrir como>/ bloco de notas;
    - Inserir as auteracoes abaixo:
    
(Omitir) #JAVA_HOME = # JAVA_HOME is not set on your system. Set it to the path to jdk to build the java files.
(Inserir) WINDOWS_PATH_TO_PYTHON = C:\Users\Wellington\AppData\Local\Programs\Python\Python310
(Inserir) WINDOWS_GUROBI_DIR = C:\gurobi951
(Inserir) GUROBI_LIB_VERSION = 95
(Inserir) WINDOWS_SCIP_DIR = C:\SCIPOptSuite8

11) tools\make python
12) tools\make install_python

Documentacao:
https://developers.google.com/optimization/install/python/source_windows
"""
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