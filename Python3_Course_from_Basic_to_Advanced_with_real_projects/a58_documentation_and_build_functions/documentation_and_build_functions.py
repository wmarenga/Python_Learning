"""
Built-in Functions:

Documentation:
https://docs.python.org/3/library/stdtypes.html

https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py

# isnumeric(), isdigit() and isdecimal() => return the same result.

# Numbers and positives (123456789)
# Obs: Note: If it is a float or any other negative value, it returns false.
# print(num1.isnumeric())
# print(num2.isnumeric())

num1 = input('Type one number: ')
num2 = input('Type another number: ')

while True:
    if num1.isdigit() and num2.isdigit():
        print(float(num1) + float(num2))
        break
    else:
        print('Digite um valor válido!')
        num1 = input('Type one number: ')
        num2 = input('Type another number: ')


# If we want to convert any number (Teacher Solution):

import re


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^\-{,1}[0-9]+$', val):
        return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

###########
#  USAGE  #
###########


# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False

num1 = input('Type one number: ')
num2 = input('Type one number: ')

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print('ERROR')

# Using try/ except:

num1 = input('Type one number: ')
num2 = input('Type one number: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('ERROR')
"""
