# Exercicio 17 - Checagem de Primos:
# Escreva um programa que receba um número inteiro positivo na
# entrada e verifique se é primo. Se o número for primo, imprima
# "primo". Caso contrário, imprima "não primo".
# Exemplos:
# Digite um número inteiro: 13
# primo
# Digite um número inteiro: 12
# não primo

n = int(input('Digite um número inteiro: '))

count = 2
primo = True

while count < n and primo:
    primo = not (n % count == 0)
    count += 1
if (primo):
    print('primo')
else:
    print('não primo')
