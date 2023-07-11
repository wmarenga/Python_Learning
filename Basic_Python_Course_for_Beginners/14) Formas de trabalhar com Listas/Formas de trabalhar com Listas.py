'''
Formas de trabalhar com listas:

    Função                          Descrição
range(inteiro)              retorna um iterável do tipo range
lambda x: função_x          Retorna uma função
map(função,lista)           Retorna um iterável do tipo map
list(iterável)              Cria uma lista a partir de um iterável

Atenção, este não é um tutorial sobre programação funcional! Quem se interessar pode pesquisar por:
Functional Programming ou Programação Funcional.

x = []

for i in range(10):
    x.append(i)
print(x)

Usando o range para criar uma lista. 
y = list(range(10))
print(y)

Funcao Lambda (forma rapida de se criar funcoes em Python):
f = lambda x : x**2
print(f(5))

lista = [1, 2, 3, 4]
f = lambda x : x**2
print(map(f, lista))
print(type(map(f, lista)))

Retorna uma lista com os quadrados
lista = [1, 2, 3, 4]
f = lambda x : x**2
print(list(map(f, lista)))

Fazendo iteracoes dentro das listas
quadrado = [x**2 for x in range(1, 5)]
print(quadrados)
saida: [1, 4, 9, 16]

'''

