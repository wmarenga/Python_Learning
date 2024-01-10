import re

# Constant
REGRESSIVES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valid(cnpj):
    cnpj = only_numbers(cnpj)

    try:
        if is_sequence(cnpj):
            return False
    except:
        return False

    try:
        new_cnpj = calculate_digit(cnpj=cnpj, digit=1)
        new_cnpj = calculate_digit(cnpj=new_cnpj, digit=2)
    except Exception as e:
        return False

    if new_cnpj == cnpj:
        return True
    else:
        return False


def calculate_digit(cnpj, digit):
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
