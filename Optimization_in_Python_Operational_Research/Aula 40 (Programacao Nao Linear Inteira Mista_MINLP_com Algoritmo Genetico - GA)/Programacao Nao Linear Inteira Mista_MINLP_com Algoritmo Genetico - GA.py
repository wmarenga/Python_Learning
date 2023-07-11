""" 
Algoritmo Genetico (GA):

pip install geneticalgorithm

Documentacao:
https://pypi.org/project/geneticalgorithm/

"""
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

" Criando a funcao (f) com variavel (x) "
" Para inserir as restricoes, precisamos criar uma penalidade (pen) "
def f(x):
    pen = 0
    if not -x[0]+2*x[1]*x[0]<=8: pen = np.inf
    if not 2*x[0]+x[1]<=14: pen = np.inf
    if not 2*x[0]-x[1]<=10: pen = np.inf
    return -(x[0]+x[1]*x[0]) + pen

" Definindo o limite das variaveis "
varbounds = np.array([[0,10],[0,10]])

" Definindo os tipos de variaveis "
vartype = np.array([['int'],['real']])

" Afim de termos maior controle sobre os dados gerados, definimos alguns parametros "
algorithm_param = {'max_num_iteration': 100,\
                   'population_size':100,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

" Criando o modelo e defimimdo a dimensao do problema quando as variaveis sao utilizadas "
" Ao criar o modelo, definimos que ele ira utilizar os parametros que definmos acima "
model = ga(function=f,dimension=2,variable_type_mixed=vartype,variable_boundaries=varbounds,algorithm_parameters=algorithm_param)

" Para rodar o algoritmo "
model.run()