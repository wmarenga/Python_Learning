def remover_caracteres(cnpj_num):
    for c in cnpj_num:
        if not c.isdigit():
            cnpj_num = cnpj_num.replace(c, '')
    return cnpj_num


def calc_digitos1(cnpj):
    dig1_mult = '543298765432'
    soma_dig1 = int()
    cnpj12 = cnpj[0:12]
    for i in range(0, 12):
        soma_dig1 += int(cnpj12[i]) * int(dig1_mult[i])

    form_dig1 = 11 - (soma_dig1 % 11)
    if form_dig1 > 9:
        form_dig1 = 0
        cnpj13 = cnpj12 + str(form_dig1)
        return cnpj13
    else:
        form_dig1
        cnpj13 = cnpj12 + str(form_dig1)
        return cnpj13


def calc_digitos2(cnpj13):
    dig2_mult = '6543298765432'
    soma_dig2 = int()
    for i in range(0, len(dig2_mult)):
        soma_dig2 += int(cnpj13[i]) * int(dig2_mult[i])
    form_dig2 = 11 - (soma_dig2 % 11)
    if form_dig2 > 9:
        form_dig2 = 0
        cnpj14 = cnpj13 + str(form_dig2)
        return cnpj14
    else:
        form_dig2
        cnpj14 = cnpj13 + str(form_dig2)
        return cnpj14
