"""

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))  # Alinhado a esquerda.
print('Prazer em te conhecer {:>20}!'.format(nome))  # Alinhado a direita.
print('Prazer em te conhecer {:^20}!'.format(nome))  # Alinhado ao centro.
# Alinhado ao centro acrescentando caracteres.
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# O resultado poderá ser limitado em casas decimais utilizando :.3f, onde f = float.
# Adicionando o \n, conseguimos fazer a quebra de linha.
print('A soma é {},\no produto é {},\na divisão é {:.3f},\na divisão inteira é {},\ne o expoente é {}'.format(s, m, d, di, e))

# Utilizando o " end='' ", podemos mostrar os resultados de 2 prints em uma linha.

print('A soma é {}, o produto é {}, a divisão é {:.3f},'.format(s, m, d), end=' ')
print('a divisão inteira é {}, o expoente é {}'.format(di, e))

# Desafio 5:
# Faça um programa que leia um número inteiro emostre na tela o seu sucessor e seu antecessor.

n = int(input('Digitel um número: '))
print('Analisando o valor {}, seu sucessor é {} e seu antecessor é {}'.format(
    n, n + 1, n - 1))

# Desafio 6:
# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('O dobro do seu número é {},\no triplo é {},\ne a raiz é {:.2f}.'.format(
    (n * 2), (n * 3), pow(n, 1/2)))

# Desafio 7:
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
média = (nota1 + nota2) / 2
print('A média entre {} e {} é {:.1f}'.format(nota1, nota2, média))
if média >= 7:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')

# Desafio 8:
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite o valor em metros: '))
medida = input('Digite a medida desejada (km, hm, dam, dm, cm, mm): ')
if (medida == 'km'):
    print('{} m equivalem a {} km'.format(metros, (metros * 0.001)))
elif (medida == 'hm'):
    print('{} m equivalem a {} hm'.format(metros, (metros * 0.01)))
elif (medida == 'dam'):
    print('{} m equivalem a {} dam'.format(metros, (metros * 0.1)))
elif (medida == 'dm'):
    print('{} m equivalem a {} dm'.format(metros, (metros * 10)))
elif (medida == 'cm'):
    print('{} m equivalem a {} cm'.format(metros, (metros * 100)))
elif (medida == 'mm'):
    print('{} m equivalem a {} mm'.format(metros, (metros * 1000)))

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

# Desafio 10:
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar (US$ 1 = R$ 3.27).

carteira = float(input('Quanto dinheiro você tem na carteira? '))
tipo_moeda = str(input('Qual a moeda que tem na carteira (R, US, EUR)? '))
if (tipo_moeda == 'R'):
    moeda_destino = input('Qual moeda de destino quer converter? (US, EUR)? ')
    if (moeda_destino == 'US'):
        dolar = carteira / 5.61
        print('O valor de sua carteira de {}$ {:.2f} equivale a {}$ {:.2f}.'.format(
            tipo_moeda, carteira, moeda_destino, dolar))
    elif (moeda_destino == 'EUR'):
        euro = carteira / 6.62
        print('O valor de sua carteira {}$ {:.2f} equivale a {}$ {:.2f}.'.format(
            tipo_moeda, carteira, moeda_destino, euro))
elif (tipo_moeda == 'US'):
    moeda_destino = input('Qual moeda de destino quer converter? (R, EUR)? ')
    if (moeda_destino == 'R'):
        real = carteira / 0.18
        print('O valor de sua carteira {}$ {:.2f} equivale a {}$ {:.2f}.'.format(
            tipo_moeda, carteira, moeda_destino, real))
    elif (moeda_destino == 'EUR'):
        euro = carteira / 1.18
        print('O valor de sua carteira {}$ {:.2f} equivale a {}$ {:.2f}.'.format(
            tipo_moeda, carteira, moeda_destino, euro))
elif (tipo_moeda == 'EUR'):
    moeda_destino = input('Qual moeda de destino quer converter? (R, US)? ')
    if (moeda_destino == 'R'):
        real = carteira / 0.15
        print('O valor de sua carteira {}$ {:.2f} equivale a {}$ {:.2f}.'.format(
            tipo_moeda, carteira, moeda_destino, real))
    elif (moeda_destino == 'US'):
        dolar = carteira / 0.85
        print('O valor de sua carteira {}$ {:.2f} equivale a {}$ {:.2f}.'.format(
            tipo_moeda, carteira, moeda_destino, dolar))

# Desafio 11:
Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2m2.

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg * alt
lt_tinta = área / 2  # 2m2 por litro
print(' A sua parede tem a dimensão de {:.2f} m X {:.2F} m e\n a área total é de {:.2f} m2, sendo assim\n você precisa de {:.1f} litros de tinta.'.format(
    larg, alt, área, lt_tinta))

# Desafio 12:
# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: R$ '))
novo_preço = preço * 0.95
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% custará R$ {:.2f}'.format(
    preço, novo_preço))

# Desafio 13:
# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Digite o seu salário atual: R$ '))
novo_salário = salário * 1.15
print('Um funcionário que ganha um salário de R$ {:.2f}, com acrescido de 15% irá ganhar R$ {:.2f}'.format(
    salário, novo_salário))

"""
