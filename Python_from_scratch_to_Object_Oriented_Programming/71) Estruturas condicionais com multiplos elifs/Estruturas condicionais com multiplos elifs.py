nome = input('Digite o seu nome: ')

if nome == 'Fernando':
    print(f'Ola {nome}, voce e o adminstrador do sistema!!!')
elif nome in 'Ana Barbara Maria Tatiana':
    print(f'Bem vinda {nome}, voce e uma usuaria registrada no sistema.')
elif nome in 'Carlos Jose Paulo':
    print(f'Bem vindo {nome}, voce e um usuario registrado no sistema.')
else:
    print(f'Ola {nome}, voce nao esta logado no sistema, suas permissoes sao restritas')
