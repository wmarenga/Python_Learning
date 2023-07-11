# Exercicio 19 - Coeficiente Binomial:
# (n: k) = n! / k! * (n - k)!

def fatorial(n):
    fat = 1
    while n > 0:
        fat *= n
        n -= 1
    return(fat)


def coef_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))


n = int(input('Digite o valor de n: '))
k = int(input('Digite o valor de k: '))
if n < k:
    print(0)
else:
    print(f'{coef_binomial(n, k):.0f}')
