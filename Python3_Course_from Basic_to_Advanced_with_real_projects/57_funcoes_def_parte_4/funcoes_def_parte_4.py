"""
Escopo de variáveis (Locais vs Globais):

# Escopo Global:
variavel = 'valor'
print(variavel)


def func():
    print(variavel)


def func2():
    global variavel  # Estamos determinando que esta variável será global
    variavel = 'Outro valor'
    print(variavel)


func()
func2()

print(variavel)  # Esta variável irá exibir 'valor', pois está mostrando
# a variavel global.

variavel = 'valor2'


def func1():
    outra_variavel = 'valor func1()'
    # print(variavel)  # UnboundLocalError
    # variavel = 1234  # variável local
    # print(variavel)


def func2():
    print(outra_variavel)  # Não conseguimos acessar,
    # pois é uma variável local de outra função.


func1()
func2()  # NameError
"""
# Para resolver este problema


def func1():
    outra_variavel = 'Wellington'
    return outra_variavel


def func2(arg):
    print(arg)


var = func1()
func2(var)
