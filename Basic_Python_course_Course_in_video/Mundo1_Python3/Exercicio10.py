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
