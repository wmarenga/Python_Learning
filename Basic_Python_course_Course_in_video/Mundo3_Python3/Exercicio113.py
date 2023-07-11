# Desafio 113 - Funções Aprofundadas em Python:
# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma
# funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mERRO: por favor, digite um número inteiro válido:\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digital este número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[31mERRO: por favor, digite um número inteiro válido:\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digital este número.\033[m')
            return 0
        else:
            return n


# PROGRAMA PRINCIPAL:
numi = leiaInt('Digite um número: ')
print(f'Você digitou o número {numi}.')

numf = leiaFloat('Digite um número: ')
print(f'Você digitou o número {numf}.')
