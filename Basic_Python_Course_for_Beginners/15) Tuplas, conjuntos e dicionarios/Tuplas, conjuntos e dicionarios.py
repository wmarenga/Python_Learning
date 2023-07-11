'''
Tuplas, conjuntos e dicionários:

Tipo                        Descrição                                                          Sintaxe

tuple           tupla: uma sequência de dados que é imutável                    vogais = ('a','e','i','o','u')
set             conjunto: elementos não possuem ordem e não se repetem          alg_decimais = {0,1,2,3,4,5,6,7,8,9}
dict            dicionário: são indexaxos por uma chave keys                    alg_romanos = {'I':1,"II":2,'III':3,'IV':4,'V':5,'X':10}

vogais = ('a', 'e', 'i', 'o', 'u')

As tuplas tambem sao indexaveis 
print(vogais[0])

Podemos ver o numero de elementos
print(len(vogais))

Alterando elementos de uma lista 
vogais = ['a', 'e', 'i', 'o', 'u']
vogais[0] = 5
print(vogais)

Adicionando elementos no final da lista
vogais.append('x')
print(vogais)

Criamos a Tupla verificar o comportamento
vogais = ('a', 'e', 'i', 'o', 'u')

## Apresenta um erro, pois nao podemos alterar uma Tupla
vogais[0] = 5
vogais.append('x')

SET: conjunto: elementos não possuem ordem e não se repetem
inteiros = {0,1,2,3,4,5,6,7,8,9,11}
print(len(inteiros))

Ao contrario das listas e Tuplas, o set nao e indexado 
## Apresenta um erro
inteiros[0]

inteiros = {0,1,2,3,4,5,6,7,8,9,11, 1, 2, 3}
print(inteiros)
saida: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
Os elementos nao repetirao

len(inteiros)

Dicionarios: são indexaxos por uma chave keys 
dicionario_1 = {'A':1, 'B':2, 'C':3}
print(dicionario_1)

Acessando elementos de um dicionario pela sua chave (index)
print(dicionario_1['B'])

enumerate de uma lista gera uma Tupla
vogais = ['a','e','i','o','u']
for i in enumerate(vogais):
print(i)
'''
