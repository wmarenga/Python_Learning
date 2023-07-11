# Dicionarios em Python (Sintaxe basica de um dicionario)
dicionario = {'chave': 'valor'}

print(dicionario)
print(type(dicionario))

# Adicionando elementos novos a um dicionario
dicionario1 = {'Nome1': 'Paulo'}
print(dicionario1)

# Adicionando o valor 'Veronica' na chave 'Nome2' ao dicionario1
dicionario1['Nome2'] = 'Veronica'
print(dicionario1)

# Alterando o valor de uma chave de um dicionario
dicionario1 = {'Nome1': 'Ana', 'Nome2': 'Carla', 'Nome3': 'Maria'}
print(dicionario1)

# Alterando o valor da chave "Nome2"
dicionario1['Nome2'] = 'Barbara'
print(dicionario1)

# Acrescentando chave e valor a um dicionario existente
dicionario2 = dicionario1 | {'Nome4': 'Wellington'}
print(dicionario2)

# Acessando um elemento do dicionario (sempre pela chave)
dicionario1 = {'Nome': 'Fernando', 'idade': 32,
               'sexo': 'Masculino', 'Nacionalidade': 'Brasileira'}
print(dicionario1['Nome'])
print(dicionario1['Nacionalidade'])

# Usando o construtor de dicionarios do Python (dict)
dicionario2 = dict(chave1='valor da chave1', chave2='valor de chave2')
print(dicionario2)
print(type(dicionario2))

# Consultando as chaves de um dicionario
dicionario2 = dict(chave1='valor da chave1', chave2='valor de chave2')
print(dicionario2.keys())

# Consultando os valores de um dicionario
dicionario2 = dict(chave1='valor da chave1', chave2='valor de chave2')
print(dicionario2.values())

# Pesquisando a chave e obtendo valor
d3 = {'1': 'Ana', '2': 'Maria', '3': 'Paulo', '4': 'Marcos'}
print(d3.get('4'))
print(d3.get('2'))

# Pesquisando no dicionario via operador logico
d3 = {'1': 'Ana', '2': 'Maria', '3': 'Paulo', '4': 'Marcos'}
print('3' in d3)

# Expressoes logicas em dicionarios
# Verificando se uma chave ou valor constam em um dicionario (pesquisa pela chave e obtendo valor)
d3 = {'1': 'Ana', '2': 'Maria', '3': 'Paulo', '4': 'Marcos'}
print('3' in d3)
# Pela chave
print('2' in d3.keys())
# Pelo valor
print('Ana' in d3.values())
# Elemento especifico do dicionario
print(d3['2'] == 'Maria')

# Atualizacao de elementos de um dicionario. Informamos a chave e o novo valor a ser alterado
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D'}
print(d4)
d4.update({'2': 'E'})
print(d4)

# Removendo um elemento de um dicionario (sempre pela chave)
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D'}
print(d4)
del d4['4']
print(d4)
# Tambem podemos usar o parametro .pop() para remover elementos de um dicionario
dicionario1 = {'Nome': 'Fernando', 'Idade': 32,
               'Sexo': 'Masculino', 'Nacionalidade': 'Brasileiro'}
dicionario1.pop('Nacionalidade')
print(dicionario1)

# Imprimindo somente chaves ou somente valores de um dicionario
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}
# Mostrando as chaves de um dicionario
print(d4.keys())
print(type(d4.keys()))
# Mostrando os valores de um dicionario
print(d4.values())

# Pesquisando o tamanho de um dicionario
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}
print(len(d4))

# Lendo as chaves de um dicionario por meio de um laco FOR
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}

for chaves in d4.keys():
    print('Chaves: ', chaves)

# Lendo os valores de um dicionario por meio de um laco FOR
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}

for valores in d4.values():
    print('Valores: ', valores)

# Lendo chaves e valores de um dicionario por meio de um laco FOR (chaves e valores)
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}

for itens in d4.items():
    print('Chaves : Valores = ', itens)

# Laco FOR descompactando elementos de um dicionario
d4 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}

lista1 = list()
lista2 = list()
for n, o in d4.items():
    lista1.append(n)
    lista2.append(o)
    print(f'Chaves: {n}, Valores: {o}')
print(lista1)
print(lista2)

# Listas dentro de dicionarios
dicionario = {'almox': ['Folha de Oficio', 'Caneta',
                        'Grampeador'], 'cozinha': ['Cafe', 'Acucar']}

print(dicionario['almox'][0])
print(dicionario['cozinha'][1])

# Dicionario dentro de um dicionario
usuarios = {'Joao': {'Identificador': '0001', 'Cargo': 'Porteiro', 'Salario': '2000'}, 'Maria': {'Identificador': '0003',
                                                                                                 'Cargo': 'Aux. Limpeza', 'Salario': '1900'}, 'Jose': {'Identificador': '0002', 'Cargo': 'Tecnico', 'Salario': '2500'}}

for chaves, valores in usuarios.items():
    print(f'Funcionaios: {chaves}')

    for i, j in valores.items():
        # \t cria um paragrafo (tab)
        print(f'\t{i} = {j}')

# Ordenar um dicionario

meu_dicionario = {'nome': 'Wellington', 'telefone': 999999}
sorted(meu_dicionario)

# Diferentes formas de criar um dicionario

dict([('sap', 4139), ('guido', 4127), ('jack', 4098)])
{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, guido=4127, jack=4098)