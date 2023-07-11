# Estruturas de Repeticao

validador = input('Digite "Brasil" para continuar: ')

while validador != 'Brasil':
    print('Palavra-chave nao confere, digite novamente: ')
    validador = input('Digite "Brasil" para continuar: ')

    if validador == 'Brasil':
        print('Agora voce digitou Brasil corretamente!!!')
