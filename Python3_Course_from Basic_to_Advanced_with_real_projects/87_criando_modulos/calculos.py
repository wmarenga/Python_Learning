import math

PI = math.pi  # Por ser uma constante usamos letra maiúscula.


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


# Se o módulo estive sendo importado, não executar o que está dentro
# do if
lista = [1, 2, 3, 4, 5]
if __name__ == '__main__':
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
# print(__name__)  # tambem se chama __main__
