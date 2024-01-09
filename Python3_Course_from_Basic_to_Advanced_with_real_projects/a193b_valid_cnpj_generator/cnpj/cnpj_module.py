import re
import random

REGRESSIVES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def validation(cnpj):
    cnpj = only_numbers(cnpj)

    try:
        if is_sequence(cnpj):
            return False
    except:
        return False

    try:
        new_cnpj = calculates_digit(cnpj=cnpj, digit=1)
        new_cnpj = calculates_digit(cnpj=new_cnpj, digit=2)
    except Exception as e:
        return False

    if new_cnpj == cnpj:
        return True
    else:
        return False


def calculates_digit(cnpj, digit):
    if digit == 1:
        regressives = REGRESSIVES[1:]
        new_cnpj = cnpj[:-2]
    elif digit == 2:
        regressives = REGRESSIVES
        new_cnpj = cnpj
    else:
        return None

    total = 0
    for index, regressive in enumerate(regressives):
        total += int(cnpj[index]) * regressive

    digit = 11 - (total % 11)
    digit = digit if digit <= 9 else 0

    return f'{new_cnpj}{digit}'


def is_sequence(cnpj):
    sequence = cnpj[0] * len(cnpj)

    if sequence == cnpj:
        return True
    else:
        return False


def only_numbers(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def generator():
    first_digit = random.randint(0, 9)
    second_digit = random.randint(0, 9)
    segund_bloc = random.randint(100, 999)
    third_bloc = random.randint(100, 999)
    fourth_bloc = '0001'

    start_cnpj = f'{first_digit}{second_digit}{segund_bloc}' \
        f'{third_bloc}{fourth_bloc}00'

    new_cnpj = calculates_digit(cnpj=start_cnpj, digit=1)
    new_cnpj = calculates_digit(cnpj=new_cnpj, digit=2)

    return new_cnpj


def formating(cnpj):
    cnpj = only_numbers(cnpj)
    formated = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formated
