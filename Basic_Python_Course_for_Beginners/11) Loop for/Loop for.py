'''
Loop for:

- for variável in o_que_será_iterado:

Há uma série de tipos que podem ser utilizado como iteradores, como:

- range --> seus elementos são inteiros
- list --> seus elementos são os que estão contidos na lista
- enumerate --> seus elementos são tuplas que contem inteiros e valores

Criando um range:

range(10)
saida: range(0, 10)

print(type(range(10))

for i in range(10):
    print(i)

for i in range(10):
    print(i**2)

for i in range(1, 10):
    print(i**2)

Listando os elementos de uma lista
lista_vogais = ['a', 'e', 'i', 'o', 'u']

for i in lista_vogais:
    print(i)

lista_vogais = 'aeiou'

Tambem podemos fazeer o mesmo procedimento para strings
for i in lista_vogais:
    print(i)

Usando operacoes matematicas
lista_vogais = ['a', 'e', 'i', 'o', 'u']

for i in lista_vogais:
    print(i*10)

Usando o comprimento da lista
lista_vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(len(lista_vogais)):
    print(i)

Usando comando enumerate cria uma Tupla
lista_vogais = ['a', 'e', 'i', 'o', 'u']

for i in enumerate(lista_vogais):
    print(i)

O primeiro elemento e o indice e o segundo e o elemento da lista
saida:
(0, 'a')
(1, 'e')
(2, 'i')
(3, 'o')
(4, 'u')

Acessando os indices:
for i in enumerate(lista_vogais):
    print(i[0])
saida:
0
1
2
3
4

Acessando os elementos:
for i in enumerate(lista_vogais):
    print(i[1])
saida:
a
e
i
o
u

'''
    
