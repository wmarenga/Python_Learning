# Exercicio 8 - FizzBuzz parcial, parte 2:
# Receba um número inteiro na entrada e imprima
# Buzz
# se o número for divisível por 5. Caso contrário,
# imprima o mesmo número que foi dado na entrada.

num = int(input('Digite um número: '))
if num % 5 == 0:
    print('Buzz')
else:
    print(num)
