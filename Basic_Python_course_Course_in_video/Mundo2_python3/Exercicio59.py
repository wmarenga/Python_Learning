# Desafio 59:
# Crie um programa que leia DOIS VALORES e mostre um
# MENU na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada
# em cada caso.

from time import sleep
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print("""
    Escolha a operação desejada:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    escolha = int(input('>>>>> Digite sua escolha: '))
    if escolha == 1:
        soma = num1 + num2
        print(
            'A soma entre \033[1;32m{}\033[m + \033[1;32m{}\033[m = \033[7;31;47m{}\033[m'.format(num1, num2, soma))
    elif escolha == 2:
        mult = num1 * num2
        print('O resultado de \033[1;32m{}\033[m X \033[1;32m{}\033[m = \033[7;31;47m{}\033[m'.format(
            num1, num2, mult))
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre \033[1;32m{}\033[m e \033[1;32m{}\033[m, o maior valor é \033[7;31;47m{}\033[m'.format(
            num1, num2, maior))
    elif escolha == 4:
        print('Informe os números novamente: ')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte Sempre!')
