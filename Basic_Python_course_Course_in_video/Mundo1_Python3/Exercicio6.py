# Desafio 6:
# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('O dobro do seu número é {},\no triplo é {},\ne a raiz é {:.2f}.'.format(
    (n * 2), (n * 3), pow(n, 1/2)))
