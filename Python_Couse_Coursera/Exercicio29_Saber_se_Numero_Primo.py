def éPrimo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True


num = int(input("Digite um número inteiro: "))
while num > 0:
    if éPrimo(num):
        print(num, "é primo!")
    else:
        print(num, "não é primo!")
    num = int(input("Digite um número inteiro: "))
