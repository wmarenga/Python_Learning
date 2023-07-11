"""
Gerador de CPF:

CPF = 168.995.350-90
___________________________________________________
1 * 10 = 10             #       1 * 11  = 11  <=
6 * 9  = 54             #       6 * 10  = 60
8 * 8  = 64             #       8 *  9  = 72
9 * 7  = 63             #       9 *  8  = 72
9 * 6  = 54             #       9 *  7  = 63
5 * 5  = 25             #       5 *  6  = 30
3 * 4  = 12             #       3 *  5  = 15
5 * 3  = 15             #       5 *  4  = 20
0 * 2  =  0             #       0 *  3  = 0
                        #   =>  0 *  2  = 0
        297             #                 343
11 - (297 % 11) = 11    #        11 - (343 % 11) = 9
11 > 9 = 0              #
Digito 1 = 0            #       Digito 2 = 9
"""
from random import randint

while True:
    cpf_aleatorio = str(randint(0, 999999999))
    soma_parcial1 = 0
    soma_parcial2 = 0
    n1 = 10
    n2 = 11

    # Descobrindo o primeiro dígito:

    while n1 in range(10, 1, -1):
        for cp in cpf_aleatorio:
            soma_parcial1 += int(cp) * n1
            n1 -= 1

    dig1 = 11 - (soma_parcial1 % 11)
    if dig1 > 9:
        dig1 = 0
        cpf_validacao1 = cpf_aleatorio + str(dig1)
    else:
        cpf_validacao1 = cpf_aleatorio + str(dig1)

    # Descobrindo o segundo dígito

    while n2 in range(11, 1, -1):
        for cp in cpf_validacao1:
            soma_parcial2 += int(cp) * n2
            n2 -= 1

    dig2 = 11 - (soma_parcial2 % 11)
    if dig2 > 9:
        dig2 = 9
        cpf_validacao2 = cpf_validacao1 + str(dig2)
    else:
        cpf_validacao2 = cpf_validacao1 + str(dig2)

    print(
        f'O CPF válido é: {cpf_validacao2[0:3]}.{cpf_validacao2[3:6]}.{cpf_validacao2[6:9]}-{cpf_validacao2[9:12]}')

    decisao = input('Quer gerar outro CPF? [S]im ou [N]ão: ').upper()

    while decisao not in 'SN':
        decisao = input('Digite somente [S] ou [N]: ').upper()
    if decisao == 'S':
        continue
    else:
        break
