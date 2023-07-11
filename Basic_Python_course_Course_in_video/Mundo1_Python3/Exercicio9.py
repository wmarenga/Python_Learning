# Desafio 9:
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número inteiro e saiba a sua tabuada: '))
f = 0
print('-'*50)
while f < 10:
    f += 1
    # f -= 1 (decremento)
    # f *= 2 (incremento multiplicado por 2)
    # f /= 2 (incremento dividindo por 2)
    # f //= 2 ( incremento dividindo o resultado inteiro)
    m = n * f
    print('{} X {:>2} = {}'.format(n, f, m))
