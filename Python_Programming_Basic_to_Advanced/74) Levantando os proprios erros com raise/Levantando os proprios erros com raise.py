"""
Levantando os proprios erros com raise:

raise => lanca excecoes.

Obs: O raise nao e uma funcao. E uma palavra reservada, assim como def, ou qualquer outra em Python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas proprias excecoes e
mensagens de erro.

A forma geral de utilizar e:

raise TipoDoErro('Mensagem de erro')

# Exemplos

raise ValueError('Valor incorreto')

# Exemplo real:

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('A Cor precisa ser uma string')
    print(f'O texto {texto} sera impresso na cor {cor}')


colore('Geek', 'azul')
#colore(4, 'azul') # TypeError: O Texto precisa ser uma string
#colore('Geek', 4) # TypeError: A Cor precisa ser uma string

# Exemplo real - Refatorado:

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('A Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} sera impresso na cor {cor}')


colore('Geek University', 'verde')
colore('Geek University', 'preto') # ValueError: A cor precisa ser uma entre: ('verde', 'amarelo', 'azul', 'branco')

Obs: O raise, assim como o return, finaliza a funcao. Ou seja, nada apos o raise sera executado.
"""

