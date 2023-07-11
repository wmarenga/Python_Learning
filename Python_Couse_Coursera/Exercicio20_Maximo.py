# Exercício 19 - Máximo
# Escreva a função maximo que recebe 2 números inteiros como
# parâmetro e devolve o maior deles.
# Exemplos de execução no shell do Python:
# >>> maximo(3, 4)
# 4
# >>> maximo(0, -1)
# 0

def maximo(x, y):
    if x > y:
        return x
    else:
        return y


maximo(2, 4)
