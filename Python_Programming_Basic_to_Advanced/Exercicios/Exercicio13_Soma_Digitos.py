num = int(input('Digite um número: '))
soma = 0
while num != 0:
    dígito = num % (10)
    soma += dígito
    num = num // (10)
print(soma)
