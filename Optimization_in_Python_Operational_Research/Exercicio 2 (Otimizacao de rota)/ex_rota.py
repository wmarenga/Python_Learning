import pandas as pd, numpy as np
from ortools.sat.python import cp_model

#entrada
caminho_arquivo = 'D:\\23) Programação\\Cursos\\Python\\6) Otimizacao em Python_Pesquisa Operacional\\Exercicio 2 (Otimizacao de rota)\\rotas_input.xlsx'
nos = pd.read_excel(caminho_arquivo, sheet_name='nos')
caminhos = pd.read_excel(caminho_arquivo, sheet_name='caminhos')
num_nos = len(nos)
num_caminhos = len(caminhos)

#modelo
model = cp_model.CpModel()
" Criacao de variaveis zeros para os 8 caminhos possiveis e converte para uma lista "
x = np.zeros(num_caminhos).tolist()
for c in caminhos.index:
    x[c] = model.NewIntVar(0,1, 'x[{}]'.format([c]))

#função objetivo
model.Minimize(sum([x[c] * caminhos.distancia[c] for c in caminhos.index]))

#restrições
no_origem = int(nos.no[nos.desc=='origem'])
no_destino = int(nos.no[nos.desc=='destino'])
model.Add(sum([x[c] for c in caminhos.index[caminhos.no_de==no_origem]])==1)
model.Add(sum([x[c] for c in caminhos.index[caminhos.no_para==no_destino]])==1)

for no in nos.no[nos.desc=='meio']:
    " x[c] sao os caminhos "
    sum_entra = sum([x[c] for c in caminhos.index[caminhos.no_para==no]])
    sum_sai = sum([x[c] for c in caminhos.index[caminhos.no_de==no]])
    model.Add(sum_sai <= 1)
    model.Add(sum_entra <= 1)
    model.Add(sum_entra == sum_sai)
    
#resolver
solver = cp_model.CpSolver()
status = solver.Solve(model)

#imprimir
print('Status =', solver.StatusName(status))
print('FO =', np.round(solver.ObjectiveValue()))

caminhos['ativado'] = 0
for c in caminhos.index:
    caminhos.ativado[c] = solver.Value(x[c])
print(caminhos)

print('Rota escolhida')
for c in caminhos.index[caminhos.ativado==1]:
    " O primeiro %1 = caminhos.no_de[c] e o segundo caminhos.no_para[c]"
    print('X%i%i - %.2f' % (caminhos.no_de[c], caminhos.no_para[c], caminhos.distancia[c]))