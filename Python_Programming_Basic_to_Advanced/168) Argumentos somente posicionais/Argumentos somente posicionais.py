"""
Argumentos Somente Posicionais

Significa que temos que usar a variável somente. Não podemos fazer declaração
nomeada.

float(x=0, /) por causa desta barra

Exemplo:

print(float(valor)) sim

print(float(x=valor)) não

valor = '67.3'

print(float(valor))

print(valor := 67.3) # Usando Walrus

Exemplo sem a barra:

def cumprimenta_v1(nome):
    return f'Olá {nome}'

print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome='Geek'))



Exemplo com a barra:

def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek'))

Obs: Passando a /, estamos declarando que o parâmetro 'nome' não poderá ser
nomeado.

Exemplo com 2 parâmetros (primeiro posicional - sem possibilidade de
nomeação e segundo nomeado com valor previamente definido)


def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('University', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-vinda'))
# print(cumprimenta_v3(nome='Felicity', 'Bem-vinda'))

A barra indicará que tudo que estiver antes delas, será posicional (mesmo
com parâmetro nomeado).


def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'


print(cumprimenta_v4('Geek'))
print(cumprimenta_v4('Felicity', 'Bem-vinda'))
# print(cumprimenta_v4('University', mensagem='Hello'))

Utilizando o *, estamos dizendo que todos os parâmetros após o * terão que ser
nomeados (obrigatório nomerar os parâmetros).


def cumprimenta_v5(*, nome):
    return f'Olá {nome}'


print(cumprimenta_v5(nome='Geek'))
# print(cumprimenta_v5('Geek'))

Descrição:

def cumprimentar_v6(somente sem nomeação, /, opcional nomear, *, obrigatório
nomear):


def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimentar_v6('Geek', mensagem1='Hello', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Geek', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Geek', 'Oi', mensagem2='Vamos?'))
# Irá apresentar erro pois 'mensagem2 ter que ser nomeado'
#print(cumprimentar_v6('Geek', 'Oi', 'Vamos?'))
"""
