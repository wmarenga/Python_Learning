# Desafio 104:
# Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante a função INPUT() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico.
# Ex. n = leiaInt('Digite um n:').

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


# PROGRAMA PRINCIPAL:
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
