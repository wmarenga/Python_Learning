# Exercicio 15 - Ímpares:
# Receba um número inteiro positivo na entrada e imprima os n
# primeiros números ímpares naturais. Para a saída, siga o formato
# do exemplo abaixo.
# Exemplo:
# Digite o valor de n: 5
# 1
# 3
# 5
# 7
# 9

n = int(input("Digite o valor de n: "))

i = 1

while i <= (2*n):
    if i % 2 != 0:
        print(i)
        i += 1
    else:
        i += 1
