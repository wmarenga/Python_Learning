"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digit 1 = 0          #   Digit 2 = 9

Calculation of the first digit of the CPF
CPF: 746.824.890-70
Collect the sum of the first 9 digits of the CPF
by multiplying each value by a countdown starting
from 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

- Sum all results:
70+36+48+56+12+20+32+27+0 = 301

- Multiply the previous result by 10
301 * 10 = 3010

- Get the remainder from dividing the previous account by 11
3010 % 11 = 7
If the previous result is greater than 9:
    result is 0
contrary to this:
    result is the value of the count

The first digit of the CPF is 7 (digit 10 after comma)

"""

# Infinite loop
while True:
    # cpf = '74682489070'
    cpf = input('Enter a CPF: ')
    # Eliminates the last two digits of the CPF
    new_cpf = cpf[:9]
    reverse = 10                        # reverse counter
    total = 0

    # Loop of CPF
    for index in range(19):
        if index > 8:                   # First index goes from 0 to 9,
            index -= 9                  # These are the first 9 Digits of the CPF

        # Total value of the multiplication
        total += int(new_cpf[index]) * reverse

        reverse -= 1                    # Decrease the reverse counter
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:                   # If the Digit is > 9 the value is 0
                d = 0
            total = 0                   # Reset the total
            # Concatenates the generated Digit into the new cpf
            new_cpf += str(d)

    # Avoid sequences. Ex: 11111111111, 00000000000...
    sequence = new_cpf == str(new_cpf[0]) * len(cpf)

    # I discovered that sequences evaluated as true, so I also added that check here.
    if cpf == new_cpf and not sequence:
        print('Valid')
    else:
        print('Invalid')
