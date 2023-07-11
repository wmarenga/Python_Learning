"""
Documentação:
https://docs.python.org/3/library/exceptions.html

# Exemplo


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise


try:
    print(divide(2, 0))  # ZeroDivisionError: division by zero
except ZeroDivisionError as error:
    print(error)
"""

# Exemplo customizado


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser zero.")
    return n1 / n2


print(divide(2, 1))

try:
    print(divide(n1=2, n2=0))  # ValueError: n2 não pode ser zero.
except ValueError as error:
    print('Você está tentando dividir por zero.')
    print('Log: ', error)
