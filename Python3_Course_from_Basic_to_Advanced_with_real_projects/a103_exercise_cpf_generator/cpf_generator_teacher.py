from random import randint
import re

while True:
    cpf_quantity = re.sub(
        r'[^0-9]', '', input("How many cpf's do you want to generate? "))
    if cpf_quantity == '':
        print("Enter only integer numbers!")
    else:
        break


for _ in range(int(cpf_quantity)):
    number = str(randint(100000000, 999999999))

    new_cpf = number                   # 9 random numbers
    reverse = 10                        # reverse counter
    total = 0                           # The total of multiplications

    # Loop of CPF
    for index in range(19):
        if index > 8:                   # First index goes from 0 to 9,
            index -= 9                  # These are the first 9 digits of the CPF

        # Total value of the multiplication
        total += int(new_cpf[index]) * reverse

        reverse -= 1                    # Decrease the reverse counter
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:                   # If the digit is > 9 the value is 0
                d = 0
            total = 0                   # Zero the total
            # Concatenates the digit generated in the new cpf
            new_cpf += str(d)

    print(new_cpf)
