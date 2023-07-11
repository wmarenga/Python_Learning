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
    # Descobrindo os dígito:
    cpf_parc = str(randint(100000000, 999999999))

    def digito(mult, start_mult, cpf, passagem=1):
        somatorio = 0
        while mult in range(start_mult, 1, -1):
            for c in cpf:
                somatorio += int(c) * mult
                mult -= 1
        if passagem == 1:
            dig = 11 - (somatorio % 11)
            if dig > 9:
                dig = 0
                return cpf + str(dig)

            else:
                return cpf + str(dig)
        else:
            dig = 11 - (somatorio % 11)
            if dig > 9:
                dig = 9
                return cpf + str(dig)

            else:
                return cpf + str(dig)

    cpf_valido = digito(11, 11, digito(10, 10, cpf_parc), passagem=2)

    print(
        f'O CPF válido é: {cpf_valido[0:3]}.{cpf_valido[3:6]}.{cpf_valido[6:9]}-{cpf_valido[9:11]}')

    decisao = input('Quer gerar outro CPF? [S]im ou [N]ão: ').upper()

    while decisao not in 'SN':
        decisao = input('Digite somente [S] ou [N]: ').upper()
    if decisao == 'S':
        continue
    else:
        break
