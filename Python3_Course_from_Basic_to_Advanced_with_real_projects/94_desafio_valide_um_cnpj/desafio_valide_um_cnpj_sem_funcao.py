"""
04.252.011/0001-10
40.688.134/0001-61
71.506.168/0001-11
12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1  # multiplica (0*5, 4*4, etc)
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65 (soma dos resultados)
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

cnpj = '04.252.011/0001-10'
dig1_mult = '543298765432'
dig2_mult = '6543298765432'
soma_dig1 = int()
soma_dig2 = int()

# Analisando e substituindo os caractéres
for c in cnpj:
    if not c.isdigit():
        cnpj = cnpj.replace(c, '')

cnpj_sem_digitos = cnpj[0:12]

# Calculando o primeiro dígito
for i1 in range(0, 12):
    soma_dig1 += int(cnpj_sem_digitos[i1]) * int(dig1_mult[i1])

form_dig1 = 11 - (soma_dig1 % 11)
if form_dig1 > 9:
    form_dig1 = 0
else:
    form_dig1

cnpj_dig1 = cnpj_sem_digitos + str(form_dig1)

# Calculando o segundo dígito
for i2 in range(0, 13):
    soma_dig2 += int(cnpj_dig1[i2]) * int(dig2_mult[i2])

form_dig2 = 11 - (soma_dig2 % 11)
if form_dig2 > 9:
    form_dig2 = 0
else:
    form_dig2

cnpj_dig2 = cnpj_dig1 + str(form_dig2)

if cnpj == cnpj_dig2:
    print(f'O CNPJ {cnpj_dig2} é VÁLIDO!!')
else:
    print(f'O CNPJ {cnpj_dig2} é INVÁLIDO!!')
