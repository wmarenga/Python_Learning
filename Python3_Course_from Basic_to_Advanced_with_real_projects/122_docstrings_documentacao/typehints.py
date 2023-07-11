""" Documentação deste módulo

Ele não faz nada, mas é só um exemplo para você.
Typiging - https://docs.python.org/3/library/typing.html
"""
from typing import Union
x: int = 10
y: float = 10.5
z: bool = False


def funcao(p1: float, p2: str, p3: dict):
    return p1, p2, p3


# não apresentará erro, pois definimos os typos de parâmetros corretos.
funcao(1.1, 'str', {})

# Não apresentará erro, pois definimos que a função retornará um float como resultado.


def funcao2(p1: float, p2: str, p3: dict) -> float:
    return 10.10


print(funcao2(10.2, 'str', {}))


# Funçao retornando mais de um tipo de valor
# from typing import Union

def funcao3() -> Union[list, dict]:
    return []
