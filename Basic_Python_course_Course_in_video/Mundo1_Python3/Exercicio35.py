# Desafio 35:
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

# Maneira matemática:

lado1 = int(input('Digite o primeiro lado do triângulo: '))
lado2 = int(input('Digite o segundo lado do triângulo: '))
lado3 = int(input('Digite o terceiro lado do triângulo: '))

if abs(lado2-lado3) < lado3 and (lado2 + lado3) > lado3 and abs(lado1-lado3) < lado2 and (lado1 + lado3) > lado2 and abs(lado1-lado2) < lado3 and (lado1 + lado2) > lado3:
    print('Com as medidas informada conseguimos formar um TRIÂNGULO.')
else:
    print('IMPOSSÍVEL formar um triângulo com as medidas dos lados.')

# Outra maneira:

lado1 = int(input('Digite o primeiro lado do triângulo: '))
lado2 = int(input('Digite o segundo lado do triângulo: '))
lado3 = int(input('Digite o terceiro lado do triângulo: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Com as medidas informada conseguimos formar um TRIÂNGULO.')
else:
    print('IMPOSSÍVEL formar um triângulo com as medidas dos lados.')
