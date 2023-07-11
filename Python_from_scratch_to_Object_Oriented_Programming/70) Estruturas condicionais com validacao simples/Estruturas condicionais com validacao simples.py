# Estruturas condicionais com validacao simples (em string)

nome = input('Digite o seu nome: ')

if nome == 'Fernando':
    print('Ola {nome}, voce e o administrador do sistema!!!')
elif nome in 'Ana Barbara Carlos Jose Maria Paulo Tatiana':
    print(
        f'Bem vindo(a) {nome}, voce e um(a) usuario(a) registrado(a) no sistema.')
else:
    print(
        f'Ola {nome}, voce nao esta logado no sistema, suas permissoes sao restritas.')
