# Desafio 50:
# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS
# e mostre a soma apenas daqueles que foram PARES. Se o
# valor digitado for ÍMPAR, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}⁰ número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número(s) PARE(S) e a soma foi {}.'.format(cont, soma))
