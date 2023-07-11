# Desafio 66:
# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

num = soma = cont = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos números é {soma} e foram digitados {cont}')
