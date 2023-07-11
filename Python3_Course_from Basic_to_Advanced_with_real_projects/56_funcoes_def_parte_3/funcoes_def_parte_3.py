"""
Funções (def) em Python - *args, **kwargs:

kwargs => key world arguments (argumentos nomeados)

# Quando eu defino um parâmetro padrão (nomeado), os próximo tem
# que ser obrigatoriamente nomeados também.


def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome)
    return nome, a6


func(1, 2, 3, 4, 5)
var = func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
print(var[0], var[1])


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5, 6]
# n1, n2, *n = lista  # Desempacotando
# print(n1, n2, n)  # Mostrando n1, n2 e o resto da lista.

# Exemplo com *args (retorna uma tupla):


def func(*args):
    args = list(args)  # Cast dos valores da tupla para lista.
    args[0] = 20
    print(args)
    # print(args[0])  # Mesmo princípio de lista (primeiro elemento).
    # print(args[-1])  # Mesmo princípio de lista (último elemento).
    # print(len(args))


func(1, 2, 3, 4, 5)

lista = [1, 2, 3, 4, 5, 6]
# n1, n2, *n = lista  # Desempacotando
# print(n1, n2, n)  # Mostrando n1, n2 e o resto da lista.
# print(*lista, sep='-')  # Exibe os valores da lista desempacotados.

# Enviando a lista desempacotada


def func2(*args):
    print(args)


# As duas lista serão concatenadas em uma única tupla.
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func2(*lista, *lista2)

"""

# Usando args/ kwargs


def func3(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

    # O melhor é utilizar get() quando não sabemos se o mesmo existe.
    nome = kwargs.get('nome')
    print(nome)

    idade = kwargs.get('idade')  # None, pois não informei idade.
    print(idade)

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')

    idade = kwargs['idade']  # KeyError se a idade não for informada.


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func3(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)
