"""
def lin():
    print('-'*30)


print('-'*30)

# PROGRAMA PRINCIPAL
título('    CURSO EM VÍDEO    ')

título('    APRENDA PYTHON    ')
título('    GUSTAVO GUANABARA    ')
# PROGRAMA PRINCIPAL (Entre a "DEF" e o programa principal devemos deixar duas linha.)
lin()
print('        CURSO EM VÍDEO        ')
lin()
lin()
print('        APRENDA PYTHON        ')
lin()
lin()
print('       GUSTAVO GUANABARA      ')
lin()

def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


# PROGRAMA PRINCIPAL
título('        CURSO EM VÍDEO    ')
título('        APRENDA PYTHON    ')
título('       GUSTAVO GUANABARA    ')

# Maneira comum de somar.
a = 4
b = 5
s = a + b     # => soma(4, 5)
print(s)

a = 8
b = 9
s = a + b     # => soma(8, 9)
print(s)

a = 2
b = 1
s = a + b     # => soma(2, 1)
print(s)

# DEFINIÇÃO DE FUNÇÃO SOMA.
def soma(a, b):
    s = a + b
    print(s)


# PROGRAMA PRINCIPAL
soma(4, 5)
soma(8, 9)
soma(2, 1)

# PODEMOS ESPECIFICAR OS PARÂMETROS:
soma(a=4, b=3)
soma(b=6, a=1)

------------------------------------
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# PROGRAMA PRINCIPAL
soma(4, 5)
soma(b=4, a=5)

# São colocados os valores dentro de uma TUPLA.


def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
#    print(type(núm))


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# (2, 1, 7) <class 'tuple'>
# (8, 0) <class 'tuple'>
# (4, 4, 7, 6, 2) <class 'tuple'>


def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# TRABALHANDO COM LISTAS.


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

------------------------------

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(2, 9, 4)

"""
