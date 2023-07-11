"""
# Desafio 102:
# Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e outro
# chamado show, que será um valor lógico (opcional) indicando se será
# ou não mostrado na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    from math import factorial
    fact = factorial(num)
    return f'O fatorial de {num} é {fact}.'


print(fatorial(int(input('Digite o número para calcular o fatorial: '))))
"""
# SOLUÇÃO DO PROFESSOR:


def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# PROGRAMA PRINCIPAL:
print(fatorial(4, show=False))

# FORMA DO ALUNO:


def fatorial(n=1, show=False):
    """
        => Calcula o fatorial de um número.
        :param n: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do fatorial de um número n.
    """
    m = 1
    conta = f''
    for c in range(n, 0, -1):
        m *= c
        if c > 1:
            conta += f'{c} X '
        elif c == 1:
            conta += f'{c}'
    if show == True:
        return f'{conta} = {m}'
    else:
        return m


print(fatorial(int(input('Digite um número: ')), show=True))
