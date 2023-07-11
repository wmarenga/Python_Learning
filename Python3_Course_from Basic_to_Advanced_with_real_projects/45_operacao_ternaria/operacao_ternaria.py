"""
Operador ternário em Python:

logged_user = True  # logado
# logged_user = False  # não logado

# Exemplo de operador ternário
msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'

# Não ternário
# if logged_user:
#     msg = 'Usuário logado'
# else:
#     msg = 'Usuário precisa logar'

print(msg)

# Outro exemplo
# Não ternário
idade = 18

if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')


"""

# Outro exemplo
# Ternário
idade = input('Qual a sua idade? ')

while not idade.isnumeric():
    print('Você precisa digitar apenas números!')
    idade = input('Qual a sua idade? ')
else:
    idade = int(idade)
    eh_maior = (idade >= 18)
    msg = 'Pode acessar' if eh_maior else 'Não pode acessar'

print(msg)
