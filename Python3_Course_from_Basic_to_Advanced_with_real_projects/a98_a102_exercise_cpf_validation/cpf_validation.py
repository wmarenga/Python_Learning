"""
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

! Replacing NOT numbers with regular expression (re):

cpf = re.sub(r'[^0-9]', '', input('Enter your CPF: '))

[^0-9] => everything that is not a number

! With .replace():

cpf = input('Enter your CPF: ').replace('.', '').replace('-', '')

"""
import re

while True:
    cpf = re.sub(r'[^0-9]', '', input('Enter your CPF: '))
    digit1 = 0
    digit2 = 0
    n1 = 10
    n2 = 11

    if len(cpf) != 11:
        print('Invalid CPF!! Enter exactly 11 digits: ')
        continue

    cpf9 = cpf[:9]

    # Finding the first digit:

    while n1 in range(10, 1, -1):
        for cp in cpf9:
            digit1 += int(cp) * n1
            n1 -= 1

    dig1 = 11 - (digit1 % 11)
    if dig1 > 9:
        dig1 = 0
        cpf_valition1 = cpf9 + str(dig1)
    else:
        cpf_valition1 = cpf9 + str(dig1)

    # Discovering the second digit:

    while n2 in range(11, 1, -1):
        for cp in cpf_valition1:
            digit2 += int(cp) * n2
            n2 -= 1

    dig2 = 11 - (digit2 % 11)
    if dig2 > 9:
        dig2 = 9
        cpf_valition2 = cpf_valition1 + str(dig2)
    else:
        cpf_valition2 = cpf_valition1 + str(dig2)

    while cpf != cpf_valition2:
        print(f'CPF was NOT validated = {cpf}!!!')
    else:
        print(f'The CPF = {cpf} is valid!')
        decision = input(
            'Do you want to check another CPF? [Y]es or [N]o: ').upper()
        while decision not in 'YN':
            decision = input('Type only [Y]es or [N]o: ').upper()
        if decision == 'Y':
            continue
        else:
            break
