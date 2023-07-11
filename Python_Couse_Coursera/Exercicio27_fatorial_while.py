
num = int(input('Digite o valor de n: '))
while num >= 0:
    fatorial = 1
    while num > 1:
        fatorial = fatorial * num
        num -= 1
    print(fatorial)
    print('Digite um número negativo para sair!')
    num = int(input('Digite o valor de n (negarivo para sair!): '))
