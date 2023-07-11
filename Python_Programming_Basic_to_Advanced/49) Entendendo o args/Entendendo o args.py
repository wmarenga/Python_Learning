""" 
Entendendo o *args:

- O *args e um parametro, como outro qualquer. Isso significa que voce podera 
chamar de qualquer coisa, desde que comece com asterisco. 

Exemplo:

*xis
Mas por convensao, utilizamos *args para defini-lo. 

O que seria o *args?

O parametro *args utilizado em uma funcao, coloca os valores extras informados como entrada
em uma tupla. Entao desde ja lembre-se que tuplas sao imutaveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

print(4, 6) # TypeError (Colocando parametros default nao teriamos este erro)
print(4, 6, 9, 5) # TypeError (mesmo colocando parametros default, ainda teriamos TypeError)

# Se quisermos informar 10 argumentos, como fariamos?

# Entendento o args:

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros() # Retorna uma tupla vazia ()
soma_todos_numeros(1) # Retorna uma tupla vazia (1,)
soma_todos_numeros(2, 3) # Retorna uma tupla vazia (2, 3)
soma_todos_numeros(2, 3, 4) # Retorna uma tupla vazia (2, 3, 4)
soma_todos_numeros(3, 4, 5, 6) # Retorna uma tupla vazia (3, 4, 5, 6)

# Fazendo uma soma utilizando args:

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# Otimizando o codigo (refatorando):

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# Tambem poderiamos utilizar numeros reais

print(soma_todos_numeros(23.4, 12.5))

# Podemos definir parametros extras com o args

def soma_todos_numeros(nome, sobrenome, *args):
    return f'O nome e {nome}, o email e {sobrenome} e a soma e {sum(args)}'

print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))
print(soma_todos_numeros('Angelina', 'Jolie', 23.4, 12.5))

# Outro exemplo de utilizacao do *args
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu nao tenho certeza quem vece e ...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

def soma_todos_numeros(*args):
    return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

#numeros = [1, 2, 3, 4, 5, 6, 7]
#print(soma_todos_numeros(numeros)) # TypeError

# Utilizando o desempacotador

#numeros = [1, 2, 3, 4, 5, 6, 7] # Listas
#num1, num2, num3, num4, num5, num6, num7 = numeros # Desempacotamentos Manual
#numeros = (1, 2, 3, 4, 5, 6, 7) # tuplas
numeros = {1, 2, 3} # set, conjunto

print(soma_todos_numeros(*numeros))

# O asterisco (*) serve para que informemos ao Python que estamos passando como 
# argumento uma colecao de dados. Desta forma, ele sabera que precisa, antes, 
# desempacotar estes dados. Serve para listas, tuplas
"""