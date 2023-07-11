# Desafio 37:
# Escreva um programa que leia um número inteira qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário;
# 2 para octal;
# 3 para hexadecimal.

d = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para convesão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
conv = int(input('Digite a opção desejada: '))
if conv == 1:
    print('O seu número decimal {} convertido para binário é {}.'.format(
        d, bin(d)[2:]))
elif conv == 2:
    print('O seu número decimal {} convertido para octal é {}.'.format(
        d, oct(d)[2:]))
elif conv == 3:
    print('O seu número decimal {} convertido para hexadecimal é {}.'.format(
        d, hex(d)[2:]))
else:
    print('Opção inválida! Tente novamente usando os números (1, 2 ou 3)')
