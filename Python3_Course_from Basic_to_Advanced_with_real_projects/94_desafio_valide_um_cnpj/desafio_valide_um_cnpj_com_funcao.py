from meu_modulo_cnpj import modulo

cnpj = '04.252.011/0001-10'

sem_caracteres = modulo.remover_caracteres(cnpj)
cnpj13 = modulo.calc_digitos1(sem_caracteres)
cnpj14 = modulo.calc_digitos2(cnpj13)

if sem_caracteres == cnpj14:
    print(f'O CNPJ {cnpj} é VÁLIDO!!')
else:
    print(f'O CNPJ {cnpj} é INVÁLIDO!!')
