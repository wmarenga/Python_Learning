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
    # Discovering the digits:
    partial_cpf = str(randint(100000000, 999999999))

    def digit(mult, start_mult, cpf, passing=1):
        summatory = 0
        while mult in range(start_mult, 1, -1):
            for c in cpf:
                summatory += int(c) * mult
                mult -= 1
        if passing == 1:
            dig = 11 - (summatory % 11)
            if dig > 9:
                dig = 0
                return cpf + str(dig)

            else:
                return cpf + str(dig)
        else:
            dig = 11 - (summatory % 11)
            if dig > 9:
                dig = 9
                return cpf + str(dig)

            else:
                return cpf + str(dig)

    valid_cpf = digit(11, 11, digit(10, 10, partial_cpf), passing=2)

    print(
        f'The valid CPF is: {valid_cpf[0:3]}.{valid_cpf[3:6]}.{valid_cpf[6:9]}-{valid_cpf[9:11]}')

    decision = input(
        'Do you want to generate another CPF? [Y]es or [N]o: ').upper()

    while decision not in 'YN':
        decision = input('Type only [Y] or [N]: ').upper()
    if decision == 'Y':
        continue
    else:
        break
