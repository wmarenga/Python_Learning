"""
Quantidade de caracteres (len):

Conta os elementos de uma str, list, set, tuple, dict.

Obs: Não funciona com tipos numéricos (int, float e bool).
Obs: O retorno de len é um int (TypeError)

while True:
    usuario = input('Digite seu usuário: ')
    qtd_caracteres = len(usuario)
    if qtd_caracteres < 6:
        print('Você precisa digitar pelo menos 6 caracteres.')
    else:
        print('Você foi cadastrado no sistema.')
        print(usuario, qtd_caracteres, type(qtd_caracteres))

"""

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(
    f'A quantidade total de caracteres digitados foi: {len(string1) + len(string2)}')

print(len(string2))
print(string2.__len__())  # É a mesma coisa.
