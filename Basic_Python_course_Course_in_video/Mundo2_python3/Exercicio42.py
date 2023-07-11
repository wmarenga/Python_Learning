# Desafio 42:
# Refaça o desafio 35, dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# 1) Equilátero: todos os lados iguais;
# 2) Isósceles: dois lados iguais;
# 3) Escaleno: todos os lados diferentes.

# Maneira matemática:

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))
if abs(lado2-lado3) < lado3 and (lado2 + lado3) > lado3 and abs(lado1-lado3) < lado2 and (lado1 + lado3) > lado2 and abs(lado1-lado2) < lado3 and (lado1 + lado2) > lado3:
    print('Os lados informados formam um triângulo')
    if lado1 == lado2 == lado3:
        print('Com as medidas informada \033[1;32m{:.2f}, {:.2f}, {:.2f}\033[m formamos um \033[7;32mTriângulo Equilátero\033[m.'.format(
            lado1, lado2, lado3))
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Com as medidas informada \033[1;34m{:.2f}, {:.2f}, {:.2f}\033[m formamos um \033[7;34mTriângulo Isósceles\033[m.'.format(
            lado1, lado2, lado3))
    else:
        print('Com as medidas informada \033[1;35m{:.2f}, {:.2f}, {:.2f}\033[m formamos um \033[7;35mTriângulo Escaleno\033[m.'.format(
            lado1, lado2, lado3))
else:
    print('IMPOSSÍVEL formar um triângulo com as medidas dos lados.')
