"""

AULA 20 - Funções (Parte 2):

Interactive Help:

# No console do Python:

help()

help> ** Digitar o que está precisando de ajuda **

quit ** para sair **

# Via comando:

help(input)

ou

print(input.__doc__)

exemplo:

help> print

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

# Docstrings:


def contador(i, f, p):
    
-> Faz uma contagem e mostra na tela.
: Param i: início da contagem
: Param f: fim da contagem
: Param p: passo da contagem
: Return: sem retorno
Função criada por Gustavo Guanabara do Curso em Vídeo

    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')


help(contador)

# Parâmetros Opcionais:


def somar(a=0, b=0, c=0):

-> Faz a soma de três valores e mostra o resultado na tela.
: Param a: Primeiro Valor
: Param b: Segundo Valor
: Param c: Terceiro Valor
Função criada por Gustavo Guanabara do Curso em Vídeo

    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 2)  # O parâmetro c é opcional.
somar(3)
somar()
somar(b=4, c=2)
somar(c=2, a=1)

# Escopo (local) de Variáveis (Globais e Locais):


def teste():
    x = 8  # Variável local.
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa Principal


n = 2  # Variável Global (funciona dentro e fora da função).
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')
# Não funciona, pois x é uma variável local.
#     NameError: name 'x' is not defined

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 Global vale {n1}')

def teste(b):
    global a  # A variável 'A' local para a seu a variável Global.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')

# Retorno de Resultados:
# Comando Return:


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(1, 7)
somar(4)

# Usando o Return:


def somar(a=0, b=0, c=0):
    s = a + b + c
#   (substituir pelo return) print(f'A soma vale {s}')
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Os resultados foram {r1}, {r2}, {r3}.')

# Prática da aula:
# Foi definido o valor 1, quando não for informado nenhum valor.


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')

# Podemos utilizar o return para True ou False:


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))

# Outra maneira:

if par(num):
    print('É par!')
else:
    print('É Ímpar!')
    
"""
