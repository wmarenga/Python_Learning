"""
Exercício 32: Primos
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 
como parâmetro e devolve a quantidade de números primos que existem entre 2 e n 
(incluindo 2 e, se for o caso, n).

Exemplo:

>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30
"""


def primo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True


limite = int(input("Limite máximo: "))

n = 2
while n < limite:
    if primo(n):
        print(n, end=", ")
    n += 1


def n_primos(x):
    i = 2
    count = 0
    fator = 2
    while(i <= x):
        if(primo(i)):
            count = count + 1
        i = i + 1
    return count


# print(n_primos(int(input('Numero: '))))
