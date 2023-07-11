# Exercício 24 - Máximo com 3 parâmetros:
# Reescreva a função 'maximo' do outro exercício, que devolve
# o maior valor dentre dois inteiros recebidos, para que ela
# passe a receber 3 valores inteiros como parâmetros e devolva
# o maior dentre eles.
# Exemplos de execução no Python Shell
# >>>maximo(30, 14, 10)
# 30
# >>>maximo(0, -1, 1)
# 1

def maximo(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z


maximo(2, 4, 6)
