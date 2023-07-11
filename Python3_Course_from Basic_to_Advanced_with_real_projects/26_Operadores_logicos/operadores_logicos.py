"""
Operadores Lógicos:

and     => e (ambas tem que ser True para ser True)
or      => ou (uma ou outra têm que ser True para ser True)
not     => não (inversor de valores)
in      => está em, no, na
not in  => não está em, no, na

a = 2
b = 2
c = 3

# Exemplo de and:
print(a == b and b < c)  # True (True and True)
print(a == b and b > c)  # False (True and False)
print(a != b and b < c)  # False (False and True)
print(a != b and b > c)  # False (False and False)

# Exemplo de or:
print(a == b or b < c)  # True (True or True)
print(a == b or b < c)  # True (True or False)
print(a != b or b < c)  # True (False or True)
print(a != b or b > c)  # False (False or False)

# Exemplo de not:
print(not c > a)  # False (c > a == True) invertido seria False.
print(not c < b)  # True (c < b == False) invertido seria True.

a = ''  # Considerado bool False
b = 0   # Considerado bool False

if not a:
    print('Por favor, preencha o valor de A.')

if not b:
    print('Por favor, preencha o valor de B.')

# Exemplo de in:
nome = 'Luiz Otávio'

if 'u' in nome:
    print('Existe a letra "u" no seu nome.')

if 'otá' in nome:
    print('Existe')
else:
    print('Não existe.')

# Exemplo de not in:
if 'vio' not in nome:
    print('Executei.')
else:
    print('Existe o texto.')

# Sistema básico de validação de senha

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
"""
