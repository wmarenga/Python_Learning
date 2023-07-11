# Desafio 101:
# Crie um programa que tenha uma função chamada VOTO() que
# vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Você tem {idade} anos, seu voto foi NEGADO!'
    elif 18 > idade >= 16 or idade >= 65:
        return f'Você tem {idade} anos, seu voto é OPCIONAL!'
    else:
        return f'Você tem {idade} anos, o seu voto é OBRIGATÓRIO!'


# PROGRAMA PRINCIPAL:
print(voto(int(input('Em que ano você nasceu? '))))
