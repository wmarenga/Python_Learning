nome1 = 'Fernando'
nome2 = 'Maria'

''' Se usarmos elif, o codigo para quando o if for verdadeiro. Mesmo que a condicao em
elif seja verdadeira '''
if nome1 == 'Fernando':
    print(f'Bem-vindo {nome1}!!!')
elif nome2 == 'Maria':
    print(f'Bem-vinda {nome2}!!!')
else:
    print('Erro: Nome desconhecido.')
