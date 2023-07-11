"""
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items())

pessoas = {'nomes': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nomes"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())  # É representado por uma lista com três Tuplas.

for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} => {v}')
# del pessoas['sexo']
# print(pessoas.items())
# Alterar o valor do índice "nomes' para Leandro.
pessoas['nomes'] = 'Leandro'
print(pessoas.items())

pessoas['peso'] = 98.5
print(pessoas.items())

# Criando um dicionário dentro de uma lista:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
# [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]

print(estado1)
print(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do esrado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()
"""
