# Desafio 79:
# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma LISTA. Caso o número já exista lá dentro, ele NÃO
# SERÁ ADICIONADO. No final, serão exibidoas todos os valores únicos
# digitados, em ordem crescente.

números = []
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor Duplicado! Não é possível adicioná-lo.')
    decisão = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if decisão == 'N':
        break
print('-='*40)
números.sort()
print(f'Você digitou os valores {números}')
