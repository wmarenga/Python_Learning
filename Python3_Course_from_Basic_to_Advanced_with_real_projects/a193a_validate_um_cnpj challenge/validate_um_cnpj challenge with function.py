from my_module_cnpj import module

cnpj = '04.252.011/0001-10'

no_characters = module.remove_characters(cnpj)
cnpj13 = module.calc_digits1(no_characters)
cnpj14 = module.calc_digits2(cnpj13)

if no_characters == cnpj14:
    print(f'The CNPJ {cnpj} is VALID!!')
else:
    print(f'The CNPJ {cnpj} is NOT VALID!!')
