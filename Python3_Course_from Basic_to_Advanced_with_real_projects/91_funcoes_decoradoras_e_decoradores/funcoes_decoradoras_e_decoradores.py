"""
Funções Decoradoras:

As funções decoradores envolvem um método mudando ou não o comportamento
da função ou classe.
Utilizamos os decoradores para adicionar funcionalidades extras a outras
funções ou classes.

def fala_oi():
    print('Oi')


# fala_oi()

# Jogando um função em uma variável
variavel = fala_oi

variavel()
print(type(variavel))  # <class 'function'>


def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave  # retorna a função sem executar


@master
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)


# fala_oi = master(fala_oi)
# fala_oi()
# print(type(fala_oi))  # <class 'function'>

outra_funcao('Ola, eu sou Luiz.')
"""
from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        # Tempo em milisegundos
        tempo = (end_time - start_time) * 1000
        print(
            f'\nA função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(10000):
        print(i, end=" - ")
        # sleep(1)


demora()
