# Estruturas condicionais com Interpolacao:

nomes = ['Fernando', 'Maria', 'Carlos']

usuario = input('Digite o seu nome: ')

if usuario in nomes:
    print(f'Bem-vindo(a) {usuario}!!')
else:
    print(f'Usuario {usuario} nao cadastrado')
