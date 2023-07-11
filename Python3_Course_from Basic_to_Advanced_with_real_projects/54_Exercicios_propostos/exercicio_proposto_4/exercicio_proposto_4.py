"""
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne
fizz, se o parâmetro da função for divisível por 5 retorne buzz.
Se o parâmetro da função for divisível por 5 e por 3, retorne
FizzBuzz, caso contrário, retorne o número enviado.
"""
from random import randint


def fizzbuzz(num):
    num = int(num)
    if num % 3 == 0 and num % 5 == 0:
        return f'fizzbuzz, {num} é divisível por 3 e 5'
    if num % 5 == 0:
        return f'buzz, {num} é divisível por 5'
    if num % 3 == 0:
        return f'fizz, {num} é divisível por 3'
    return f'O número digitado é {num}.'


"""
print(fizzbuzz(7))
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(22))

"""
for i in range(100):
    aleatorio = randint(0, 100)
    print(fizzbuzz(aleatorio))
