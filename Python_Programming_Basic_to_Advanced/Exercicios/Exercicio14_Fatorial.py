# Exercício 14 - Fatorial
# Escreva um programa que receba um número natural n
# n na entrada e imprima n!
# n! (fatorial) na saída.
# Exemplo:
# Digite o valor de n: 5
# 120
# Dica: lembre-se que o fatorial de 0 vale 1!
num = int(input('Digite o valor de n: '))
count = num
f = 1
while count > 0:
    f *= count
    count -= 1
print(f)
