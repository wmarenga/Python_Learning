import math

# def circunferencia(raio: float) -> float: # Nunca ter os 2 (na função e
# no comentário)


def circunferencia(raio):
    # type: (float) -> float # Também pode ser feito assim (Type Hinting)
    return 2 * math.pi * raio


# print(circunferencia(8))

# print(circunferencia('geek'))


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str # Com múltiplos argumentos (texto, alinhamento)
    if alinhamento:
        return 'a'
    else:
        return 'b'


# cabecalho1(texto=43, alinhamento='geek')


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


print(cabecalho2(texto='42', alinhamento=False))


# Fazendo o type hinting por comentário
nome = 'Geek University'  # type: str
