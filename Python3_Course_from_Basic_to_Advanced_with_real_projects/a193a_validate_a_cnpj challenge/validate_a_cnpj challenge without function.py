"""
04.252.011/0001-10
40.688.134/0001-61
71.506.168/0001-11
12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Formula -> 11 - (65 % 11) = 1

First digit = 1 (If the digit is greater than 9, it becomes 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Formula -> 11 - (67 % 11) = 10 (Since the result is greater than 9, then it is 0)

Second digit = 0

New CNPJ + Digits = 04.252.011/0001-10
Original CNPJ=       04.252.011/0001-10
Valid

Recap.
543298765432 -> First digit
6543298765432 -> Second digit
"""

cnpj = '04.252.011/0001-10'
dig1_mult = '543298765432'
dig2_mult = '6543298765432'
som_dig1 = int()
som_dig2 = int()

# Parsing and replacing characters
for c in cnpj:
    if not c.isdigit():
        cnpj = cnpj.replace(c, '')

cnpj_without_digits = cnpj[0:12]

# Calculating the first digit
for i1 in range(0, 12):
    som_dig1 += int(cnpj_without_digits[i1]) * int(dig1_mult[i1])

form_dig1 = 11 - (som_dig1 % 11)
if form_dig1 > 9:
    form_dig1 = 0
else:
    form_dig1

cnpj_dig1 = cnpj_without_digits + str(form_dig1)

# Calculating the second digit
for i2 in range(0, 13):
    som_dig2 += int(cnpj_dig1[i2]) * int(dig2_mult[i2])

form_dig2 = 11 - (som_dig2 % 11)
if form_dig2 > 9:
    form_dig2 = 0
else:
    form_dig2

cnpj_dig2 = cnpj_dig1 + str(form_dig2)

if cnpj == cnpj_dig2:
    print(f'The CNPJ {cnpj_dig2} is VALID!!')
else:
    print(f'The CNPJ {cnpj_dig2} is NOT VALID!!')
