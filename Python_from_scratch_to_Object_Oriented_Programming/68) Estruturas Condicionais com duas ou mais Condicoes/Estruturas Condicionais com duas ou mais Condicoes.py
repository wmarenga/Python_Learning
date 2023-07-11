# 2 ou mais condicoes sendo verdadeiras

num1 = 12
num2 = 44
nome1 = 'Fernando'
nome2 = 'Maria'

if num1 >= 10 and nome1 == 'Fernando':
    print(f'Numero maior que 10 e o usuario e {nome1}')
if num1 <= 10 and nome1 == 'Fernando':
    print(f'Numero menor que 10 e o usuario e {nome1}')
if num1 == num2 and nome2 == 'Maria':
    print(f'Numero 1 e o numero 2 sao iguais, assim como o usuario e {nome2}')
if num1 != num2 and nome2 == 'Maria':
    print(
        f'Numero 1 e o numero 2 sao diferentes, assim como o usuario e {nome2}')
# Operador and exige que as duas condicoes sejam verdadeiras (uma condicao e outra)
