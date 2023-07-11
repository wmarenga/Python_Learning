''' Realize a criacao de uma simples tabuada que e exibida em tela
para o usuario.'''

tabuada = int(input('Digite o numero para ver a tabuada: '))

for t in range(1, 11):
    print(f'{t} X {tabuada} = {t * tabuada}')
