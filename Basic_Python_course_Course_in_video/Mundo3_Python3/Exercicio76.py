# Desafio 76:
# Crie um programa que tenha uma Tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

list = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
        4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<31}', end='')
    else:
        print(f'R${list[pos]:>7.2f}')
print('-'*40)
