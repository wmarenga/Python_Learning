# Desafio 39:
# Faça um programa que leia o ano de nascimento de um jovem e
# informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que
# passou do prazo.

from datetime import date
ano_nasc = int(input('Digite ano de seu nascimento: '))
ano_atual = date.today().year
# Outra maneira: ano_atual = int(datetime.now().strftime('%Y'))
idade = ano_atual - ano_nasc
if idade < 18:
    print('Quem nasceu em \033[1;32m{}\033[m tem {} anos em {}.\nAinda faltam {} anos para o alistamento.\nSue alistamento será em {}.'.format(
        ano_nasc, idade, ano_atual, 18 - idade, ano_atual - 18))
elif idade == 18:
    print('Quem nasceu em \033[1;32m{}\033[m tem {} anos em {}.\nVocê tem que se alistar IMEDIATAMENTE!'.format(
        ano_nasc, idade, ano_atual))
elif idade > 18:
    print('Quem nasceu em \033[1;32m{}\033[m tem {} anos em {}. \nVocê já deveria ter se alistado há \033[1;33;41m{}\033[m anos.\nSeu alistamento foi em \033[1;33;41m{}\033[m.'.format(
        ano_nasc, idade, ano_atual, idade - 18, ano_atual - 18))
