# Desafio 41:
# A confederação Nacional de Natação precisa de um programador
# que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM;
# Até 14 anos: INFANTIL;
# Até 19 anos: JUNIOR:
# Até 20 anos: SENIOR;
# Acima: MASTER.

from datetime import date
nasc = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
if idade <= 9:
    print(
        'Você tem \033[7;35m{} anos\033[m e sua categoria é \033[7;35mMIRIM!\033[m'.format(idade))
elif idade <= 14:
    print(
        'Você tem \033[7;33m{} anos\033[m e sua categoria é \033[7;33mINFANTIL!\033[m'.format(idade))
elif idade <= 19:
    print(
        'Você tem \033[7;36m{} anos\033[m e sua categoria é \033[7;36mJUNIOR!\033[m'.format(idade))
elif idade <= 20:
    print(
        'Você tem \033[7;32m{} anos\033[m e sua categoria é \033[7;32mSENIOR!\033[m'.format(idade))
elif idade > 20:
    print(
        'Você tem \033[7;34m{} anos\033[m e sua categoria é \033[7;34mMASTER!\033[m'.format(idade))

# Também posso usar o "else"
# else:
#    print('Você tem \033[7;34m{} anos\033[m e sua categoria é \033[7;34mMASTER!\033[m'.format(idade))