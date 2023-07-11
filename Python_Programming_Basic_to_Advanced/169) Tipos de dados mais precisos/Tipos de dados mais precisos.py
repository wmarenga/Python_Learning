"""
int, str, float, List, Set, Dict, etc

def dobro(valor: int) -> int:
    return valor * 2


print(dobro(8))
print(dobro(42))
print(dobro('Geek'))  # Não irá apresentar erro.

# Utilizando o mypy teremos uma mensagem de erro.
# Argument 1 to "dobro" has incompatible type "str"; expected "int"mypy(error)

1) Literal type
2) Union
3) Final
4) Typed dictionaries
5) Protocols

1) Literal type

from typing import Literal


# Irá retornar uma string exata/ literal ['conectado', 'desconectado']
def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass

Exemplo sem o Literal type:

def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
calcula_v1('*', 3, 5)  # ValueError: Operação inválida '*' (operacao!r => '*')

Exemplo com Literal type

from typing import Literal


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
calcula_v2('*', 3, 5) # Argument 1 to "calcula_v2" has incompatible type "Literal['*']"; expected "Literal['+', '-']"mypy(error)

2) Union
from typing import Union


# -> Union[str, int]: # Poderá ser uma string ou integer.
def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado

Obs: Podemos utilizar o Union  em qualquer parâmetro da função.

3) Final

from typing import Final

NOME: Final = 'Geek'

print(NOME)

NOME = 'University' # Cannot assign to final name "NOME"mypy(error)

print(NOME)


# O final agora é com 'f' minúsculo, pois é um decorador.
from typing import final


@final
class Pessoa:
    pass

# Base class "Pessoa" is marked final and cannot be subclassedPylance


class Estudante():
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')


# Obs: As classes filha não devem sobrescrever o método.

4) Typed Dictionaries

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str  # Serão as chaves do dicionário
    atualizacao: int  # Serão os valores do dicionário


geek = CursoPython(versao='3.8.5', atualizacao=2020)

print(geek)

# Podemos informar chave: valor nomeados
outro = CursoPython(algo='vai', coisa=True) # (class) CursoPython(*, versao: str, atualizacao: int) Extra keys ("algo", "coisa") for TypedDict "CursoPython"mypy(error)

print(outro)

# 5) Protocols

from typing import Protocol


class Curso(Protocol):
    titulo: str

#    def __init__(self):
#        Curso.titulo = 'Programação em Python'


def estudar(valor: Curso) -> None:
    # Poderia chamar Curso.titulo também
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'


v1 = Venda()
# c1 = Curso()


# estudar(c1)
estudar(v1)
"""
