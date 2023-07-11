# Desafio 86:
# Crie um programa que declare uma matriz de dimensão 3X3 e preencha com
# valores lidos pelo teclado. No final, mostre a matriz na tela, com a
# formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
print('&'*40)
print(matriz)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
