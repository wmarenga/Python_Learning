# Desafio 34:
# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento.
# 1) Para salários superiores a R$ 1250.00, calcule um aumento de 10%.
# 2) Para os salários inferiores ou iguais, o aumento é de 15 %.

salário = float(input('Digite o seu salário: '))
if salário > 1250:
    aumento10 = salário * 1.1
    print('O seu salário atual é R$ {:.2f} e o seu novo salário com aumento de 10% é \033[1;33;41mR$ {:.2f}\033[m.'.format(
        salário, aumento10))
else:
    aumento15 = salário * 1.15
    print('O seu salário atual é R$ {:.2f} e o seu novo salário com aumento de 15% é \033[1;33;41mR$ {:.2f}\033[m.'.format(
        salário, aumento15))
