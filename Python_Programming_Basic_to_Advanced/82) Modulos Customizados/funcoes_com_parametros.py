"""
Funcoes com Parametros (de entrada):

- Funcoes que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma funcao, ja sabemos que temos funcoes que:

- Nao possuem entrada;
- Nao possuem saida;
- Possuem entrada mas nao possuem saida;
- Nao possuem entrada mas possuem saida;
- Possuem entrada e saida;

# Fumcao anterior

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

# Refatorando uma funcao

def quadrado(numero):
#    return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

print(quadrado())
# TypeError: quadrado() missing 1 required
positional argument: 'numero'

# Funcao anterior
def cantar_parabens():
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

# Refatorando a funcao
def cantar_parabens(aniversariante):
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o {aniversariante}')


cantar_parabens('Wellington')
# Funcoes podem ter n parametros de entrada, ou seja,
# podemos receber como entrada em uma funcao quantos
# parametros forem necessarios. Eles sao separados por
# vírgula.

# Exemplos:

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# Obs: Se informarmos um numero errado de parametro ou argumentos,
# teremos TypeError

print(soma(2, 3, 4)) # TypeError - Informando menos argumentos
print(soma(4)) # TypeError - Informando menos argumentos

# Nomeando Parametros

def nome_completo(nome, sobrenome): # nome e sobrenome sao
parametros para receber argumentos
    return f'Seu nome completo e {nome} {sobrenome}'

print(nome_completo('Angelina', "Jolie")) # Sao argumentos
os dados que a funcao vai receber

# A diferenca entre Parametros e Argumentos

# Parametros sao variaveis declaradas na definicao de uma funcao;
# Argumentos sao dados passados durante a execucao de uma funcao;

# A ordem dos parametros e primordial

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
# Erro comum na utilizacao do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla)))
"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
