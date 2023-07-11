# Exercício 18 - Dígitos Adjacentes:
# Escreva um programa que receba um número inteiro na entrada
# e verifique se o número recebido possui ao menos um dígito
# com um dígito adjacente igual a ele. Caso exista, imprima "sim";
# se não existir, imprima "não".
# Exemplos:
# Digite um número inteiro: 12345
# não
# Digite um número inteiro: 1011
# sim

num = int(input('Digite um número inteiro: '))

num_anterior = num % 10
num = num // 10
igual_adjacente = False
pos = 0

while num > 0 and not igual_adjacente:
    atual = num % 10
    if atual == num_anterior:
        igual_adjacente = True
    else:
        pos += 1
        num_anterior = atual
    num = num // 10
if igual_adjacente:
    print('sim')
else:
    print('não')
