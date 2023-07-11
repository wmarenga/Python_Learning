"""
Doctests:

Doctests são testes que colocamos na docstring das funções/métodos Python.


def soma(a, b):
    # Adicionar 3 aspas aqui
    # soma os números a e b

    # >>> soma(1, 2) # Tem que ser exatamente igual ao python console
    # 3

    # >>> soma(4, 6)
    # 10
    # Adicionar 3 aspas aqui
    return a + b

Para rodar um test do doctest:

python -m doctest -v nome_do_mobulo.py
python -m doctest -v 143_Doctests/Doctests.py

# Saída

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    # Adicionar 3 aspas aqui
    # duplica os valores em uma lista

    # >>> duplicar([1, 2, 3, 4])
    # [2, 4, 6, 8]

    # >>> duplicar([])
    # []

    # >>> duplicar(['a', 'b', 'c'])
    # ['aa', 'bb', 'cc']

    # >>> duplicar([True, None])
    # Traceback (most recent call last):
    #   ...
    # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    # Adicionar 3 aspas aqui
    #
    # pass  # ***Test Failed*** 4 failures.
    # return []  # ***Test Failed*** 3 failures.

    # 4 passed and 0 failed./ Test passed.
    return [2 * elemento for elemento in valores]

# ... => representa as informações entre os erros
print(duplicar([True, None]))
# Traceback (most recent call last):
#  File "c:/Users/wmare/OneDrive/Área de Trabalho/Curso_Atual/143_Doctests
# /Doctests.py", line 114, in <module>
#    print(duplicar([True, None]))
#  File "c:/Users/wmare/OneDrive/Área de Trabalho/Curso_Atual/143_Doctests
# /Doctests.py", line 111, in duplicar
#    return [2 * elemento for elemento in valores]
#  File "c:/Users/wmare/OneDrive/Área de Trabalho/Curso_Atual/143_Doctests
# /Doctests.py", line 111, in <listcomp>
#    return [2 * elemento for elemento in valores]
# TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

# Erro inesperado...

def fala_oi():
    # Adicionar 3 aspas aqui
    # Fala oi

    # >>> fala_oi()
    # 'oi'
    # Adicionar 3 aspas aqui

    # return "oi"

OBS: Dentro do doctest, o Python não reconhece string com aspas duplas.
Precisa ser aspas simples.

# Temos que usar aspas simples no 'oi' dentro do Docstring
# ***Test Failed*** 1 failures.
# Expected:
#     "oi"
# Got:
#    'oi'

# Um último caso estranho...


def verdade():
    # Adicionar 3 aspas aqui
    Retorna verdade

    # >>> verdade()
    True
    # Adicionar 3 aspas aqui
    return True
"""


def verdade():
    """
    Retorna verdade

    >>> verdade()
    True
    """
    return True
