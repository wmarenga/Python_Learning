"""
Listas (list):

Listas em Python funcionam como vetores/ matrizes (Arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dados.

As listas, ao contrário, das tuplas podem ser alteradas.

Linguagem C e Java: Arrays
- Possuem tamanho e tipo de dados fixos:
Ou seja, nestas linguagens se você criar um 'array' do tipo 'int' e com tamanho 5, este 'array'
será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Em Python:
- Dinâmico: Não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando 
elementos:
- Qualquer tipo de dado. Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de 
dado:

As listas em Python são SEMPRE representadas por colchetes: []

As listas sao mutaveis: Ou seja, porem ser alteradas constantemente

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

# lista2 = ['G', 'e', 'e', 'k', '  ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista5 = list('Geek University')

lista3 = []
lista5 = list('Geek University')
print(lista5)

# Para números:

lista4 = list(range(11))

# Podemos facilmente checar se determinado valor está contido na lista.

num = 7
if num in lista4.index(num):
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Para String:

lista5 = list('Geek University')
if 'e' in lista5:
    print("Encontrei a letra 'e'")
else:
    print('Não encontrei a letra e')

# Podemos facilmente ordenar uma lista:

# Números:

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(lista1)
lista1.sort()
print(lista1)

# Strings
lista5 = list('Geek University')
print(dir(lista5))
print(lista5)
# Ordem: espaços em branco, caractéres e números, letras maiúsculas e por fim letras minúsculas.
lista5.sort()
print(lista5)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista.

print(lista5.count('e'))

# Adicionando elementos em uma lista
# Para adicionar elementos em uma lista utilizamos a funcao append()

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(lista1)
# Adiciona ao final da lista
lista1.append(55)
print(lista1)

Obs.: Com o parâmetro 'Append', somente conseguiremos adicionar um elemento por vez no append.

# Adicionando uma lista dentro da lista:

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista1.append([0, 6, 8])

# O Python só encontra se forem os exatos números na lista interna.
if [0, 6, 8] in lista1:
    print('Encontrei na lista')
else:
    print('Não encontrei a lista')

# Adicionamos mais de 1 elemento dentro de uma lista
lista1.extend([21, 24])
print(lista1)

# Adicionando vários elementos em uma lista (extend), os elementos adicionado serão incluídos 
no final da lista:

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista1.extend([21, 24]) # Usando o extend, podemos adicionar vários elementos em uma lista.

print(lista1)

if 21 in lista1:
    print('Encontrei na lista')
else:
    print('Não encontrei a lista')

# Podemos inserir um novo elemento na lista informando a posição do índice.
# NÃO SUBSTITUIMOS O VALOR OUTRORA NA POSIÇÃO 2. O mesmo sera deslocado para a direita da lista.

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista1.insert(2, 'Novo Valor') # Adiciona um valor no índice posição 2.
print(lista1)
[1, 99, 'Novo Valor', 4, 27, 15, 22, 3, 1, 44, 42, 27]

# União de 2 listas:
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', '  ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

# Mesma coisa do extend()
lista6 = lista1 + lista2

print(lista6)

lista1.extend(lista2)  # adiciona a lista2

print(lista1)

# Invertendo a ordem de uma lista (reverse):

Opção 1:
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista1.reverse()
print(lista1)

lista2 = ['G', 'e', 'e', 'k', '  ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista2.reverse()
print(lista2)

Opção 2 (Mesma coisa do reverse):
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(lista1[::-1])

lista2 = ['G', 'e', 'e', 'k', '  ', 'U', 'n','i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista2[::-1])

# Copiar uma lista
lista2 = ['G', 'e', 'e', 'k', '  ', 'U', 'n','i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elements existem dentro de uma lista
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista.
# O 'pop' não somente remove o último elemento mas também o retorna.

lista5 = list('Geek University')
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice. Será excluído 1 elemento/ índice da lista.
Obs.: Os elementos à direita deste índice serão Realocados para a esquerda.
Obs.: Se nao houver elemento no indice infromado, teremos o erro IndexError.
lista5 = list('Geek University')
print(lista5)

lista5.pop(2) # Revove o elemento na posição 2 (índice).
print(lista5)

# Removendo elementos especificos de uma lista (minha solucao):
lista5 = list('Geek University')

for i, v in enumerate(lista5):
    while v == 'r':
        lista5.pop(i)
        break
    
print(lista5)

# Podemos remover todos os elementos
lista5 = list('Geek University')
print(lista5)
lista5.clear()
print(lista5)
print(len(lista5))

print(lista5)
# Replicar elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos converter uma 'string' para uma lista

# Exemplo 1 (separando caracteres de uma string e criamdo uma lista com eles):
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()  # Separa os blocos de palavras. Por default o split interpreta 
espaçoes em branco como separadores.
print(curso)

# Obs.: Por padrão, o 'split()' separa os elementos da lista pelo espaço entre elas.

# Exemplo 2:
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',') # Determina que a vírgula será o separador das palavras.
print(curso)

# Convertendo uma lista em 'String'
lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em 
uma 'String'.
curso = ' '.join(lista6)
print(curso)

# Se quisermos adicinar um $ entre os elementos da lista
curso = '$'.join(lista6)
print(curso)

# A lista poderá conter tipos de dados diversos e outras lista também.
lista6 = [1, 2, 2.34, True, 'Geek', 'd', [1, 2, 3], 32423525]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 (Utilizando 'for'):
soma = 0
lista6 = [1, 2, 2.34, 32423525]
for elemento in lista6:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 (Utilizando 'while'):
carrinho = []
produto = ''

while produto != 'sair':
    produto = input("Adicione um produto na lista ou digite 'sair' para sair: ")
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

Meu Exemplo:

carrinho = []
produto = ''

while True:
    if produto != 'sair':
        produto = input("Adicione um produto na lista ou digite 'sair' para sair: ")
        carrinho.append(produto)
    else:
        break
    
carrinho.pop()
for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

!           0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense em um círculo.

!           0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

!    -4        -3        -2      -1         0         1         2       3 (é um ciclo)
# ['verde', 'amarelo', 'azul', 'branco', 'verde', 'amarelo', 'azul', 'branco']
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # ERRO, não existe índice -5

for cor in cores:  # lista as cores na ordem normal
    print(cor)

for cor in cores[::-1]:  # lista as cores na ordem inversa
    print(cor)

indice = 0
while indice < len(cores): # len(cores) é a quantidade total de índices.
    print(cores[indice])
    indice = indice + 1 # incremento

cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar índice em um "for"

for indice, cor in enumerate(cores): # O "enumerate gera pares (indice e cor)".
    print(indice, cor)

# Gerar uma lista com os pares.
cores = list(enumerate(cores))

# Uma lista aceita valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes mas também úteis.
# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Obs.: Caso não tenha este elemento na lista, será apresentado ERRO.
print(numeros.index(12))  # ValueError: 12 is not in list.

# Retorna o índice do primeiro elemento encontrado.
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(5))  # Índex 0

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar.
print(numeros.index(5, 1))  # buscando a partir do índice 1.
print(numeros.index(5, 4))  # buscando a partir do índice 4 (ValueError: 5 is not in list).

# Podemos fazer busca dentro de um range (início e fim):
print(numeros.index(5, 0, 6)) # Encontro o valor 5 no índice 0 (continua mostrando o primeiro índice da lista).

# Revisão de "Slicing"

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista

lista = [1, 2, 3, 4]

# Iniciando no índice 1 e mostrando todos os elementos restantes.
print(lista[1::])
print(lista[-1::])  # Lista com a ordem invertida (de tráz para frente).

# Trabalhando com "slice" de lista com parâmetro 'fim'.

# Inicia no índice 0 e termina no índice 1, pois o índice 2 não está incluído.
print(lista[:2]) # Comeca em 0, pega ate o indice (2-1)
print(lista[1:3])  # Inicia no índice 1 e termina no índice 2.
print(lista[0:-2])

# Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2])  # Começa em 1 e mostra todos os elemento de 2 em 2.
print(lista[::2])  # Começa em 0 e vai ate o final, de 2 em 2.
print(lista[1::-1])  # Começa em 1 e vai ate o final, de 1 em 1 (de traz para frente).

# Invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0] # Inverte a ordem dos índices em uma lista.
print(nomes)

# Forma mais prática (mesma forma de fazer):
nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho.
# (*) Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
print(max(lista))  # Valor Máximo
print(min(lista))  # Valor Mínimo
print(len(lista))  # Tamanho da lista

# Transformar uma lista em "tupla"
# Uma lista é criada por colchetes e uma tupla - parênteses.
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas (deverá ter a quantidade exata de elementos)
# Se tivérmos mais elemento, aparecerá o erro: "ValueError: too many values to 
unpack (expected 3)".

lista = [1, 2, 3, 4]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (shallow copy e Deep Copy)

# Forma 1 (Deep Copy):
lista = [1, 2, 3]
print(lista)

# Em Python chamamos de "Deep Copy".
# As duas listas ficaram totalmente independentes (alteradas sem relacao entre elas)

nova = lista.copy() # Foram copiados os valores da lista "lista" para "nova"
print(nova)
nova.append(4) # Acrescentamos o valor 4 na "nova"
print(lista)
print(nova)

# Forma 2 (Shallow Copy):
# Quando alteramos uma lista, a outra tambem sera alterada (copia por atribuicao)

lista = [1, 2, 3]
print(lista)

nova = lista  # Cópia mantendo as lista associadas
print(nova)
nova.append(4) # Se acrescentármos o valor 4 em "lista" ou "nova", ambas serão alteradas.

print(lista)
print(nova)
"""
