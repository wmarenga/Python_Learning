"""
CPF Generator:

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
Digit 1 = 0            #       Digit 2 = 9
"""
from random import randint


while True:
    cpf_random = str(randint(0, 999999999))
    partial_sum1 = 0
    partial_sum2 = 0
    n1 = 10
    n2 = 11

    # Finding the first digit:

    while n1 in range(10, 1, -1):
        for cp in cpf_random:
            partial_sum1 += int(cp) * n1
            n1 -= 1

    dig1 = 11 - (partial_sum1 % 11)
    if dig1 > 9:
        dig1 = 0
        cpf_validation1 = cpf_random + str(dig1)
    else:
        cpf_validation1 = cpf_random + str(dig1)

    # Finding the second digit

    while n2 in range(11, 1, -1):
        for cp in cpf_validation1:
            partial_sum2 += int(cp) * n2
            n2 -= 1

    dig2 = 11 - (partial_sum2 % 11)
    if dig2 > 9:
        dig2 = 9
        cpf_validation2 = cpf_validation1 + str(dig2)
    else:
        cpf_validation2 = cpf_validation1 + str(dig2)

    print(
        f'The valid CPF is: {cpf_validation2[0:3]}.{cpf_validation2[3:6]}.{cpf_validation2[6:9]}-{cpf_validation2[9:12]}')

    decisao = input(
        'Do you want to generate another CPF? [Y]es or [N]o: ').upper()

    while decisao not in 'YN':
        decisao = input('Type only [Y] ou [N]: ').upper()
    if decisao == 'Y':
        continue
    else:
        break
