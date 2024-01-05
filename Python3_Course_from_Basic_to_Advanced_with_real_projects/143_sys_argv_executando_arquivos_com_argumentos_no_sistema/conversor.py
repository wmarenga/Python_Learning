def dec_to_bin(num):
    binario = list()
    while num >= 1:ö
        resto = num % 2
        result = num // 2
        binario.insert(0, resto)
        num = result
    else:
        return binario


def bin_to_dec(num):
    num.reverse()
    total = 0
    for i, n in enumerate(num):
        total += (n * (2 ** i))
    return total


print(dec_to_bin(31))
print(bin_to_dec([1, 1, 0, 0, 1]))
