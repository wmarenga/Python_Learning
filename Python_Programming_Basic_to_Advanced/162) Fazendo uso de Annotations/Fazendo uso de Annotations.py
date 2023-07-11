"""
Os Annotations nos ajudam a utilizar o Tye Hinting.

texto: str
str => Annotation

Correto:

texto: str

Incorreto:

texto:str
texto : str

Correto (retorno):

) -> str

Incorreto (retorno):

)->str
) ->str

# Correto

alinhamento: bool = True

# Incorreto

alinhamento:bool=True

alinhamento : bool = True

alinhamento : bool=True

alinhamento: bool= True

import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


# print(circunferencia.__annotations__)
# {'raio': <class 'float'>, 'return': <class 'float'>}

nome: str = 'Geek University'

peso: float = 67.9

ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)
# Annotations das variáveis globais
# {'nome': <class 'str'>, 'peso': <class 'float'>, 'ativo': <class 'bool'>}



"""


class Pessoa:
    # Uma função que não retorna nada, retorna None
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Geek University', idade=37, peso=69.5)

print(p.__dict__)
# {'_Pessoa__nome': 'Geek University', '_Pessoa__idade': 37, '_Pessoa__peso': 69.5}

# print(p.__annotations__) Não tem annotations

print(p.andar.__annotations__)
# {'return': <class 'str'>}

print(p.__init__.__annotations__)
# {'nome': <class 'str'>, 'idade': <class 'int'>, 'peso': <class 'float'>, 'return': None}
