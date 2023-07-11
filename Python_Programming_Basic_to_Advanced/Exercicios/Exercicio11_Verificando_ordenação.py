# Exercicio 10 - Verificando ordenação:
# Receba 3 números inteiros na entrada e imprima
# crescente
# se eles forem dados em ordem crescente. Caso contrário, imprima
# não está em ordem crescente.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 < num2 and num1 < num3 and num2 < num3:
    print('crescente')
else:
    print('não está em ordem crescente')
