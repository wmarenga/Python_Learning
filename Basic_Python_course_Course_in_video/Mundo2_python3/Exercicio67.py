# Desafio 67:
# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O
# programa será INTERROMPIDO quando o número solicitado for
# negativo.

fator = 1
# Temos que usar um loop infinito (True).
while True:
    print('-'*30)
    num = int(input("Quer ver a tabuada de qual valor? "))
    print('-'*30)
    if num < 0:
        break
    for fator in range(1, 11):
        mult = num * fator
        print(f'{num} X {fator} = {mult}')
        fator += 1
print('Digitou um valor negativo. ACABOU!')
