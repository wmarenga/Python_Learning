"""
Exercício 1:
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro.
"""
"""
num = input('Digite um número: ')

while True:
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print(f'O número {num} é par.')
        else:
            print(f'O número {num} é ímpar.')
        break
    elif num.isalpha():
        print('Digite um valor inteiro!')
        num = input('Digite um número: ')
    else:
        print('Digite um valor inteiro válido!')
        num = input('Digite um número: ')
"""
"""
Exercício 2:
Faça um programa que pergunte a hora ao usuário e, baseando-se no
horário descrito, exiba a saudação apropriada.
Ex.: Bom dia 0 ás 11, Boa tarde 12 ás 17 e Boa noite 18 ás 23.
"""
hora = input('Que horas são agora, por favor (somente numeros): ')
minuto = input('Que minutos são agora, por favor (somente numeros): ')


while True:
    if hora.isdigit() and minuto.isdigit():
        hora = int(hora)
        minuto = int(minuto)
        if hora >= 00 and hora < 12:
            print(f'Bom dia agora são {hora}:{minuto}')
        elif hora >= 12 and hora < 18:
            print(f'Boa tarde agora são {hora}:{minuto}')
        else:
            print(f'Boa noite agora são {hora}:{minuto}')
        break
    elif hora.isalpha() or minuto.isalpha():
        print('Digite somente números!')
        hora = input('Que horas são agora, por favor (somente numeros): ')
        minuto = input('Que minutos são agora, por favor (somente numeros): ')
    else:
        print('Digite somente números inteiros!')
        hora = input('Que horas são agora, por favor (somente numeros): ')
        minuto = input('Que minutos são agora, por favor (somente numeros): ')

"""
Exercício 3:
Faça um programa que peça o primeiro nome do usuário. Se o nome
tiver 4 letras ou menos escreva: "Seu nome é curto"; se tiver entre
5 e 6 letras, escreva: "Seu nome é normal"; maior que 6 letras
escreva: "Seu nome é muito grande".
"""
"""
primeiro_nome = input('Digite o seu primeiro nome: ').capitalize()

if len(primeiro_nome) <= 4:
    print(
        f'Oi {primeiro_nome}!, seu nome só tem {len(primeiro_nome)} letras, seu nome é CURTO!')
elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
    print(
        f'Oi {primeiro_nome}!, seu nome tem {len(primeiro_nome)} letras, seu nome é NORMAL!')
else:
    print(
        f'Oi {primeiro_nome}!, seu nome tem {len(primeiro_nome)} letras, seu nome é MUITO GRANDE!')
"""
