# Desafio 87:
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados;
# B) A soma dos valores da terceira coluna;
# C) O maior valor da segunda linha.
"""
   ________________________
0 |    |    |    |    |    |
  |____|____|____|____|____|
1 |    |    |    |    |    |
  |____|____|____|____|____|
2 |    |    |    |    |    |
  |____|____|____|____|____|
    0    1    2    0     1
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = terceira = det = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
        if matriz[lin][col] % 2 == 0:
            pares += matriz[lin][col]
        if col == 2:
            terceira += matriz[lin][col]
        if det == 0:
            diagonaldir = (matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[0][1]
                                                                    * matriz[1][2]*matriz[2][0])+(matriz[0][2]*matriz[1][0]*matriz[2][1])
            diagonalesq = (matriz[0][2]*matriz[1][1]*matriz[2][0]) + (
                matriz[0][0]*matriz[1][2]*matriz[2][1]) + (matriz[0][1]*matriz[1][0]*matriz[2][2])
            determinante = diagonaldir - diagonalesq
        if lin == 1:
            if matriz[lin][col] == 0:
                maior = matriz[lin][col]
            elif matriz[lin][col] > maior:
                maior = matriz[lin][col]
            elif matriz[lin][col] < maior:
                maior = maior
print('&'*40)
print(matriz)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')
print(f'A determinante da matriz é {determinante}.')
print()
