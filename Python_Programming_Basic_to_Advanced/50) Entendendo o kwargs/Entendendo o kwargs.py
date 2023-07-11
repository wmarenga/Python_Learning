""" 
Entendendo **kwargs:

Assim como no *args (*xis), tambem poderiamos usar qualquer nome para **kwargs (**xis), mas
por convensao chamamos de **kwargs.

Este e so mais um parametro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parametros nomeados, e transforma estes parametros extras em
um dicionario.

# Exemplo:
#def cores_favoritas(**kwargs):
#    print(kwargs)
    
#cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Exemplo (poderiamos passar outros parametros junto com o **kwargs):
def cores_favoritas(a=1, b=2, **kwargs):
    print(f'{a + b} {kwargs}')
    
cores_favoritas(3, 4, marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} e {cor}')
        # Usamos title() para converter as primeiras letras para maiuscula
    
cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs: Os parametros *args e **kwargs nao sao obritorios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Nao tenho certeza quem voce e ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funcoes, podemos ter (NESTA ORDEM):

# - Parametros Obrigatorios;
# - *args;
# - Parametros default (nao obrigatorios);
# - **kwargs

# Exemplo

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos') # Parametros Obrigatorios
    print(args) # args
    if solteiro: 
        print('Solteiro') # Parametros default
    else:
        print('Casado') # Parametros default
    print(kwargs) # kwargs

minha_funcao(8, 'Julia') # Somente os parametros obrigatorios
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True) # Obrigatorios, args(4, 5, 3) e alterando o default (solteiro)
minha_funcao(34, 'Felipe', eu='Nao', voce='Vai') # Obrigatorios, args (nada), e kwargs (nomeados - chave:valor)
minha_funcao(19, 'Carla', 9, 4, 3, java=False, Python=True) # Obrigatorios, args (9, 4, 3) e kwargs (chave:valor)

# Entendendo por que e importante manter esta ordem dos parametros na declaracao

# Funcao com a ordem correta de parametros
#def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Redefinindo com a ordem incorreta de parametros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

# Devido a declaracao errada o args ficou vazio e o instrutor recebeu o valor 3
Output:
#>>>[1, 2, (), 3, {'sobrenome': 'University', 'cargo': 'Instrutor'}]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

Retorna uma lista com:
a = 1 # Inteiro
b = 2 # Inteiro
args = (3,) # Tupla
instrutor = 'Geek' # String
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'} # Dicionario

# Desempacotar com **kwargs:
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))

# Outro Exemplo:
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3] # Lista
tupla = (1, 2, 3) # Tupla
conjunto = {1, 2, 3} # Set

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# Obs: Os nomes da chave em um dicionario (argumentos => a, b, c) devem ser o mesmo 
# dos (parametros => a, b, c) da funcao.
dicionario = dict(d=1, e=2, f=3)

soma_multiplos_numeros(**dicionario) # TypeError: soma_multiplos_numeros() got an unexpected keyword argument 'd'

# Podemos desempacotar um dicionario e tambem passar outros parametros juntos

def soma_multiplos_numeros(a, b, c, **kwargs):
    print (a + b + c)
    print(kwargs)


dicionario = dict(a=1, b=2, c=3, nome='Geek')

soma_multiplos_numeros(**dicionario, lang='Python')
"""
