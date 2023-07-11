# Desafio 33:
# Faça um programa que leia três números e mostre e qual é o maior e qual é o menor.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O número menor é {}'.format(menor))
print('O número maior é {}'.format(maior))

# Solução simples:
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
num = [a, b, c]
ordenado = num.sort()
print('O menor número é {}: '.format(num[0]))
print('O maior número é {}'.format(num[len(num) - 1]))
