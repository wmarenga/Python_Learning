"""
Documentação:
http://mypy-lang.org/

pip install mypy

Para executar no terminal:
Obs: Somente faz sentido utilizar o MyPy com o Type Hinting (texto: str, alinhamento: bool = True)

>> mypy 160_Checagem_de_Tipos_com_MyPy/Checagem_de_Tipos_com_MyPy.py

:42: error: Argument "alinhamento" to "cabecalho" has incompatible type "str"; expected "bool"
Found 1 error in 1 file (checked 1 source file)

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))


print(cabecalho('geek university', alinhamento=True))

cabecalho(texto='4', alinhamento=True)

"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))


print(cabecalho('geek university', alinhamento=True))
