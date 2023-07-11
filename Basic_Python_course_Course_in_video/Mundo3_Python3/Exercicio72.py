# Desafio 72:
# Crie um programa que tenha uma TUPLA totalmente preenchida
# com uma contagem por extenso, de ZERO até VINTE.
# Seu programa deverá ler um número pelo teclado (ENTRE 0 e 20)
# e mostrá-lo por EXTENSO.

tuplanum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número \033[7;32m{tuplanum[num]}\033[m')
    decisão = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while decisão not in 'SN':
        decisão = str(
            input('Responda novamente!!! Quer continuar? [S/N] ')).strip().upper()[0]
    if decisão == 'N':
        break
print(f'Você digitou o número \033[7;32m{tuplanum[num]}\033[m')
print('{:=^30}'.format(' PROGRAMA FINALIZADO '))
