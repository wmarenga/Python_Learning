"""
while em Python:

Utilizado para realizar ações enquanto uma condição for verdadeira.

Requisitos: Entender condições e operadores.

# Loop infinito
while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá {nome}!')

print('Não será executada.')

# Mostrar um número até 100
x = 0
while x <= 100:
    print(x, end='-')
    x += 1

print('Acabou!')

# Usando 'continue'
# Continuará executando e pula o x == 3
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue

    print(x)
    x += 1

print('Acabou')

# Usando 'break'
# Irá parar quando x == 3
x = 0
while x < 10:
    if x == 3:
        x += 1
        break

    print(x)
    x += 1

print('Acabou')
x = 0  # Coluna
while x < 10:
    y = 0  # Linha
    while y < 5:
        print(f'({x}, {y})', end=',')
        y += 1
    x += 1  # x = x + 1


print('Acabou!')

"""
# Criando uma calculadora básica
while True:
    print()

    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if num_1.isalpha() or num_2.isalpha():
        print('Digite um valor inteiro!')
        continue

    elif num_1.isdigit() and num_2.isdigit():
        num_1 = int(num_1)
        num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)

    sair = input('Deseja sair? [s]im ou [n]ão: ').lower()

    if sair == 's':
        break
