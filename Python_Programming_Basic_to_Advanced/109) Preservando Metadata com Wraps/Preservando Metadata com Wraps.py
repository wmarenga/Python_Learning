"""
Preservando Metadata com Wraps:

Metadados => São dados intrínsecos em arquivos.

Wraps => São funções que envolvem elementos com diversas finalidades.S

# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        "Eu sou uma função(logar) dentro de outra."
from functools import wraps
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    "Soma dois números."
    return a + b


#print(soma(10, 30))

print(soma.__name__)  # mostra o nome da função logar incorretamente
print(soma.__doc__)  # mostra a documentação da função logar (descrição) incorretamente
# help(soma)  # mostra a função logar e sua documentação incorretamente

"""

# Resolução do problema

from functools import wraps
# preserva o metadado da função


def ver_log(funcao):
    @wraps(funcao)  # somente incluindo este decorator, irá resolver o problema
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra."""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    "Soma dois números."
    return a + b


print(soma(10, 40))

print(soma.__name__)  # mostra o nome da função somar (resolvido)
print(soma.__doc__)  # mostra a documentação da função somar (descrição) - Resolvido
help(soma)  # mostra a função somar e sua documentação (resolvido)
