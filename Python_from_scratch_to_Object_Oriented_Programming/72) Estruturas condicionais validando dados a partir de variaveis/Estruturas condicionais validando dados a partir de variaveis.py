nome = input('Digite o seu nome: ')

funcionarios_homens = ['Carlos', 'Jose', 'Paulo']
funcionarias_mulheres = ['Ana', 'Barbara', 'Maria', 'tatiana']

if nome == 'Fernando':
    print(f'Ola {nome}, voce e o adminstrador do sistema!!!')
elif nome in funcionarias_mulheres:
    print(f'Bem vinda {nome}, voce e uma usuaria registrada no sistema.')
elif nome in funcionarios_homens:
    print(f'Bem vindo {nome}, voce e um usuario registrado no sistema.')
else:
    print(
        f'Ola {nome}, voce nao esta logado no sistema, suas permissoes sao restritas')
