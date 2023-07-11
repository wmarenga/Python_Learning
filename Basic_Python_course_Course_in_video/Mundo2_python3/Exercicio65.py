# Desafio 65:
# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo
# teclado. No final da execução, mostre a MÉDIA ENTRE TODOS
# os valores e qual foi o MAIOR e o MENOR valores lidos. O
# programa deve perguntar ao usuário se ele quer ou nao
# continuar a digitar valores.

decisão = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while decisão == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    decisão = str(input('Quer continuar? [S/ N]')).strip().upper()[0]
media = soma / cont
print('A média entre os números é {:.1f}'.format(media))
print('O números maior é {}'.format(maior))
print('O números menor é {}'.format(menor))
